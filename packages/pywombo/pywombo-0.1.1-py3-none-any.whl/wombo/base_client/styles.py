from typing import List, Union
import json
import re
import random

from proxystr import Proxy

from ..utils import tcached, Singleton
from ..exceptions import GetStylesError
from ..models.style import StyleModel, ArtStyle
from .session import Client


class Styles(metaclass=Singleton):
    STYLES_URL = "https://dream.ai/create"
    DEFAULT_STYLE = 115

    def __init__(self, proxy: Union[Proxy, str] = None):
        self.client = Client(proxy)
        self._style_ids = None

    @property
    def free(self) -> List[ArtStyle]:
        return [s for s in self.all if not s.is_premium]

    @property
    def premium(self) -> List[ArtStyle]:
        return [s for s in self.all if s.is_premium]

    @property
    @tcached(3600)
    def top(self):
        top = {}
        for s in self.free:
            if s.model_type == 'diffusion':
                if s.clear_name not in top or s.version > top[s.clear_name].version:
                    top[s.clear_name] = s
        return sorted(top.values(), key=lambda x: x.created_at, reverse=True)

    def random(self, from_top: bool = True):
        styles = self.top if from_top else self.free
        return random.choice(styles)

    @property
    @tcached(3600)
    def all(self) -> List[ArtStyle]:
        try:
            res = self.client.get(self.STYLES_URL)
            style_model = StyleModel(**self._get_json_from_html(res.text))
            return self._extend_styles(style_model.pageProps.artStyles)
        except Exception as e:
            raise GetStylesError('Cannot get styles from https://dream.ai/create') from e

    @staticmethod
    def _get_json_from_html(text: str):
        start_text = '<script id="__NEXT_DATA__" type="application/json">'
        s = text.find(start_text)
        text = text[s + len(start_text):]
        text = text[:text.find('</script>')]
        return json.loads(text)['props']

    def _extend_styles(self, styles: List[ArtStyle]) -> List[ArtStyle]:
        for s in styles:
            s.clear_name = s.name.split(' v')[0].strip()
            if r := re.search(r' v\d+\.?\d*', s.name):
                s.version = float(r[0][2:])
            else:
                s.version = 0.0
        return styles

    @property
    @tcached(3600)
    def style_ids(self) -> List[int]:
        if not self._style_ids:
            self._style_ids = sorted([s.id for s in self.all])
        return self._style_ids

    def validate_style(self, style_id: int) -> int:
        if style_id not in self.style_ids:
            raise ValueError(f"Style_id {style_id} not allowed")
        return style_id
