registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register # 立即执行，在模块加载后，主函数执行前
def f1():
    print('running f1()')

@register # 立即执行，在模块加载后，主函数执行前
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()