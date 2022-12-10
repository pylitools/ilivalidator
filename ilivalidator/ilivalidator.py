import platform

from ctypes import *
from importlib_resources import files

if platform.uname()[0] == "Windows":
    lib_name = "libilivalidator.dll"
elif platform.uname()[0] == "Linux":
    lib_name = "libilivalidator.so"
else:
    lib_name = "libilivalidator.dylib"

def quicktext():
    print('Hello, welcome to QuickFoo package.')

class Ilivalidator:                     
    #global isolatethread
    #global dll 

    #isolatethread = None 
    #dll = None

    def validate(data_file_name):
        lib_path = files('ilivalidator.lib_ext').joinpath(lib_name)
        # str() seems to be necessary on windows: https://github.com/TimDettmers/bitsandbytes/issues/30
        dll = CDLL(str(lib_path))
        isolate = c_void_p()
        isolatethread = c_void_p()
        dll.graal_create_isolate(None, byref(isolate), byref(isolatethread))
        dll.ilivalidator.restype = bool

        result = dll.ilivalidator(isolatethread, c_char_p(bytes(data_file_name, "utf8")))
        return result

Ilivalidator.validate = staticmethod(Ilivalidator.validate)
