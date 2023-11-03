#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argcount = len(sys.argv)
    if argcount == 1:
        print("{} arguments.".format(argcount - 1))
    elif argcount == 2:
        print("{} argument:".format(argcount - 1))
    else:
        print("{} arguments:".format(argcount - 1))
    for i in range(1, argcount):
        print("{}: {}".format(i, sys.argv[i]))
