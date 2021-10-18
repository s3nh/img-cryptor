import matplotlib.pyplot as plt
import argparse
import os 

from img_cryptor.src.cryptor import Encryptor
from img_cryptor.src.cryptor import Decryptor
from PIL import Image

def main():

    enc = Encryptor(path = 'example/test.png', outname = 'example/enc_test', create = True , _key = 'keys\_keys.bin', _iv = 'keys\_iv.bin')
    enc();
    dec = Decryptor(path = 'example/enc_test', outname = 'example/test_enc.png', create = False, _key = 'keys\_keys.bin', _iv = 'keys\_iv.bin')
    res = dec()
    resimg = Image.fromarray(res)
    resimg.save('example/test_enc.png')

if __name__.__contains__("__main__"):
    main()