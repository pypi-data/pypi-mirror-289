import httpx
from io import BytesIO

from ..types import HttpUrl
from ..utils import check_and_create_path, get_next_filename


class Image:
    """
    Make shure you have installed pillow
    to use Image.image and Image.show()

    `pip install pillow`
    """
    _Image = None

    def __init__(self, url: HttpUrl):
        self.url = url
        self._image = None
        self._bytes = None

    @property
    def image(self):
        self._check_pillow()
        if not self._image:
            self._image = self._Image.open(BytesIO(self.download()))
        return self._image

    def show(self):
        self.image.show()

    def save(self, prefix: str = 'img', folder: str = 'images'):
        path = check_and_create_path(folder)
        filename = get_next_filename(path, prefix + '_', '.jpg')
        with open(f"{path}{filename}", 'wb') as file:
            file.write(self.download())

    def download(self) -> bytes:
        if not self._bytes:
            self._bytes = httpx.get(self.url).content
        return self._bytes

    @classmethod
    def _check_pillow(cls):
        if not cls._Image:
            try:
                from PIL import Image as PImage
                cls._Image = PImage
            except ImportError:
                raise ImportError("The 'pillow' package is required to use this method. Please install it using `pip install pillow`.")
