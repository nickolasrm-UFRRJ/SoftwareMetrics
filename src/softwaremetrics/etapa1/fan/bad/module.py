
from softwaremetrics.etapa1.fan.bad.module2 import bar


def foo(x: int) -> str:
    if x > 10:
        x += 1
        bar(x)

print(foo(0))
