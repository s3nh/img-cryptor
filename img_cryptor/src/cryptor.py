import Crypto
import numpy as np 

from Crypto.Cipher import AES
from Crypto import Random 
from typing import Union 
from pathlib import Path
from PIL import Image
from typing import TypeVar
from ..utils.utils import read_key

Rd = TypeVar('Rd')

class Cryptor(object):

    def __init__(self, path : str, outname : str , create: bool = True, **kwargs):
        self.path = path 
        self.outname = outname
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
        print(in_data.shape)
        return in_data.tobytes(order = 'C')

    def read_data(self):
        """
        Read data (crypted or encrypted)
        """
        infile = open(self.path, 'rb')
        data = infile.read()
        infile.close()
        return data

    def write_data(self):
        encfile = open(self.outname, 'wb')
        encfile.write(self.enc_data)
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
        super().__init__(path, outname, create)
        self.data = self.read_image()
        self.enc_data = self._encrypt()

    def __call__(self):
        self.write_data()

    def _encrypt(self):
        return self.cipher.encrypt(self.data) 

class Decryptor(Cryptor):

    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create)
        self.data = self.read_data() 
        self.dec_data = self._decrypt()

    def __call__(self):
        return self._get_numpy()

    def _decrypt(self):
        return self.cipher.decrypt(self.data)    

    def _get_numpy(self):
       return np.frombuffer(self.dec_data, dtype = np.uint8).reshape(443, 712, 4)