import matplotlib.pyplot as plt
from img_cryptor.src.cryptix import CryptixInit, Cryptix
from img_cryptor.src.cryptix import load_object, write_object
import numpy as np
from PIL import Image

def main():


    crx = Cryptix(algname = 'AES')
    print(crx) 
    ENCR_FILEPATH: str = 'example/encrypted_file.bin'
    ENCR_SHAPEPATH: str = 'example/encrypted_size.bin'
    encr = load_object(ENCR_FILEPATH)
    encr_shape = load_object(ENCR_SHAPEPATH)

    _shape = crx.decrypt(encr_shape)
    print(_shape)
    _image = crx.decrypt(encr)
    print(np.frombuffer(_image, dtype = np.uint8))    
    print(np.frombuffer(_shape, dtype = np.uint8))

if __name__ == '__main__':
    main()