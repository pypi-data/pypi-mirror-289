from typing import Union, List, Sequence
import re
import asyncio

from proxystr import Proxy

from ..base_client import BaseDream, AsyncClient
from ..models import Task, Prompt, ArtStyle, TaskId
from ..exceptions import CreateTaskError, CheckTaskError, AuthenticationError, GenerationTimeoutError


class AsyncDream(BaseDream):
    def __init__(self, proxy: Union[Proxy, str] = None, max_requests_per_token: int = 30):
        super().__init__(AsyncClient(proxy), proxy, max_requests_per_token)

    async def check_task(self, task: Union[Task, TaskId]) -> Task:
        try:
            if isinstance(task, Task):
                task_id = task.id
            else:
                task_id = task

            url = f"{self.DRAW_URL}/{task_id}"
            r = await self.client.get(url, headers=self.FLOW_HEADERS, timeout=10)
            return Task(**r.json())
        except Exception as e:
            raise CheckTaskError(task_id) from e

    async def create_task(self, prompt: Prompt, style: Union[ArtStyle, int] = None) -> Task:
        """if style is None it will be a random style from top styles"""

        await self._get_auth_token()
        json_ = {
            "is_premium": False,
            "input_spec": self._prepare_spec(prompt, style)

        }
        try:
            r = await self.client.post(url=self.DRAW_URL, headers=self.FLOW_HEADERS, json=json_, timeout=20)
            task = r.json()
        except Exception as e:
            raise CreateTaskError('Create task request failed') from e
        if task['is_nsfw']:
            raise CreateTaskError('Forbidden content requested')
        try:
            return Task(**r.json())
        except Exception as e:
            raise CreateTaskError() from e

    async def await_tasks(
        self,
        tasks: Union[Sequence[Union[Task, TaskId]], Union[Task, TaskId]],
        timeout: int = 60,
        check_for: int = 3
    ) -> List[Task]:
        ids = self._get_ids_from_tasks(tasks)
        ready_tasks = []
        for _ in range(timeout, 0, -check_for):
            for task_id in ids:
                await asyncio.sleep(0.1)
                task = await self.check_task(task_id)
                if task.url:
                    ready_tasks.append(task)
                    ids.remove(task_id)
                else:
                    break
            if not ids:
                return ready_tasks
            await asyncio.sleep(check_for)
        else:
            raise GenerationTimeoutError(f"No result after {timeout} seconds")

    async def as_complited(
        self,
        tasks: Union[Sequence[Union[Task, TaskId]], Union[Task, TaskId]],
        timeout: int = 60,
        check_for: int = 3
    ):
        ids = self._get_ids_from_tasks(tasks)
        for _ in range(timeout, 0, -check_for):
            for task_id in ids:
                await asyncio.sleep(0.1)
                task = await self.check_task(task_id)
                if task.url:
                    ids.remove(task_id)
                    yield task
            if not ids:
                break
            await asyncio.sleep(check_for)
        else:
            raise GenerationTimeoutError(f"No result after {timeout} seconds")

    async def generate(
        self,
        prompt: Prompt,
        style: Union[ArtStyle, int] = None,
        timeout: int = 60,
        check_for: int = 3,
    ) -> Task:
        """if style is None it will be a random style from top styles"""

        task = await self.create_task(prompt, style)
        return (await self.await_tasks(task))[0]

    async def _get_js_filename(self) -> str:
        response = await self.client.get(f"{self.HOST}/create")
        js_filename = re.findall(r"_app-(\w+)", response.text)
        return js_filename[0]

    async def _get_google_key(self) -> str:
        js_filename = await self._get_js_filename()

        url = f"{self.HOST}/_next/static/chunks/pages/_app-{js_filename}.js"
        response = await self.client.get(url)

        key = re.findall(r'"(AI\w+)"', response.text)
        return key[0]

    async def _get_auth_token(self) -> str:
        if self._counter_calls_auth < self._max_requests_per_token and self._auth_token:
            self._counter_calls_auth += 1
            return self._auth_token

        try:
            response = await self.client.post(
                self.AUTH_URL,
                headers=self.AUTH_HEADERS,
                params={"key": await self._get_google_key()},
                json={"returnSecureToken": True},
                timeout=20,
            )
            self._auth_token = response.json()["idToken"]
        except Exception as e:
            raise AuthenticationError('Cannot get _auth_token') from e
        self._counter_calls_auth = 0
        return self._auth_token

    async def __aenter__(self):
        await self.client.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self.client.__aexit__(*args)

    async def aclose(self):
        await self.client.aclose()

    async def close(self):
        await self.aclose()
