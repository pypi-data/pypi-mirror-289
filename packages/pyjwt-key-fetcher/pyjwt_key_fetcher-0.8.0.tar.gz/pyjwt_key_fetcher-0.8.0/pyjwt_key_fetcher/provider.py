from typing import Any, Callable, Dict, Mapping, Optional, TypedDict, Union
from uuid import uuid4

import aiocache  # type: ignore

from pyjwt_key_fetcher.errors import (
    JWTKeyNotFoundError,
    JWTProviderConfigError,
    JWTProviderJWKSError,
)
from pyjwt_key_fetcher.http_client import HTTPClient
from pyjwt_key_fetcher.key import Key


def key_builder(
    f: Callable[..., Any], *args: "Provider", **kwargs: Dict[str, Any]
) -> str:
    """
    Custom key builder for aiocache that uses the self.uuid instead of serializing
    self to something that contains some memory address that might get reused later,
    like for example <pyjwt_key_fetcher.provider.Provider object at 0x120e9a070>.

    This is especially a possible problem in tests that might create a lot of
    instances and some might end up at the same memory addresses as previously
    existing ones.
    """
    ordered_kwargs = sorted(kwargs.items())
    key = (
        f.__module__
        + f.__name__
        + "."
        + str(args[0].uuid)
        + "."
        + str(args[1:])
        + str(ordered_kwargs)
    )
    return key


class JwksUriConfigurationTypeDef(TypedDict):
    """
    Type definition for an OpenID Connect compatible configuration with a jwks_uri.
    """

    jwks_uri: str


class JwksUrlConfigurationTypeDef(TypedDict):
    """
    Type definition for a configuration using jwks_url instead of jwks_uri.
    """

    jwks_url: str


ConfigurationTypeDef = Union[JwksUriConfigurationTypeDef, JwksUrlConfigurationTypeDef]


class Provider:
    def __init__(
        self,
        iss: str,
        http_client: HTTPClient,
        config_path: str = "/.well-known/openid-configuration",
        static_config: Optional[ConfigurationTypeDef] = None,
    ) -> None:
        self.iss = iss
        self.http_client = http_client
        self._configuration: Optional[Mapping[str, Any]] = static_config
        self._jwk_map: Dict[str, Dict[str, Any]] = {}
        self.keys: Dict[str, Key] = {}
        self.config_path = config_path
        self.uuid = uuid4()

    async def _config_uri(self) -> str:
        """
        Get the URI at which the configuration is expected to be found.

        Can be for example https://example.com/.well-known/openid-configuration
        :return: The configuration URI.
        """
        return f"{self.iss.rstrip('/')}{self.config_path}"

    async def get_configuration(self) -> Mapping[str, Any]:
        """
        Get the configuration as a dictionary.

        :return: The configuration as a dictionary.
        :raise JWTHTTPFetchError: If there's a problem fetching the data.
        """
        if self._configuration is None:
            url = await self._config_uri()
            self._configuration = await self.http_client.get_json(url)

        return self._configuration

    async def _get_jwks_uri(self) -> str:
        """
        Retrieve the uri/url to JWKs.

        :return: The uri/url to the JWKs.
        :raise JWTHTTPFetchError: If there's a problem fetching the data.
        :raise JWTProviderConfigError: If the config doesn't contain "jwks_uri" or
        "jwks_url".
        """
        conf = await self.get_configuration()
        jwks_uri: str
        try:
            jwks_uri = conf["jwks_uri"]
        except KeyError as e:
            try:
                jwks_uri = conf["jwks_url"]
            except KeyError:
                raise JWTProviderConfigError(
                    "Missing 'jwks_uri' and 'jwks_url' in configuration"
                ) from e
        return jwks_uri

    @aiocache.cached(ttl=300, key_builder=key_builder)
    async def _fetch_jwk_map(self) -> Dict[str, Dict[str, Any]]:
        """
        Get all JWKs for an issuer as a dictionary with kid as key.

        Rate limited to once per 5 minutes (300 seconds).

        :return: A mapping of {kid: {<data_for_the_kid>}, ...}
        :raise JWTHTTPFetchError: If there's a problem fetching the data.
        :raise JWTProviderConfigError: If the config doesn't contain "jwks_uri".
        :raise JWTProviderJWKSError: If the jwks_uri is missing the "keys".
        """
        jwks_uri = await self._get_jwks_uri()
        data = await self.http_client.get_json(jwks_uri)
        try:
            jwks_list = data["keys"]
        except KeyError as e:
            raise JWTProviderJWKSError(f"Missing 'keys' in {jwks_uri}") from e

        jwk_map = {jwk["kid"]: jwk for jwk in jwks_list}

        return jwk_map

    async def get_jwk_data(self, kid: str) -> Dict[str, Any]:
        """
        Get the raw data for a jwk based on kid.

        :param kid: The key ID.
        :return: The raw JWK data as a dictionary.
        :raise JWTHTTPFetchError: If there's a problem fetching the data.
        :raise JWTProviderConfigError: If the config doesn't contain "jwks_uri".
        :raise JWTProviderJWKSError: If the jwks_uri is missing the "keys".
        :raise JWTKeyNotFoundError: If no matching kid was found.
        """
        if kid not in self._jwk_map:
            self._jwk_map = await self._fetch_jwk_map()
        try:
            return self._jwk_map[kid]
        except KeyError:
            raise JWTKeyNotFoundError

    async def get_key(self, kid: str) -> Key:
        """
        Get the Key for a particular kid.

        :param kid: The key id.
        :return: The Key.
        :raise JWTHTTPFetchError: If there's a problem fetching the data.
        :raise JWTProviderConfigError: If the config doesn't contain "jwks_uri".
        :raise JWTProviderJWKSError: If the jwks_uri is missing the "keys".
        :raise JWTKeyNotFoundError: If no matching kid was found.
        """
        if kid not in self.keys:
            key = Key(await self.get_jwk_data(kid))
            self.keys[kid] = key

        return self.keys[kid]
