def dictionary():
    record = []
    def getitem(key):
        match = [x for x in record if x[0] == key]
        key , value = match[0]
        return value
    def setitem(key,value):
        nonlocal record
        no_match = [x for x in record if x[0] != key]
        record =  no_match + [[key,value]]
        return record
    def dispatch(message,key=None,value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key,value)
    return dispatch
d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)
d('getitem', 3)

d('getitem', 4)

