from os import getcwd
from sys import stdin
from platform import node

__version__ = '0.1.0'

CWD = getcwd()
HOSTNAME = node()
IS_TTY = stdin.isatty()
