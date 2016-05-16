import sys
from src.interpreter import eval


def main():
    with open(sys.argv[1], 'rb') as f:
        eval(f.read())


if __name__ == '__main__':
    main()
