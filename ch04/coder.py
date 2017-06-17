#######################
# encode demo
for codec in ['latin_1', 'utf_8', 'utf_16']:
    try:
        print(codec, 'El 你好'.encode(codec), sep='\t')
    except UnicodeEncodeError as e:
        print(e)


########################
# decode demo
octets = b'Hello\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
try:
    print(octets.decode('utf_8'))
except UnicodeDecodeError as e:
    print(e)


###########################################
# handle text files, get default encoding
print('------------get default encoding------------')
import sys, locale
expressions = '''
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
    '''
my_file = open('dummy.test', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))


#############################################
# Normalizing Unicode for Saner Comparisons
print('---------------Normalizing Unicode----------------')
s1,s2 = ('café', 'cafe\u0301')
print(s1,s2)
print(len(s1), len(s2), s1 == s2)
from unicodedata import normalize, name
print('NFC', len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print('NFD', len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print('NFC==NFD', normalize('NFC', s1)==normalize('NFD', s1))
half = '\u00BD' #'1⁄2'
print(half, normalize('NFKC', half))
micro = 'μ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print('ord', ord(micro), ord(micro_kc))
print('name', name(micro), ', ', name(micro_kc))


############################################
# case folding
print('---------------case folding----------------')
micro_cf = micro.casefold()
print(micro_cf,',', name(micro_cf))
eszett = 'ß'
print(eszett, name(eszett))
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)