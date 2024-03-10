from itertools import permutations

my_list = [1, 2, 3, 4, 5, 6, 7]
my_list2 = ['A', 'B', 'C', 'D']

list_of_permutations = permutations(my_list)
list_of_permutations2 = permutations(my_list2)
cnt = 0
cnt2 = 0

for permutation in list_of_permutations:
    cnt += 1

for permutation in list_of_permutations2:
    cnt2 += 1

print(len(my_list), cnt)
print(len(my_list2), cnt2)
