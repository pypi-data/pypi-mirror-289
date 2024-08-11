from time import sleep
from typing import Union, List, Sequence
import re

from proxystr import Proxy

from ..base_client import BaseDream, Client
from ..models import Task, Prompt, ArtStyle, TaskId
from ..exceptions import CreateTaskError, CheckTaskError, AuthenticationError, GenerationTimeoutError


class Dream(BaseDream):
    def __init__(self, proxy: Union[Proxy, str] = None, max_requests_per_token: int = 30):
        super().__init__(Client(proxy), proxy, max_requests_per_token)

    def check_task(self, task: Union[Task, TaskId]) -> Task:
        try:
            if isinstance(task, Task):
                task_id = task.id
            else:
                task_id = task

            url = f"{self.DRAW_URL}/{task_id}"
            r = self.client.get(url, headers=self.FLOW_HEADERS, timeout=10)
            return Task(**r.json())
        except Exception as e:
            raise CheckTaskError(task_id) from e

    def create_task(self, prompt: Prompt, style: Union[ArtStyle, int] = None) -> Task:
        """if style is None it will be a random style from top styles"""

        self._get_auth_token()
        json_ = {
            "is_premium": False,
            "input_spec": self._prepare_spec(prompt, style)

        }
        try:
            r = self.client.post(url=self.DRAW_URL, headers=self.FLOW_HEADERS, json=json_, timeout=20)
            task = r.json()
        except Exception as e:
            raise CreateTaskError('Create task request failed') from e
        if task['is_nsfw']:
            raise CreateTaskError('Forbidden content requested')
        try:
            return Task(**r.json())
        except Exception as e:
            raise CreateTaskError() from e

    def await_tasks(
        self,
        tasks: Union[Sequence[Union[Task, TaskId]], Union[Task, TaskId]],
        timeout: int = 60,
        check_for: int = 3
    ) -> List[Task]:
        ids = self._get_ids_from_tasks(tasks)
        ready_tasks = []
        for _ in range(timeout, 0, -check_for):
            for task_id in ids:
                sleep(0.1)
                task = self.check_task(task_id)
                if task.url:
                    ready_tasks.append(task)
                    ids.remove(task_id)
                else:
                    break
            if not ids:
                return ready_tasks
            sleep(check_for)
        else:
            raise GenerationTimeoutError(f"No result after {timeout} seconds")

    def as_complited(
        self,
        tasks: Union[Sequence[Union[Task, TaskId]], Union[Task, TaskId]],
        timeout: int = 60,
        check_for: int = 3
    ):
        ids = self._get_ids_from_tasks(tasks)
        for _ in range(timeout, 0, -check_for):
            for task_id in ids:
                sleep(0.1)
                task = self.check_task(task_id)
                if task.url:
                    ids.remove(task_id)
                    yield task
            if not ids:
                break
            sleep(check_for)
        else:
            raise GenerationTimeoutError(f"No result after {timeout} seconds")

    def generate(
        self,
        prompt: Prompt,
        style: Union[ArtStyle, int] = None,
        timeout: int = 60,
        check_for: int = 3,
    ) -> Task:
        """if style is None it will be a random style from top styles"""

        task = self.create_task(prompt, style)
        return self.await_tasks(task)[0]

    def _get_js_filename(self) -> str:
        response = self.client.get(f"{self.HOST}/create")
        js_filename = re.findall(r"_app-(\w+)", response.text)
        return js_filename[0]

    def _get_google_key(self) -> str:
        js_filename = self._get_js_filename()

        url = f"{self.HOST}/_next/static/chunks/pages/_app-{js_filename}.js"
        response = self.client.get(url)

        key = re.findall(r'"(AI\w+)"', response.text)
        return key[0]

    def _get_auth_token(self) -> str:
        if self._counter_calls_auth < self._max_requests_per_token and self._auth_token:
            self._counter_calls_auth += 1
            return self._auth_token

        try:
            response = self.client.post(
                self.AUTH_URL,
                headers=self.AUTH_HEADERS,
                params={"key": self._get_google_key()},
                json={"returnSecureToken": True},
                timeout=20,
            )
            self._auth_token = response.json()["idToken"]
        except Exception as e:
            raise AuthenticationError('Cannot get _auth_token') from e
        self._counter_calls_auth = 0
        return self._auth_token

    def __enter__(self):
        self.client.__enter__()
        return self

    def __exit__(self, *args):
        self.client.__exit__(*args)

    def close(self):
        self.client.close()
