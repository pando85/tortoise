import aiohttp

API_URL = "http://127.0.0.1:8000/v1/"


class ExpectedStatusError(Exception):
    pass


class GetTokenError(Exception):
    pass


class MethodNotAllowed(Exception):
    pass


class TortoiseClient(object):
    @classmethod
    async def create(cls, user, password):
        self = TortoiseClient()
        self.token = await self._get_token(user, password)
        return self

    async def _get_token(self, user, password):
        url = 'token/'
        header = {"Content-Type": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.post(
                     API_URL + url,
                    json={'username': user, 'password': password},
                    headers=header) as response:
                if response.status == 200:
                    if 'token' in (await response.json()).keys():
                        token = (await response.json())['token']
                        return token
                raise GetTokenError(await response)

    async def _api_call(
            self, method, url, token, data=None, expected_status=None):
        header = {"Authorization": "Token " + token}
        response = await self._request(method, url, data, header)
        if response.status != expected_status:
            raise ExpectedStatusError(response)
        return await response.json()

    async def _request(self, method, url, data, header):
        if method not in ['get', 'post', 'put']:
            raise MethodNotAllowed(method)
        async with aiohttp.ClientSession() as session:
            curl = getattr(session, method)
            if data:
                header.update({"Content-Type": "application/json"})
                async with curl(
                         API_URL + url, json=data, headers=header) as response:
                    return response
            else:
                async with curl(API_URL + url, headers=header) as response:
                    return response

    async def get_tasks(self):
        return await self._call_tasks('get', 200)

    async def create_task(self, task):
        return await self._call_tasks('post', 201, data=task)

    async def _call_tasks(self, method, expected_status, data=None):
        return await self._api_call(
            method,
            'tasks/',
            self.token,
            data=data,
            expected_status=expected_status)
