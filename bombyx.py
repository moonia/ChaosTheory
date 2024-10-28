#!/usr/bin/env python3

import sys

def usage():
    print("USAGE")
    print("    ./bombyx n [k | i0 i1]\n")
    print("DESCRIPTION")
    print("    n       number of first generation individuals")
    print("    k       growth rate from 1 to 4")
    print("    i0      initial generation (included)")
    print("    i1      final generation (included)")
    sys.exit(0)

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print("Invalid number of arguments")
    sys.exit(84)

try:
    n = int(sys.argv[1])
except ValueError:
    print("First argument must be an integer")
    sys.exit(84)

if len(sys.argv) == 3:
    try:
        k = float(sys.argv[2])
        if k < 1 or k > 4:
            raise ValueError
    except ValueError:
        print("Second argument must be a decimal number between 1 and 4 inclusive")
        sys.exit(84)

if len(sys.argv) == 4:
    try:
        i0 = int(sys.argv[2])
        i1 = int(sys.argv[3])
    except ValueError:
        print("Third and fourth arguments must be integers")
        sys.exit(84)

    if i0 < 1:
        print("Third argument must be greater than or equal to 1")
        sys.exit(84)
    elif i1 < i0:
        print("Fourth argument must be greater than or equal to the third argument")
        sys.exit(84)

if len(sys.argv) == 2 and sys.argv[1] == "-h":
    usage()

if len(sys.argv) == 3:
    n = float(sys.argv[1])
    k = float(sys.argv[2])
    i = 1

    if n < 0:
        print("First argument must be greater than 0")
        sys.exit(84)
    else:
        while i <= 100:
            print("%d %.2f" %(i, n))
            n = k * n * ((1000 - n) / 1000)
            if n < 0:
                n = 0
            i += 1

if len(sys.argv) == 4:
    k = 1.00

    if n < 0:
        print("First argument must be greater than 0")
        sys.exit(84)
    else:
        while k <= 4:
            i = 1
            n = float(sys.argv[1])
            while i < i0:
                n = n * k * ((1000 - n) / 1000)
                if n < 0:
                    n = 0
                i += 1
            while i <= i1:
                print("%.2f %.2f" % (k, n))
                n = n * k * ((1000 - n) / 1000)
                if n < 0:
                    n = 0
                i += 1
            k += 0.01
