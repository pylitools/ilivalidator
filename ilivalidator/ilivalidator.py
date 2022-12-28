import platform
import json

from ctypes import *
from importlib_resources import files

if platform.uname()[0] == "Windows":
    lib_name = "libilivalidator.dll"
elif platform.uname()[0] == "Linux":
    lib_name = "libilivalidator.so"
else:
    lib_name = "libilivalidator.dylib"

class Ilivalidator:
    SETTING_ILIDIRS = "org.interlis2.validator.ilidirs"
    SETTING_MODELNAMES = "org.interlis2.validator.modelNames"
    SETTING_ALL_OBJECTS_ACCESSIBLE = "org.interlis2.validator.allobjectsaccessible"
    SETTING_LOGFILE = "org.interlis2.validator.log"
    SETTING_LOGFILE_TIMESTAMP = "org.interlis2.validator.log.timestamp"
    SETTING_XTFLOG = "org.interlis2.validator.xtflog"

    @staticmethod
    def validate(data_file_names: list, settings: dict=None) -> bool:
        lib_path = files('ilivalidator.lib_ext').joinpath(lib_name)
        # str() seems to be necessary on windows: https://github.com/TimDettmers/bitsandbytes/issues/30
        dll = CDLL(str(lib_path))
        isolate = c_void_p()
        isolatethread = c_void_p()
        dll.graal_create_isolate(None, byref(isolate), byref(isolatethread))
        dll.ilivalidator.restype = bool

        data_file_names_string = ';'.join(data_file_names)

        if settings is None:
            settings = {}       
        settings_string = json.dumps(settings)

        result = dll.ilivalidator(isolatethread, c_char_p(bytes(data_file_names_string, "utf8")), c_char_p(bytes(settings_string, "utf8")))
        return result
