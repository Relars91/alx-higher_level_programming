#!/usr/bin/python3

def infinite(args):
    total = 0
    for a in args[1:]:
        total += int(a)
    print(total)


if __name__ == "__main__":
    import sys

    infinite(sys.argv)
