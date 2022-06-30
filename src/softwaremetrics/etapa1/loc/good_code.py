from typing import Any


def lots_of_branches(x: Any):
    if x in range(1, 5):
        return x*2
    else:
        return x

lots_of_branches(5)