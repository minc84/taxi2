from itertools import combinations_with_replacement
l1 = list(combinations_with_replacement('HACK',2))
print(l1)
l2 = (', '.join(map(str, l1)))
print(l2)
l3=print(type(l2))
