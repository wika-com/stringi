print("podaj a i b")
ab=input()
boki=ab.split(" ")
a=int(boki[0])
b=int(boki[1])
p=0
ob=0
if a>0 and b>0:
    p=a*b
    ob=2*a+2*b
else:
    print("złe dane")
print(p, ob)