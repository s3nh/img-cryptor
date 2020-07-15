from Crypto.Cipher import AES
from Crypto import Random 
import typing
from typing import List, Union, Dict 


class Cryptor(object):

    def __init__(self, path : str, outname : str , create : bool, **kwargs) -> None:
        super().__init__(path)
        self.path = path 
        self.outname = outname
        if create:
            self._key, self._iv = self._init_keyiv()
        else:
            self._key = kwargs.get('_key')
            self._iv = kwargs.get('_iv')
       
       self.cipher = self._crt_cipher()

    def _read_data(self):
        infile = open(self.path, 'b')
        data = infile.read()
        infile.close()
        return data

    def _init_keyiv(self):
        _key = Random.new().read(AES.block_size)
        _iv = Random.new().read(AES.block_size)
        return _key, _iv

    def _write_data(self):
        encfile = open(self.outname, 'w')
        enc_file.write(self.enc_data)
        encfile.close() 

    def _crt_cipher(self, algo : str = 'AES'):
        _cipher = AES.new(self._key, AES.MODE_CFB, self._iv)
        return _cipher



class Encryptor(Cryptor):
    def __init__():
        super().__init__(path)
        

    def _encrypt(self)
        pass


class Decryptor(Cryptor):

    def __init__():
        super().__init__(path)


    def _decrypt(self):

        pass




