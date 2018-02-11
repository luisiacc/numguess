
def dif(li1=[], li2=[]):
    _my = []
    for elem in li1:
        if not elem in li2:
            _my.append(elem)

    return _my

def interception(li1=[], li2=[]):
    _my = []
    for elem in li1:
        if elem in li2:
            _my.append(elem)

    return _my




