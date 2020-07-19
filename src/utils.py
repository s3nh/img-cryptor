import Crypto 
import os 
import re 
import typing 
from typing import Dict 


def read_key(path : str)-> None:
    with open(path, 'rb') as keyfile:
        _key = keyfile.read()
    return _key


def read_config(path : str =  'config/config.yaml')-> Dict:
    assert os.path.exists(path), 'Provided path does not exist'
    with open(path, 'r') as confile:
        config = yaml.safe_load(confile)
    return config


def main():
    pass

if __name__ == "__main__":
    main()
