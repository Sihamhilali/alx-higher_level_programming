#!/usr/bin/python3

start = ord('a')
end = ord('z')
for a in range(start, end + 1):
    print("{:c}".format(a), end=" ")
