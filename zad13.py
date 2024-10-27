#wymiary tablicy
n=7
m=10

from random import seed
from random import randint
seed()
#sposob 1
a=[randint(0,20)]*n
for i in range(n):
    a[i]=[randint(0,20)]*m
    for k in range(m):
        a[i][k]=randint(0,20)
for j in range(n):
    print(a[j])