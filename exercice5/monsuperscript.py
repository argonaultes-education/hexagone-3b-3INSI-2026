import sys

if __name__ == '__main__':
    if 2 == len(sys.argv):
        nb_digits = int(sys.argv[1])
        for i in range(10**nb_digits):
            print(f'{i}'.rjust(nb_digits, '0'))
    