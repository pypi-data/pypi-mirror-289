import ctypes
cranddll = ctypes.CDLL('./crand.dll')

def csrand(seed):
    cranddll.csrand(seed)

def crand():
    return cranddll.crand()
def crandhelp():
    return cranddll.help()