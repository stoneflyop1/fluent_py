# 使用生成器示例
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word

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