import platform

from ctypes import *
#from importlib.resources import files
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
    global isolatethread
    global dll 

    isolatethread = None 
    dll = None

    def __init__(self, name, years):
        self.years = years 
        self.name = name 

        lib_path = files('ilivalidator.lib_ext').joinpath(lib_name)
        print(lib_name)
        print(lib_path)
        # str() seems to be necessary on windows: https://github.com/TimDettmers/bitsandbytes/issues/30
        self.dll = CDLL(str(lib_path))
        isolate = c_void_p()
        self.isolatethread = c_void_p()
        self.dll.graal_create_isolate(None, byref(isolate), byref(self.isolatethread))
        self.dll.ilivalidator.restype = bool

    def getAge(self):
        print("The age of " + self.name +" is "+self.years)

    def validate(self, data_file_name):
        print(data_file_name)
        print( platform.uname()[0] )

        # lib_path = files('lib_ext').joinpath(lib_name)
        # print(lib_name)
        # dll = CDLL(lib_path)
        # isolate = c_void_p()
        # isolatethread = c_void_p()
        # dll.graal_create_isolate(None, byref(isolate), byref(isolatethread))
        # dll.ilivalidator.restype = bool

        result = self.dll.ilivalidator(self.isolatethread, c_char_p(bytes(data_file_name, "utf8")))
        return result

    def load2gpkg(self, data_file_name):
        result = self.dll.ili2gpkg(self.isolatethread, c_char_p(bytes(data_file_name, "utf8")))
        return result
