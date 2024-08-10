from typing import Union, Dict, Sequence

from proxystr import Proxy
from pydantic_core import ValidationError

from .styles import Styles
from .session import Client, AsyncClient
from ..models import Prompt, BaseInputSpec, ArtStyle, TaskId, Task
from ..exceptions import CreateTaskError


class BaseDream:
    AUTH_URL = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp'
    HOST = 'https://dream.ai'
    DRAW_URL = 'https://paint.api.wombo.ai/api/v2/tasks'

    BASE_HEADERS = {
        "accept": "*/*",
        "accept-language": "ru,en;q=0.9",
        "origin": "https://dream.ai",
        "referer": "https://dream.ai/",
        'priority': 'u=1, i',
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    }

    _FLOW_HEADERS = {
        "authority": "paint.api.wombo.ai",
        "authorization": "bearer {auth_token}",
        "x-app-version": "WEB-2.0.0",
    }

    AUTH_HEADERS = {
        "authority": "identitytoolkit.googleapis.com",
        "x-client-version": "Chrome/JsCore/9.1.2/FirebaseCore-web",
    }

    def __init__(
        self,
        client: Union[Client, AsyncClient],
        proxy: Union[Proxy, str] = None,
        max_requests_per_token: int = 30
    ):
        self.client = client
        self.client.headers.update(self.BASE_HEADERS)
        self.proxy = Proxy(proxy) if proxy else None
        self.styles = Styles(proxy)

        self._max_requests_per_token = max_requests_per_token
        self._counter_calls_auth = 0
        self._auth_token = None

    @property
    def FLOW_HEADERS(self):
        headers = self._FLOW_HEADERS.copy()
        headers['authorization'] = headers['authorization'].format(auth_token=self._auth_token)
        return headers

    def _prepare_spec(self, prompt: Prompt, style: Union[ArtStyle, int] = None) -> Dict:
        if isinstance(prompt, str):
            if not (0 < len(prompt) <= 350):
                raise CreateTaskError('Prompt length must be from 1 to 350 symbols')

        if not style:
            style = self.styles.random()
        if isinstance(style, ArtStyle):
            style = style.id
        style = self.styles.validate_style(style)

        try:
            return BaseInputSpec(prompt=prompt, style=style).model_dump()
        except ValidationError as e:
            raise CreateTaskError('Wrong "prompt" or "style" argument') from e

    @staticmethod
    def _get_ids_from_tasks(tasks: Union[Sequence[Union[Task, TaskId]], Union[Task, TaskId]]):
        if not isinstance(tasks, Sequence):
            tasks = [tasks]
        return [t.id if isinstance(t, Task) else t for t in tasks]
