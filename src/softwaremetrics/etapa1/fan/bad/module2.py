from softwaremetrics.etapa1.fan.bad.module3 import defg


def abc(x: int) -> int:
    return x+10


def bcd(x: int) -> int:
    return x / 2


def bar(x: int) -> int:
    return defg(bcd(abc(x)))
