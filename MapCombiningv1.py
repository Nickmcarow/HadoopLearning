import sys



for line in sys.stdin:

    r = dict()

    for token in line.strip().split(" "):
        # print(token)

        if token in r:
            r[token] = r[token] + 1
        else:
            r[token] = 1
    for k in r.keys():
        print(k + '\t' + str(r[k]))