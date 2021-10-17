import Crypto 
import os 
import re 
import typing 
from src.cfg import CFG
from typing import Dict 


def read_key(path : str)-> None:
    """Read key based on prdefined path.
    Params
    --------
    path: str
        Path to procecessing key file.

    Returns
    --------
    str
    """
    with open(path, 'rb') as keyfile:
        _key = keyfile.read()
    return _key
