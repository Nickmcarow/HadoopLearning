import sys

for line in sys.stdin:
    a = line.strip().split(" ")

    for i in a:
        for b in a:
            if i != b:
                print(i + ',' + b + '\t1')


