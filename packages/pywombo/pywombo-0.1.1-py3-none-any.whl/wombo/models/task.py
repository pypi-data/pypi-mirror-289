from typing import List, Optional, Literal, Annotated

from pydantic import BaseModel, Field

from ..types import HttpUrl
from .image import Image


Prompt = Annotated[str, Field(min_length=1, max_length=350)]
TaskId = str


class BaseInputSpec(BaseModel):
    prompt: Prompt
    style: int = 115
    aspect_ratio: str = 'old_vertical_ratio'
    display_freq: int = 10


class InputSpec(BaseInputSpec):
    aspect_ratio_width: int
    aspect_ratio_height: int
    gen_type: Literal['WEEK', 'NORMAL', 'STRONG'] = 'NORMAL'


class Result(BaseModel):
    final: HttpUrl


class Task(BaseModel):
    id: str
    user_id: str
    state: str
    input_spec: InputSpec
    premium: bool
    created_at: str
    updated_at: str
    is_nsfw: bool
    photo_url_list: List[HttpUrl]
    generated_photo_keys: List[str]
    result: Optional[Result] = None

    @property
    def url(self) -> Optional[HttpUrl]:
        return self.result.final if self.result else None

    @property
    def image(self) -> Optional[Image]:
        return Image(self.url) if self.url else None
