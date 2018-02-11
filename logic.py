#
import random
import itertools

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


class Results:
    def __init__(self):
        self.numTable = self.build_table()
        self.statistics = []
        self.results = self.build_table()

    def build_table(self):
        _all = []
        def has_extra(num):
            num = str (num)
            for char in num:
                if num.count (char) > 1:
                    return True

        for number in range(1000, 10000):
            if not has_extra(number):
                _all.append(str(number))

        return _all

    def addStatistics(self, number, bulls, cows):
        self.statistics.append((number, bulls, cows))

    def remove(self, arg):
        _al = []
        for i in self.results:
            if arg not in i:
                _al.append(i)
            else:
                pass

        self.results = _al.copy()

        return None

    def remove_with(self, args=None):
        for char in args:
            self.remove(char)

    def resolve(self):
        if self.statistics:
            for num, b, c in self.statistics:
                num=str(num)
                for _number in self.results:
                    if b and c:
                        pass
                    elif b:
                        if b == 4:
                            self.results = interception(self.cows4(), self.results)
                    elif c:
                        pass
                    else:
                        self.allIs0(num)
        else:
            return False

    def variants(self, num: str):
        _li = []
        for item in itertools.permutations (num):
            _li.append (''.join (x for x in item))
        return _li

    def same_pos(self, n, m):
        for _int in range(len(n)):
            if n[_int] == m[_int]:
                return True

    def cows4(self, num: str):
        # Also does the trick for 0 bulls
        _li = []
        for var in self.variants(num):
            if self.same_pos(num, var):
                pass
            else:
                _li.append(var)

        return _li

    def allIs0(self, num):
        self.remove_with(num)

a = Results()

