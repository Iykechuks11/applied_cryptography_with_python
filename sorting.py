a = [3, 9, 2, 24, 1, 6]
b = ['a', 'b', 'c', 'd', 'e']
c1 = zip(a, b)
print(c1)
c = sorted(c1)
print(c)
# [(1, 'e'), (2, 'c'), (3, 'a'), (9, 'b'), (24, 'd')]
d = sorted(zip(a, b), key=lambda x: x[1])
print(d)
# [(3, 'a'), (9, 'b'), (2, 'c'), (24, 'd'), (1, 'e')]
