print("podaj liczbe")
a=int(input())
tekst=""
t=""
for i in range(a):
    for j in range(a,1,-1):
       tekst=tekst+" "
    tekst = tekst + "X"
    print(tekst)