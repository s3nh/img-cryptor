from PIL import Image
import imagehash

from ..src.cfg import CFG
from typing import Dict 


def compare_hashes(img_a: Image, img_b: Image) -> bool:
    """Compare hashes of images
    Params
    --------

    img_a: Image to compare.

    img_b: Image to compare.

    Returns
    ---------
    bool: True if the hashes are equal.
    """
    hash_a = imagehash.average_has(img_a)
    hash_b = imagehash.average_has(img_b)
    return hash_a == hash_b

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