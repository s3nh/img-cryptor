import matplotlib.pyplot as plt
import argparse
import os 

from img_cryptor.src.cryptix import Cryptix, CryptixInit 
from img_cryptor.src.cryptix import load_object, write_object
from PIL import Image

def main():
    os.makedirs('outpath', exist_ok = True)
    PATH: str = 'example/test.png'
    crx_init = CryptixInit(create = True, algname = 'AES')
    crx_init()
    crx_init.get_config()

    crx = Cryptix(algname = 'AES')
    print(crx.cipher)
    #We have that fucnking cyphers  and now just wanted to create
    # How to initialize 
    ENCR_FILEPATH: str = 'example/test.png'
    _encrypted_file, _encrypted_size = crx.encrypt(filepath = ENCR_FILEPATH)
    write_object(_encrypted_file, path = 'example/encrypted_file.bin')
    write_object(_encrypted_size, path = 'example/encrypted_size.bin')

if __name__.__contains__("__main__"):
    main()