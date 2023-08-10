#!/usr/bin/python3

def uppercase(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        c = chr(ord(c) - 32)
    return c