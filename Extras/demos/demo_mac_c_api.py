import ctypes



DYLIB_DIR = "/Users/natalieh/Downloads/libSBML-5.17.0-Source/install_mac/lib/"

DYLIB_FILE = DYLIB_DIR + "libsbml.5.17.0.dylib"

slib = ctypes.CDLL(DYLIB_FILE)

print("dylib file: ", DYLIB_FILE)
print("slib: ", type(slib), dir(slib))

slib.readSBMLFromFile.argtypes = [ctypes.c_char_p]
slib.readSBMLFromFile.restype = ctypes.c_uint64

doc = slib.readSBMLFromFile("model_simple_out.xml".encode('utf-8'))

slib.SBMLDocument_getLevel.argtypes = [ctypes.c_uint64]
slib.SBMLDocument_getLevel.restype = ctypes.c_uint

print("doc level: ", slib.SBMLDocument_getLevel(doc))


f = open("model_simple_out.xml", "r")

if f.mode == "r":
    contents = f.read()

print("file contents: ", type(contents), len(contents))


