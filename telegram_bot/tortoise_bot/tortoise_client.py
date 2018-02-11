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
                raise GetTokenError(response)

    async def _api_call(
            self, method, url, data=None, expected_status=None):
        header = {"Authorization": "Token " + self.token}
        response = await self._request(method, url, data, header)
        if response.status not in expected_status:
            raise ExpectedStatusError(response)
        return response

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

    async def get_tasks(self, _filter=None):
        if not _filter:
            _filter = ''
        response = await self._api_call(
            'get', 'tasks/?' + _filter, expected_status=[200])
        return await response.json()

    async def create_task(self, task):
        return await self._api_call(
            'post',
            'tasks/',
            expected_status=[201, 400],
            data=task)

    async def get_tags(self):
        response = await self._api_call('get', 'tags/', expected_status=[200])
        return await response.json()

    async def create_tag(self, tag):
        return await self._api_call(
            'post',
            'tags/',
            expected_status=[201, 400],
            data=tag)
