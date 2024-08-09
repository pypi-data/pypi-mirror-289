import httpx


class HttpxClient:
    def __init__(self):
        self._client = httpx.AsyncClient()

    async def close(self):
        await self._client.aclose()


class AioHttpClient:
    def __init__(self):
        self._client = httpx.AsyncClient()

    async def close(self):
        await self._client.aclose()


class RequestsClient:
    def close(self):
        pass
