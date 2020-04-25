import sys

for line in sys.stdin:

    (num,val) = line.strip().split(" ")

    m = val.strip().split(",")

    for i in range(len(m)):
        print(num + ","+ str(m[i]) + "\t" + "1")

