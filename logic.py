#
import itertools

def dif(li1=[], li2=[]):
    _my = [elem for elem in li1 if not elem in li2]
    return _my

def interception(li1=[], li2=[]):
    _my = [elem for elem in li1 if elem in li2]
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
                _temp = []
                num=str(num)
                for _number in self.results:

                    if b and c:
                        if self.hasCows(_number, num) == c and \
                                self.hasBulls(_number, num) == b:
                            _temp.append(_number)
                    elif b:
                        self.KillxBull(num, b)
                    elif c:
                        self.results = dif(self.results, self.bulls0(num))
                        if c == 4:
                            self.results = interception(self.cows4(num), self.results)
                        else:
                            self.KillxCow(num, c)

                    else:
                        self.allIs0(num)
            if _temp:
                self.results = interception (self.results, _temp)
            return self.results
        else:
            return False

    def variants(self, num: str):
        _li = []
        for item in itertools.permutations (num):
            _li.append (''.join (x for x in item))
        return _li

    def killValue(self, value):
        try:
            self.results.remove (value)
        except ValueError:
            pass

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

    def hasCows(self, num1, num2):
        # Obtain number of cows that has num2 on num1
        # num1: num to determine cows
        # num2: num with data
        _cows = 0
        for it in range(len(num2)):
            if num2[it] in num1:
                if num2[it] != num1[it]:
                    _cows += 1

        return _cows

    def hasBulls(self, num1, num2):
        # num1: num to determine bulls
        # num2: num with data
        _bulls = 0
        for it in range(len(num2)):
            if num1[it] == num2[it]:
                _bulls += 1

        return _bulls

    def bulls0(self, num):
        _li = []
        for elem in self.results:
            if self.same_pos(num, elem):
                _li.append(elem)
        return _li

    def KillxCow(self, num, cows):
        for elem in self.results:
            if self.hasCows(elem, num) != cows:
                self.killValue (elem)

    def KillxBull(self, num, bull):
        for elem in self.results:
            if self.hasBulls(elem, num) != bull:
                self.killValue(elem)

if __name__ == '__main__':
    a = Results()

    a.addStatistics('1234', 0, 2)
    print(a.resolve())