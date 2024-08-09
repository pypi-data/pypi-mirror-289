"""Provides a class for interacting with the ABB-free@home API."""

import asyncio
from collections.abc import Callable
import inspect
import logging
from typing import Any
from urllib.parse import urlparse

import aiohttp

from .exceptions import (
    ConnectionTimeoutException,
    ForbiddenAuthException,
    InvalidApiResponseException,
    InvalidCredentialsException,
    InvalidHostException,
    SetDatapointFailureException,
    UserNotFoundException,
)

API_VERSION = "v1"

_LOGGER = logging.getLogger(__name__)


class FreeAtHomeApi:
    """Provides a class for interacting with the ABB-free@home API."""

    _ws_session: aiohttp.ClientSession = None
    _ws_response: aiohttp.ClientWebSocketResponse = None

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        sysap_uuid: str = "00000000-0000-0000-0000-000000000000",
    ) -> None:
        """Initialize the FreeAtHomeApi class."""
        self._sysap_uuid = sysap_uuid
        self._host = host.rstrip("/")
        self._username = username
        self._password = password

    async def __aexit__(self, *_exc_info: object):
        """Close websocket connection."""
        await self.ws_close()

    async def get_configuration(self) -> dict:
        """Get the Free@Home Configuration."""
        _response = await self._request(path="/api/rest/configuration")

        return _response.get(self._sysap_uuid)

    async def get_datapoint(
        self, device_id: str, channel_id: str, datapoint: str
    ) -> list[str]:
        """Get a specific datapoint from the api."""
        _response = await self._request(
            path=f"/api/rest/datapoint/{self._sysap_uuid}/{device_id}.{channel_id}.{datapoint}",
            method="get",
        )

        return _response.get(self._sysap_uuid).get("values")

    async def get_device_list(self) -> list:
        """Get the list of devices."""
        _response = await self._request(path="/api/rest/devicelist")

        return _response.get(self._sysap_uuid)

    async def get_device(self, device_serial: str):
        """Get a specific device from the api."""
        _response = await self._request(
            path=f"/api/rest/device/{self._sysap_uuid}/{device_serial}"
        )

        return _response.get(self._sysap_uuid).get("devices").get(device_serial)

    async def get_settings(self):
        """Get the settings from the api."""
        try:
            async with aiohttp.ClientSession() as session:  # noqa: SIM117
                async with session.get(f"{self._host}/settings.json") as resp:
                    _response_status = resp.status
                    _response_json = await resp.json()
        except ValueError as e:
            if str(e) == "URL should be absolute":
                raise InvalidHostException(self._host) from e
            raise

        assert _response_status == 200
        return _response_json

    async def get_sysap(self):
        """Get the sysap from the api."""
        return await self._request(path="/api/rest/sysap")

    async def get_user(self, name: str) -> str:
        """Get a specific user from the api."""
        _settings = await self.get_settings()

        _user = next(
            iter(user for user in _settings.get("users") if user.get("name") == name),
            None,
        )

        if _user is None:
            raise UserNotFoundException(name)

        return _user

    async def set_datapoint(
        self, device_id: str, channel_id: str, datapoint: str, value: str
    ) -> bool:
        """Set a specific datapoint in the api. This is used to control devices."""
        _response = await self._request(
            path=f"/api/rest/datapoint/{self._sysap_uuid}/{device_id}.{channel_id}.{datapoint}",
            method="put",
            data=value,
        )

        if _response.get(self._sysap_uuid).get("result").lower() != "ok":
            raise SetDatapointFailureException(device_id, channel_id, datapoint, value)

        return True

    async def _request(self, path: str, method: str = "get", data: Any | None = None):
        """Make a request to the API."""

        # Set the full path to be used.
        if path[0] != "/":
            path = f"/{path}"
        _full_path = f"/fhapi/{API_VERSION}{path}"

        try:
            async with aiohttp.ClientSession(  # noqa: SIM117
                base_url=self._host,
                auth=aiohttp.BasicAuth(self._username, self._password),
            ) as client:
                async with client.request(
                    method=method, url=_full_path, data=data
                ) as resp:
                    _response_status = resp.status
                    _response = None
                    if resp.content_type == "application/json":
                        _response = await resp.json()
                    elif resp.content_type == "text/plain":
                        _response = await resp.text()
        except ValueError as e:
            if str(e) == "URL should be absolute":
                raise InvalidHostException(self._host) from e
            raise

        # Check the status code and raise exception accordingly.
        if _response_status == 401:
            raise InvalidCredentialsException(self._username)
        if _response_status == 403:
            raise ForbiddenAuthException(path)
        if _response_status == 502:
            raise ConnectionTimeoutException(self._host)

        try:
            assert _response_status == 200
        except AssertionError:
            raise InvalidApiResponseException(_response_status) from None

        return _response

    @property
    def ws_connected(self) -> bool:
        """Returns whether the websocket is connected."""
        return self._ws_response is not None and not self._ws_response.closed

    async def ws_close(self):
        """Close the websocket session."""
        await self.ws_disconnect()

        if self._ws_session:
            await self._ws_session.close()

    async def ws_connect(self):
        """Connect to the host websocket."""

        _parsed_host = urlparse(self._host)
        _full_path = f"{_parsed_host.hostname}/fhapi/{API_VERSION}/api/ws"
        _url = f"ws://{_full_path}"

        if self.ws_connected:
            return

        _timeout = aiohttp.ClientTimeout(total=10)
        if self._ws_session is None:
            self._ws_session = aiohttp.ClientSession(
                auth=aiohttp.BasicAuth(self._username, self._password), timeout=_timeout
            )

        _LOGGER.info("Websocket attempting to connect %s", _url)
        self._ws_response = await self._ws_session.ws_connect(url=_url)
        _LOGGER.info("Websocket connected %s", _url)

    async def ws_disconnect(self):
        """Close the websockets connection."""
        if not self._ws_response or not self.ws_connected:
            return

        await self._ws_response.close()

    async def ws_listen(
        self, callback: Callable[[list], None], retry_interval: int = 5
    ):
        """Listen for evens on the websocket. For known errors sleep for an interval and attempt again."""
        while True:
            if not self._ws_response or not self.ws_connected:
                try:
                    await self.ws_connect()
                except aiohttp.WSServerHandshakeError as ex:
                    _LOGGER.error(
                        "Websocket Handshake Connection Error. %s", ex.message
                    )
                    await asyncio.sleep(retry_interval)
                    continue
                except aiohttp.ClientConnectionError as ex:
                    _LOGGER.error("Websocket Client Connection Error. %s", ex)
                    await asyncio.sleep(retry_interval)
                    continue
                except TimeoutError as ex:
                    _LOGGER.error("Timeout waiting for host. %s", ex)
                    await asyncio.sleep(retry_interval)
                    continue

            data = await self._ws_response.receive()
            if data.type == aiohttp.WSMsgType.TEXT:
                _ws_data = data.json().get(self._sysap_uuid)
                if inspect.iscoroutinefunction(callback):
                    await callback(_ws_data)
                else:
                    callback(_ws_data)
            elif data.type == aiohttp.WSMsgType.ERROR:
                _LOGGER.error("Websocket Response Error. Data: %s", data)
                await asyncio.sleep(retry_interval)
            elif data.type in (
                aiohttp.WSMsgType.CLOSE,
                aiohttp.WSMsgType.CLOSED,
                aiohttp.WSMsgType.CLOSING,
            ):
                _LOGGER.warning("Websocket Connection Closed.")
                await asyncio.sleep(retry_interval)


if __name__ == "__main__":
    pass
