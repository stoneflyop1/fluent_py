# 使用生成器示例2, lazy模式
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # genexp
        # return (match.group() for match in RE_WORD.finditer(self.text))
        # gen yield
        for match in RE_WORD.finditer(self.text): # finditer是lazy的
            yield match.group()

if __name__ == '__main__':
    s = Sentence('"The time has come," the Walrus said,')
    print(repr(s))
    for word in s: print(word)
    print(list(s))

    s3 = Sentence('Pig and Pepper')
    it = iter(s3)
    print(it)
    print(next(it))
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration:
        print('StopIteration')
    print(list(it))
    print(list(iter(s3)))