import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30] # ordered list
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31] # values to find

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        print (position)
        offset = position * '  |' 
        print('{0:2d} @ {1:2d}    {2}{0:<2d}'.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        fn = bisect.bisect_left
    else:
        fn = bisect.bisect
    
    print('DEMO:', fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK)) 
    demo(fn)