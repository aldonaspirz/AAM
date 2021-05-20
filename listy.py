# . Stworz liste (A) skladajaca sie z 11 liczb calkowitych.
A=[1,2,3,4,5,6,7,8,9,10,11]
# Rozszerz tę listę o 10 liczb calkowitych.
A.extend(range(12,22))
# Zamien czesc ujemną z pierwszej listy na 5 pierwszych liczb z listy B.

# Zamień elementy 3, 7, 10 nowej listy na rozne litery.


replacements = {
    3: 'c',
    7: 'g',
    10: 'z',
}

A = [replacements.get(x, x) for x in A]

# Usun liczby ktore sa miedzy literami
def zadanie6(zmienna):
    list=[]
    for i in zmienna:
        
        if type(i) is str:
            list.append(i)
    return list

wynik6=zadanie6(A)
print(wynik6)

# Stworz 5-elementową liste ktora zawiera dowolne litery.
import string
import random
def zadanie7():
    list=[]
    for i in range(5):
        random_letter = random.choice(string.ascii_letters)
        list.append(random_letter)
        
    return list
wynik7=zadanie7()
print(wynik7)
lista_new=[]
wynik7.reverse()
lista_new=wynik7
print(lista_new)


