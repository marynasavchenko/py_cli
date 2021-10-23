import sys


def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('argument :: {}'.format(arg))

    print(format('py cli'))


if __name__ == '__main__':
    main()
