#wymiary tablicy
n=3
m=4

#sposob 1
a=[0]*n
for i in range(n):
    a[i]=[0]*m
print(a)

#sposob 2
a=[]
for i in range(n):
    a.append([0]*m)
print(a)