import matplotlib.pyplot as plt
import argparse
import os 

from img_cryptor.src.cryptix import Cryptix, CryptixInit 
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
    
    print(crx.key)
    print(crx.value)
    # _img = crx.load_input(path = PATH)
    #print(_img)


if __name__.__contains__("__main__"):
    main()