#!/usr/local/bin/python3
import sys

def is_periodic(string):
    pattern = ''
    for char in string:
        # Increment pattern
        pattern += char
        n = len(pattern)
        if len(string) % n != 0:
            continue
        periodic = True
        reps = 1
        for i, base in enumerate(range(n, len(string), n)):
            if pattern != string[base:base+n]:
                periodic = False
                break
            reps += 1
        if periodic and reps > 1:
            return reps, pattern
    return 0, None

if __name__ == '__main__':
    value = sys.argv[1]
    print('(n, P) =', is_periodic(value))
