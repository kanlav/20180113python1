# This program adds up integers in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
    print('success ')
except ValueError:
    print('Please supply integer arguments')
