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

print(A)