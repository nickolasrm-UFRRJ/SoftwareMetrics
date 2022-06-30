

def foo(x: int) -> str:
    answers = {0: 'hello',
               1: 'world',
               2: '!'}
    return answers.get(x, '??')


def bar(x: int) -> str:
    answers = {0: 'hello',
               1: 'world'}
    return answers.get(x, '!')


for i in range(4):
    print(foo(i), bar(i), end=' ')
