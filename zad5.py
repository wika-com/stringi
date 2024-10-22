print("Podaj imiona rozdzielone prxecinkami:")
imiona=input()
lista=imiona.split(",")
for i in range(len(lista)):
    if lista[i][-1]=="a":
        print(lista[i])
