import matplotlib.pyplot as plt
import argparse
import os 

from img_cryptor.src.cryptix import Cryptix 
from PIL import Image

def main():

    PATH: str = 'example/test.png'
    crx = Cryptix(create= True, algname = 'AES')
    print(crx)
    _img = crx.load_input(path = PATH)
    print(_img)


if __name__.__contains__("__main__"):
    main()