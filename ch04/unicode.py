#############################################
# unicode sort
import locale
#locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)
import pyuca
coll = pyuca.Collator()
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)

################################################
# normalize unicode
from unicodedata import normalize
s1 = 'café' # composed "e" with acute accent
s2 = 'cafe\u0301' # decomposed "e" and acute accent
print(len(s1), len(s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))

################################################
# unicode database
import unicodedata
import re
re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
print('unicode data: ', sample)
for c in sample:
    print('U+%04x' % ord(c),
        c.center(6),
        're_dig' if re_digit.match(c) else '-',
        'isdig' if c.isdigit() else '-',
        'isnum' if c.isnumeric() else '-',
        format(unicodedata.numeric(c), '5.2f'),
        unicodedata.name(c),
        sep='\t')
