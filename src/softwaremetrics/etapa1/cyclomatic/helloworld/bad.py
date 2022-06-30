

def foo(x: int) -> str:
    if x == 0:
        return 'hello'
    elif x == 1:
        return 'world'
    elif x == 2:
        return '!'
    else:
        return '??'


def bar(x: int) -> str:
    if x == 0:
        return 'hello'
    elif x == 1:
        return 'world'
    else:
        return '!'


for i in range(4):
    print(foo(i), bar(i), end=' ')
