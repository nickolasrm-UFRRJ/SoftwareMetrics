import os


def radon(file: str):
    dir = os.path.dirname(__file__)
    os.system(f'radon.exe cc {os.path.join(dir, file)}'
              ' --total-average')


radon('menu/bad.py')
radon('menu/good.py')
radon('helloworld/bad.py')
radon('helloworld/good.py')
