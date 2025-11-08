'''
Input two sets and do the following-
A = {1,2,3,4}
B = {4,5,6,7}
1. Union - {1,2,3,4,5,6,7}
2. Intersection - {4}
3. Difference - {1,2,3}
'''
A = input('Enter the first set: ')
A = set(A.split(' '))
B = input('Enter the second set: ')
B = set(B.split(' '))
print(A, B)
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
