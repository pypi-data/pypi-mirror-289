"""
API wrapper for Outline VPN
"""
import asyncio

import aiohttp

from .exceptions import OutlineServerErrorException
from .structs import OutlineKey
from .utils import get_aiohttp_fingerprint


class OutlineVPN:
    """
    An Outline VPN connection
    """

    def __init__(self, api_url: str):
        self.api_url = api_url
        self.session: aiohttp.ClientSession | None = None

    async def init(self, cert_sha256: str = None):
        if cert_sha256:
            connector = aiohttp.TCPConnector(
                ssl=get_aiohttp_fingerprint(ssl_assert_fingerprint=cert_sha256)
            )
            session = aiohttp.ClientSession(connector=connector)
            self.session = session
        else:
            self.session = aiohttp.ClientSession()

    async def _get_metrics(self) -> dict:
        async with self.session.get(url=f"{self.api_url}/metrics/transfer") as resp:
            resp_json = await resp.json()
            if resp.status >= 400 or "bytesTransferredByUserId" not in resp_json:
                raise OutlineServerErrorException("Unable to get metrics")

            return resp_json

    async def _get_raw_keys(self) -> list[OutlineKey]:
        async with self.session.get(
            url=f"{self.api_url}/access-keys/",
        ) as resp:
            response_data = await resp.json()
            if resp.status != 200 or "accessKeys" not in response_data:
                raise OutlineServerErrorException("Unable to retrieve keys")

        return [OutlineKey.from_key_json(key_data) for key_data in response_data.get("accessKeys", [])]

    async def get_key(self, key_id: int) -> OutlineKey:
        async with self.session.get(
                url=f"{self.api_url}/access-keys/{key_id}"
        ) as resp:
            if resp.status != 200:
                raise OutlineServerErrorException("Unable to retrieve keys")
            client_data = OutlineKey.from_key_json(await resp.json())
        current_metrics = await self._get_metrics()

        client_data.used_bytes = current_metrics.get("bytesTransferredByUserId").get(client_data.key_id)
        return client_data

    async def _fulfill_keys_with_metrics(self, keys: list[OutlineKey]) -> list[OutlineKey]:
        current_metrics = await self._get_metrics()

        for key in keys:
            key.used_bytes = current_metrics.get("bytesTransferredByUserId").get(key.key_id)
        return keys

    async def get_keys(self):
        """Get all keys in the outline server"""
        raw_keys = await self._get_raw_keys()

        result_keys = await self._fulfill_keys_with_metrics(keys=raw_keys)

        return result_keys

    async def create_key(self, key_name: str = None) -> OutlineKey:
        """Create a new key"""
        async with self.session.post(url=f"{self.api_url}/access-keys/") as resp:
            if resp.status != 201:
                raise OutlineServerErrorException("Unable to create key")
            key = await resp.json()

            key["used_bytes"] = 0
            key["data_limit"] = None

        outline_key = OutlineKey.from_key_json(key)
        if key_name is not None:
            is_renamed = await self.rename_key(key_id=outline_key.key_id, name=key_name)
            if is_renamed:
                outline_key.name = key_name
        return outline_key

    async def delete_key(self, key_id: int) -> bool:
        """Delete a key"""
        async with self.session.delete(
            url=f"{self.api_url}/access-keys/{key_id}"
        ) as resp:
            return resp.status == 204

    async def rename_key(self, key_id: int, name: str) -> bool:
        """Rename a key"""
        async with self.session.put(
            url=f"{self.api_url}/access-keys/{key_id}/name", data={"name": name}
        ) as resp:
            return resp.status == 204

    async def add_data_limit(self, key_id: int, limit_bytes: int) -> bool:
        """Set data limit for a key (in bytes)"""
        data = {"limit": {"bytes": limit_bytes}}

        async with self.session.put(
            url=f"{self.api_url}/access-keys/{key_id}/data-limit", json=data
        ) as resp:
            return resp.status == 204

    async def delete_data_limit(self, key_id: int) -> bool:
        """Removes data limit for a key"""
        async with self.session.delete(
            url=f"{self.api_url}/access-keys/{key_id}/data-limit"
        ) as resp:
            return resp.status == 204

    async def get_transferred_data(self) -> dict:
        """Gets how much data all keys have used
        {
            "bytesTransferredByUserId": {
                "1":1008040941,
                "2":5958113497,
                "3":752221577
            }
        }"""
        async with self.session.get(url=f"{self.api_url}/metrics/transfer") as resp:
            resp_json = await resp.json()
            if resp.status >= 400 or "bytesTransferredByUserId" not in resp_json:
                raise OutlineServerErrorException("Unable to get metrics")
        return resp_json

    async def get_server_information(self) -> dict:
        """Get information about the server
        {
            "name":"My Server",
            "serverId":"7fda0079-5317-4e5a-bb41-5a431dddae21",
            "metricsEnabled":true,
            "createdTimestampMs":1536613192052,
            "version":"1.0.0",
            "accessKeyDataLimit":{"bytes":8589934592},
            "portForNewAccessKeys":1234,
            "hostnameForAccessKeys":"example.com"
        }
        """
        async with self.session.get(url=f"{self.api_url}/server") as resp:
            resp_json = await resp.json()
            if resp.status != 200:
                raise OutlineServerErrorException(
                    "Unable to get information about the server"
                )
        return resp_json

    async def set_server_name(self, name: str) -> bool:
        """Renames the server"""
        data = {"name": name}
        async with self.session.put(url=f"{self.api_url}/name", json=data) as resp:
            return resp.status == 204

    async def set_hostname(self, hostname: str) -> bool:
        """Changes the hostname for access keys.
        Must be a valid hostname or IP address."""
        data = {"hostname": hostname}
        async with self.session.put(
            url=f"{self.api_url}/server/hostname-for-access-keys", json=data
        ) as resp:
            return resp.status == 204

    async def get_metrics_status(self) -> bool:
        """Returns whether metrics is being shared"""
        async with self.session.get(url=f"{self.api_url}/metrics/enabled") as resp:
            resp_json = await resp.json()
            return resp_json.get("metricsEnabled")

    async def set_metrics_status(self, status: bool) -> bool:
        """Enables or disables sharing of metrics"""
        data = {"metricsEnabled": status}
        async with self.session.put(
            url=f"{self.api_url}/metrics/enabled", json=data
        ) as resp:
            return resp.status == 204

    async def set_port_new_for_access_keys(self, port: int) -> bool:
        """Changes the default port for newly created access keys.
        This can be a port already used for access keys."""
        data = {"port": port}
        async with self.session.put(
            url=f"{self.api_url}/server/port-for-new-access-keys", json=data
        ) as resp:
            if resp.status == 400:
                raise OutlineServerErrorException(
                    "The requested port wasn't an integer from 1 through 65535, or the request had no port parameter."
                )
            elif resp.status == 409:
                raise OutlineServerErrorException(
                    "The requested port was already in use by another service."
                )
            return resp.status == 204

    async def set_data_limit_for_all_keys(self, limit_bytes: int) -> bool:
        """Sets a data transfer limit for all access keys."""
        data = {"limit": {"bytes": limit_bytes}}
        async with self.session.put(
            url=f"{self.api_url}/server/access-key-data-limit", json=data
        ) as resp:
            return resp.status == 204

    async def delete_data_limit_for_all_keys(self) -> bool:
        """Removes the access key data limit, lifting data transfer restrictions on all access keys."""
        async with self.session.delete(
            url=f"{self.api_url}/server/access-key-data-limit"
        ) as resp:
            return resp.status == 204

    async def _close(self):
        await self.session.close()

    def __del__(self):
        if self.session is None:
            return
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            asyncio.run(self._close())
            return
        loop.create_task(self._close())
