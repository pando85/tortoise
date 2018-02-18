import aiohttp
import logging

from tortoisecli.errors import (GetTokenError, ExpectedStatusError)


METHODS = {"create": "post", "get": "get", "edit": "patch", "delete": "delete"}


class TortoiseClient(object):
    def __init__(self, url):
        self.api_url = url

    @classmethod
    async def create(cls, url, user, password):
        self = TortoiseClient(url)
        self.token = await self._get_token(user, password)
        return self

    @classmethod
    def create_with_token(cls, url, token):
        self = TortoiseClient(url)
        self.token = token
        return self

    async def _get_token(self, user, password):
        url = 'token/'
        header = {"Content-Type": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                     self.api_url + url,
                    json={'username': user, 'password': password},
                    headers=header) as response:
                if response.status == 200:
                    if 'token' in (await response.json()).keys():
                        token = (await response.json())['token']
                        return token
                raise GetTokenError(await response.json())

    async def api_call(self, command, resource, data=None):
        url = resource + "s/"
        #if command in ["edit", "delete"]:
        #    url += self._get_id(url)
        return await self._api_call(METHODS[command], url,
                                    data, expected_status=[200, 201])

    async def _api_call(
            self, method, url, data=None, expected_status=None):
        header = {}
        if self.token:
            header = {"Authorization": "Token " + self.token}
        response = await self._request(method, url, data, header)
        if response.status not in expected_status:
            raise ExpectedStatusError(await response.json())
        return await response.json()

    async def _request(self, method, url, data, header):
        logging.debug("Method: %s, url: %s, data: %s, header: %s",
                      method, url, data, header)
        async with aiohttp.ClientSession() as session:
            curl = getattr(session, method)
            if data:
                header.update({"Content-Type": "application/json"})
                async with curl(self.api_url + url, json=data,
                                headers=header) as response:
                    return response
            else:
                async with curl(
                        self.api_url + url, headers=header) as response:
                    return response
