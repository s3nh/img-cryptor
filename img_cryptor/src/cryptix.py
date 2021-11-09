import Crypto
import numpy as np

from Crypto.Cipher import AES
from Crypto import Random 
from pathlib import Path
from PIL import Image
from typing import Any, TypeVar, Union, Tuple
from ..utils.utils import read_key

Rd = TypeVar('Rd')

# This section should be stored in utils.utils.py
def parse_filepath(path: Tuple[str, Path]) -> Path:
    if not isinstance(path, Path):
        #ffs
        path = Path(path)

    return filepath

def rename_filepath(path: Tuple[str, Path]) -> Path:
    raise NotImplementedError

def load_object(path: str):
    """
    Load any object based on its filepath.

    Params
    ----------
    path: str
        Path for provided file. 

    Returns
    ----------
    data: Any
        data stored in loaded files.
    """
    _file = open(path, 'rb')
    data = _file.read()
    _file.close()
    return data

def write_object(data: Any, path: Union[Path, str]):
    """
    Save any object. 

    Params 
    ----------

    data: Any
        Data to save properly.

    path: Union[Path, str]
        Place in which file will be exported.

    """
    outfile = open(path, 'wb')
    outfile.write(data)
    outfile.close()

class CFG:
    """
    Configuration file which consist every
    information needed to properly perform encryption or decryption,
    depends of individual needs.
    """

    key_outpath: str = 'outpath/key.bin'
    value_outpath: str = 'outpath/value.bin'

class CryptixInit(object):

    def __init__(self, create: bool, algname: str = 'AES'):
        self.config = CFG()
        self.create = create
        self.algname = algname

    def get_config(self):
        return dir(self.config)

    def __call__(self):
        _key, _value = self._init_keys()
        write_object(_key, CFG.key_outpath)
        write_object(_value, CFG.value_outpath)

    def _init_keys(self) -> Union[Rd, Rd]:
        _key = Random.new().read(AES.block_size)
        _iv = Random.new().read(AES.block_size)
        return _key, _iv

class Cryptix(object):

    def __init__(self, algname: str = 'AES'):
        self.cipher = self.create_cipher(algname = algname)

    def __call__(self, path: str):
        input = self.load_input(path = path)
     
    def load_input(self, path: Union[Path, str]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Load input image based on its filepath,.

        Params 
        ----------

        path: Union[Path, str]
            Path in which file is stored. 

        Returns
        ----------
        Tuple[np.ndarray, np.ndarray]
            Tuple which consist information about the image and its size. 
        """
        _img = Image.open(path)
        print(_img.size)
        _imsize = np.array((_img.size[0], _img.size[1]))
        return np.array(_img).tobytes(order = 'C'), _imsize.tobytes(order = 'C')

    def get_cipher(self, algname: str = 'AES'):
        """Load specific algorithm from Crypto, 
            based on its name.
        """
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
        self.key = load_object(CFG.key_outpath)
        self.value = load_object(CFG.value_outpath)
        attr_cipher: Any = self.get_cipher(algname = algname)
        _cipher = attr_cipher.new(self.key, AES.MODE_CFB, self.value)
        return _cipher

    def encrypt(self, filepath: str):
        _input, _input_size = self.load_input(path = filepath)
        self.encr_input  = self.cipher.encrypt(_input)  
        self.encr_input_size = self.cipher.encrypt(_input_size)
        return self.encr_input, self.encr_input_size

    def decrypt(self, file: Any):
        return self.cipher.decrypt(file)

    def _np_trans(self, file: Any, filesize: tuple):
        return np.frombuffer(file, dtype = np.uint8).reshape(filesize)