from typing import Any


def lots_of_branches(x: int):
    if x == 1:
        return x+1
    elif x == 2:
        return x+2
    elif x == 3:
        return x+3
    elif x == 4:
        return x+4
    else:
        return x
    #match x:
    #    case 1:
    #        return x+1
    #    case 2:
    #        return x+2
    #    case 3:
    #        return x+3
    #    case 4:
    #        return x+4
    #    case _:
    #        return x

lots_of_branches(5)
