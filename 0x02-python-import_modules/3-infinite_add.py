#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_num = len(argv) - 1
    if arg_num == 0:
        print("{}".format(arg_num))
    else:
        result = []
        for i in range(1, arg_num + 1):
            result.append(int(argv[i]))
        print("{}".format(sum(result)))
