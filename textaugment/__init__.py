import os
from .translate import Translate
from .word2vec import Word2vec
from .wordnet import Wordnet
from .constants import LANGUAGES

name = "textaugment"

__version__ = '1.0'
__licence__ = 'MIT'
__author__ = 'Joseph Sefara'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

__all__ = [
    'Translate',
    'Word2vec',
    'Wordnet',
    'LANGUAGES'
]
