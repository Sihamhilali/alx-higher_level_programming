#!/usr/bin/python3

start = ord('a')
end = ord('z')
for a in range(start, end + 1):
    if chr(a) != 'e' and chr(a) != 'q':
        print('{:s}'.format(chr(a)), end='')
