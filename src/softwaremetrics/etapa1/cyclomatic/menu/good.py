
def menu():
    def call_pass(): pass

    ops = {0: call_pass,
           1: call_pass,
           2: call_pass}
    op = 0
    while op != -1:
        if op in ops:
            ops[op]()
        else:
            op = -1


if __name__ == '__main__':
    menu()
