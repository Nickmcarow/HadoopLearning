import sys

r = dict()

for line in sys.stdin:

    (num,val) = line.strip().split(" ")

    if num not in r:
        r[num] = ""

for i in r.keys():
    print(r[i])

