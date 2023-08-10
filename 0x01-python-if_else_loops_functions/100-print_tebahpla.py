#!/usr/bin/python3

start = ord('z')
end = ord('a')
for i in range(start, end - 1, -1):
    if i % 2 == 1:
        print("{:c}".format(i - 32), end="")
    print("{:c}".format(i), end="")
