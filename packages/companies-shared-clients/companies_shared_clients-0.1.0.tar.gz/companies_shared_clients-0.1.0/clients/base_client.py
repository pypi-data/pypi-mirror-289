import os
from typing import Dict

import aiohttp
from aiohttp import BasicAuth


class APIConsumer:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def make_api_request(
            self,
            method: str,
            path: str,
            params: Dict | None = None,
            json: Dict | None = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=method,
                    url=f'{os.environ.get("COMPANY_HOUSE_API_BASE_URL")}/{path}',
                    params=params,
                    json=json,
                    auth=BasicAuth(self.api_key, ''),
                    ssl=False
            ) as response:
                if response.status == 404:
                    return {'not_found': True}
                elif not response.ok:
                    print(response.reason)
                    return
                result = await response.json()
                return result

    async def make_stream_request(
            self,
            method: str,
            path: str,
            params: Dict | None = None,
            json: Dict | None = None,
    ):
        async with aiohttp.ClientSession() as session:
            async with session.request(
                    method=method,
                    url=f'{os.environ.get("COMPANY_HOUSE_STREAM_BASE_URL")}/{path}',
                    params=params,
                    json=json,
                    auth=BasicAuth(self.api_key, ''),
                    ssl=False
            ) as response:
                if response.status == 404:
                    return {'not_found': True}
                elif not response.ok:
                    print(response.reason)
                    return
                async for line in response.content:
                    print(line.decode())

                result = await response.json()
                return result
