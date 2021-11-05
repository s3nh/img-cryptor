import Crypto
import numpy as np

from Crypto.Cipher import AES
from Crypto import Random 
from pathlib import Path
from PIL import Image
from typing import Any, TypeVar, Union, Tuple
from ..utils.utils import read_key

Rd = TypeVar('Rd')

class Cryptix(object):

    def __init__(self, create: bool, algname: str = 'AES'):
        self.create = create
        self.cipher = self.create_cipher(algname = algname)

    def __call__(self):
        if self.create:
            _key, _v = self._init_keys()

    def load_input(self, path: str):
        _img = Image.open(path)
        _imsize = _img.size
        return np.array(_img), _imsize

    def _init_keys(self) -> Union[Rd, Rd]:
        _key = Random.new().read(AES.block_size)
        _iv = Random.new().read(AES.block_size)
        return _key, _iv

    def get_cipher(self, algname: str = 'AES'):
        return getattr(Crypto.Cipher, algname)

    def create_cipher(self, algname : str = 'AES'):
        """Create new cipher
           with predefined algorithm name.

        Params
        ----------

        algo: str
            Algorithm name (#TODO list it)

        Returns
        ----------
        _cipher: Any
        """
        attr_cipher: Any = self.get_cipher(algname = algname)
        _cipher = attr_cipher.new(self._key, AES.MODE_CFB, self._iv)
        return _cipher

    def encrypt(self, file: np.ndarray, filesize : Tuple):
        return self.cipher.encrypt(file, filesize)

    def decrypt(self, file: Any):
        return self.cipher.decrypt(file)

    def _np_trans(self, file: Any, filesize: tuple):
        return np.frombuffer(file, dtype = np.uint8).reshape(filesize)