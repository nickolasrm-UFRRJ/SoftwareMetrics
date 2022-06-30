from glob import glob
import os


if __name__ == '__main__':
    dir = os.path.dirname(__file__)
    bad = os.path.join(dir, 'bad', '*.py')
    os.system(f'pyan3 {bad} --uses --no-defines'\
              ' --colored --grouped --annotated --html > bad.html')
    os.system(f'multimetric {" ".join(glob(bad))}')
    os.system(f'bad.html')
