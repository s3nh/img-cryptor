import argparse
import os 
from img_cryptor.src.cryptor import Cryptor, Encryptor 
from img_cryptor.utils.utils import read_key
from typing import List, Dict, Union, Optional 

def main():

    cr = Cryptor(path = 'example/test.png', outname = 'example/enc_test', create = True)
    enc = Encryptor(path = 'example/test.png', outname = 'example/enc_test', create = True)
    print(cr)
    print(enc)
    enc();

if __name__.__contains__("__main__"):
    main()