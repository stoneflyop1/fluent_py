class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        # step带有类型信息, begin和end只是整数
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

def aritprog_gen(begin, step, end=None):
    # step带有类型信息, begin和end只是整数
    result = type(step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

def aritprog_gen2(begin, step, end=None):
    import itertools
    first = type(step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen


if __name__ == '__main__':
    ap = ArithmeticProgression(0,1,3)
    print(list(ap))
    ap = ArithmeticProgression(1, 0.5, 3)
    print(list(ap))
    from fractions import Fraction
    ap = ArithmeticProgression(0, Fraction(1, 3), 1)
    print(list(ap))
    from decimal import Decimal
    ap = ArithmeticProgression(0, Decimal('0.1'), 0.3)
    print(list(ap))
    ap1 = aritprog_gen(1, 0.5, 6)
    print(list(ap1))
    ap2 = aritprog_gen2(1, Decimal('0.5'), 6)
    print(list(ap2))