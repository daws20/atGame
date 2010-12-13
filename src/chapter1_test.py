from ctypes import *
from ctypes.util import find_library

cglib = cdll.LoadLibrary(find_library('ApplicationServices '))
