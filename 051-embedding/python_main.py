from ctypes import *

class Profile(Structure):
    _fields_ = [("fname", c_char_p), ("sname", c_char_p), ("age", c_int)]

lib_dll = cdll.LoadLibrary("c_dll.dll")
lib_dll.SetProfile.argtypes  = [POINTER(Passport)]

lib_dll.ShowProfile()

lib_dll.SetFName(c_char_p(b"Cyrus"))
lib_dll.SetSName(c_char_p(b"Smith"))

lib_dll.ShowProfile()

profile = Profile("fname", "sname", 10)

lib_dll.SetProfile(pointer(passport))

lib_dll.ShowProfile()