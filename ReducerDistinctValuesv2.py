import sys

d = {}
for line in sys.stdin:
    value, key = line.strip().split("\t")
    d.setdefault(key, set()).add(value)

for key, value in d.items():
    print(f"{key}\t{len(value)}")

    # import sys
    #
    # r = dict()
    # dr = dict()
    #
    # for line in sys.stdin:
    #
    #     num, val = line.strip().split("\t")
    #
    #     s = num + val
    #
    #     if s not in r:
    #         r[s] = val
    #
    # for i in r.keys():
    #
    #     # print(r[i])
    #     if r[i] in dr:
    #         dr[r[i]] = dr[r[i]] + 1
    #     else:
    #         dr[r[i]] = 1
    #
    # for i in dr.keys():
    #     print(i + '\t' + str(dr[i]))