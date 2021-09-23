import itertools      

d ={'1':['a','b', 'c'], '2':['d','e', 'f']}

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))