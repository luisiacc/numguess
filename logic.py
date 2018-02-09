#
import random
import itertools


class Results:
    def __init__(self):
        self.numTable = self.build_table()
        self.statistics = []
        self.results = []

    def build_table(self):
        _all = []
        def has_extra(num):
            num = str (num)
            for char in num:
                if num.count (char) > 1:
                    return True

        for number in range(1000, 10000):
            if not has_extra(number):
                _all.append(number)

        return _all

    def addStatistics(self, number, bulls, cows):
        self.statistics.append((number, bulls, cows))

    def resolve(self):
        if self.statistics:
            for table_number in self.numTable:
                cows = 0
                bulls = 0
                number = str(table_number)
                for num, b, c in self.statistics:
                    if b and c:
                        pass
                    elif b:
                        pass
                    elif c:
                        pass
                    else:
                        pass

        else:
            return False


