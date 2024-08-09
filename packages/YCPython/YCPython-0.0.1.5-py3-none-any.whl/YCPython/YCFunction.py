import sys

def Hello():
    print('called YCPython.YCFunction.Hello()', __name__)

import inspect
def Message(_msg):
    print(f"{inspect.stack()[1][1]}:{inspect.currentframe().f_back.f_lineno} ", _msg)

def ErrorMessage(_msg):
    sys.stderr.write(f"ERROR: {inspect.stack()[1][1]}:{inspect.currentframe().f_back.f_lineno} " +  _msg + '\n')

import ctypes
def ListToArray(_li):
    iList = [x for x in _li if isinstance(x, int)]
    fList = [x for x in _li if isinstance(x, float)]
    if len(_li) == len(iList):
        arr = (ctypes.c_int * len(_li))(*_li)
        return arr
    elif len(_li) == len(fList):
        arr = (ctypes.c_float * len(_li))(*_li)
        return arr
    elif len(_li) == len(iList) + len(fList):
        _lii = [float(x) for x in _li]
        arr = (ctypes.c_float * len(_lii))(*_lii)
        return arr
    else:
        ErrorMessage("I don't know input type")
        pass

if __name__ == '__main__':
    Hello()
    li = list(range(0,100))
    arr = ListToArray(li)
    print(type(arr))
    li.append("abc")
    arr = ListToArray(li)
    print(type(arr))


