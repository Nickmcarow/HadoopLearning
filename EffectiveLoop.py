from collections import defaultdict
import sys

for line in sys.stdin:
    keys = line.strip().split()
    for a in keys:
        cnt = defaultdict(int)
        for b in keys:
            if a != b: cnt[b] += 1
        print(a, end='\t')
        print(','.join([f'{key}:{val}' for key, val in cnt.items()]))