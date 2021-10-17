import pathlib

from Crypto.Cipher import AES
from Crypto import Random 
from typing import List, Union, Dict, Optional 
from pathlib import Path
from PIL import Image
import numpy as np 

class Cryptor():

    def __init__(self, path : str, outname : str , create: bool = True):
        self.path = path 
        self.outname = outname
        if create:
            self._key, self._iv = self._init_keyiv()
        else:
            self._key = kwargs.get('_key')
            self._iv = kwargs.get('_iv')
       
        self.cipher = self._crt_cipher()

    def _read_image(self):
        """Read the image based on path argument

        Params
        ----------
        None

        Returns
        -----------

        in_data: np.array



        """
        in_data = np.asarray( Image.open(self.path) )
        return in_data

    def _read_data(self):
        """
        Read data (crypted or encrypted)
        """
        infile = open(self.path, 'rb')
        data = infile.read()
        infile.close()
        return data

    def _init_keyiv(self):
        """ Initialize key and initialize vector
        """
        _key = Random.new().read(AES.block_size)
        _iv = Random.new().read(AES.block_size)
        return _key, _iv

    def _crt_cipher(self, algo : str = 'AES'):
        _cipher = AES.new(self._key, AES.MODE_CFB, self._iv)
        return _cipher

class Encryptor(Cryptor):
    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create, **kwargs)
        self.data = self._read_image()
        self.enc_data = self._encrypt()

    def _encrypt(self):
        return self.cipher.encrypt(self.data) 

    def _write_data(self):
        encfile = open(self.outname, 'wb')
        encfile.write(self.enc_data)
        encfile.close() 

class Decryptor(Cryptor):

    def __init__(self, path, outname, create, **kwargs):
        super().__init__(path, outname, create, **kwargs)
        self.data = self._read_data() 
        self.dec_data = self._decrypt()

    def _decrypt(self):
        return self.cipher.decrypt(self.data)    
    

    def _write_data(self):
        encfile = open(self.outname, 'wb')
        encfile.write(self.dec_data)
        encfile.close() 

    def _get_numpy(self):
       return np.frombuffer(self.dec_data, dtype = np.uint8).reshape(kwargs.get('size'))
    
    
