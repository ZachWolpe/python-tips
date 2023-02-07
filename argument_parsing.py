




# optional args
import getopt
import sys

opts, args = getopt.getopt(
    sys.argv[1:],
    'f:m:',
    ['filename','message']
    )

print()
print('opt:     ', opts)
print('args:    ', args)
print()

for (opt, arg) in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg
