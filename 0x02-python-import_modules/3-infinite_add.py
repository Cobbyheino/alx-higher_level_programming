#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import math
    totalsum = 0
    for i in sys.argv:
        totalsum += int(i)
        print("{}".format(totalsum))
