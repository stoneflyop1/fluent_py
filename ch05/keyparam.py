#####################################
# @param {name} 位置参数，也可以按照关键字参数传入
# @param {cls} 仅能作为关键字参数(因为在星号参数之后给出)，即：传入参数时必须写cls=value；是python3的特性
# @param {content} 所有从第二个开始不是以关键字传入的参数都会以tuple的形式被此参数捕获
# @param {attrs} 按照词典展开参数，若可以匹配位置参数则会认为是位置参数，其他作为key-value形式提供给函数

def tag(name, *content, cls=None, **attrs):
    ''' generate one or more HTML tags '''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                    for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                            (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))
my_tag = {'name':'img', 'title':'Sunset boulevard',
     'src':'sunset.jpg', 'cls':'framed'}
print(tag(**my_tag))


def f(a, *, b):
    ''' 关键字Only的参数示例 b仅能按照关键字参数传入'''
    return a, b

try:
    print(f(1,2))
except:
    print('b is keyword only')

print(f(1,b=2))