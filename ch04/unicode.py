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


######################################
# unicode dual mode
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')
text_str = ('Ramanujan saw \u0be7\u0bed\u0be8\u0bef'
    " as 1729 = 1³ + 12³ = 9³ + 10³.")
text_bytes = text_str.encode('utf_8')
print('Text', repr(text_str), sep='\n ')
print('Numbers')
print('   str  :', re_numbers_str.findall(text_str))
print('   bytes:', re_numbers_bytes.findall(text_bytes))
print('   str  :', re_words_str.findall(text_str))
print('   bytes:', re_words_bytes.findall(text_bytes))

