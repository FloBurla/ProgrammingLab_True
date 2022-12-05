def sum_list(lista):
    Somma = 0
    for variable in lista:
        Somma += variable
    return Somma

lista=[1,12,61,42,59,15,28,13,77,11]
Somma=sum_list(lista)
print(Somma)