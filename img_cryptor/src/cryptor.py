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
        return Image.open(path)

    def _init_keys(self) -> Union[Rd, Rd]:
        """Initialize key and value instance
        """
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
        _cipher: Any = self.get_cipher(algname = algname)
        return _cipher

    def encrypt(self, file: Image, filesize : Tuple):
        return self.cipher.encrypt(file, filesize)

    def decrypt(self, file: Any):
        return self.cipher.decrypt(file)

    def _np_trans(self, file: Any, filesize: tuple):
        return np.frombuffer(file, dtype = np.uint8).reshape(filesize)


class Cryptor(object):


    def __init__(self, ):
        self.path = path 
        self.outname = outname
        print(kwargs.items())
        if create:
            self._key, self._iv = self.initialize_keys()
        else:
            self._key = read_key(kwargs.get('_key'))
            self._iv = read_key(kwargs.get('_iv'))
        self.cipher = self.create_cipher()

    def read_image(self):
        """Read the image based on path argument

        Params
        ----------
        None

        Returns
        -----------
        in_data: np.array, 

        shape: Tuples
            Shape of processed image.
        """
        in_data = np.asarray( Image.open(self.path) )
        _shape = np.asarray(in_data.shape)
        print(_shape)
        return in_data.tobytes(order = 'C'), _shape.tobytes(order = 'C')

    def read_data(self):
        """
        Read data (crypted or encrypted)
        """
        infile = open(self.path, 'rb')
        data = infile.read()
        infile.close()
        return data

    def write_data(outpath: str, data: Any):
        encfile = open(outpath, 'wb')
        encfile.write(data)
        encfile.close() 

    def initialize_keys(self) -> Union[Rd, Rd]:
        """ Initialize key and initialize vector
        """
        _key = Random.new().read(AES.block_size)
        _iv = Random.new().read(AES.block_size)
        return _key, _iv

    def create_cipher(self, algo : str = 'AES'):
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
        tmp_ciph = getattr(Crypto.Cipher, algo)
        _cipher = tmp_ciph.new(self._key, AES.MODE_CFB, self._iv)
        return _cipher

class Encryptor(Cryptor):
    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create, **kwargs)
        self.data, self.shape = self.read_image()
        self.enc_data = self._encrypt(data = self.data)
        self.enc_shape = self._encrypt(data = self.shape)

    def __call__(self):
        self.save_cryptedata(input_file = self.enc_data, filename = self.outname) 
        self.save_cryptedata(input_file = self.enc_shape, filename = self.outname + '_shape')

    def save_cryptedata(self, input_file: Any, filename: str):
        encfile = open(filename, 'wb')
        encfile.write(input_file)
        encfile.close() 

    def _encrypt(self, data: Union[np.ndarray, Tuple]):
        return self.cipher.encrypt(data) 

class Decryptor(Cryptor):

    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create, **kwargs)

    def __call__(self):
        self.data =  self.load_cryptedata(filename = self.path) 
        self.shape = self.load_cryptedata(filename = self.path + '_shape')
        self.dec_data = self._decrypt(self.data)
        self.dec_numpy  = self._get_numpy()
        self.dec_shape = np.frombuffer(self._decrypt(self.shape), dtype = np.uint8)
        self.save_data(input_file = self.dec_numpy, filename = self.outname)
        print(f"Decrypted file shape :{self.dec_shape}")

    def load_cryptedata(self,filename: Union[str, Path]) -> None:
        infile = open(filename, 'rb')
        data = infile.read()
        infile.close()
        return data

    def _decrypt(self, file: Any):
        return self.cipher.decrypt(file)    

    def save_data(self, input_file: Any, filename: str):
        file = open(filename, 'wb')
        file.write(input_file)
        file.close()

    def _get_numpy(self):
       return np.frombuffer(self.dec_data, dtype = np.uint8).reshape((443, 712, 4))