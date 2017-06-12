
# Character encode decode
s = 'café'
print(s)
print(len(s))
b = s.encode('utf8')
print(b)
print(len(b))
c = b.decode('utf8')
print(c)