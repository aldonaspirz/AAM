# 1. Stwórz słownik w którym kluczami będą ulubione napoje (bezalkoholowe), a wartosciami
# ich ocena w skali od 0 do 10.
from typing import KeysView


bezalko={'woda':10, 'cola':9, 'orange juice':8, 'lemoniada':7, 'woda gazowana':6, 'fanta':5, 'sprite':4, 'pinapple juice':3, 'piwo bezalkoholowe':2, 'sok porzeczkowy':1, 'pepsi':0 }
# 2. Dodaj do słownika 5 napojow alkoholowych wraz z ich ocena
A={'piwo':10,'wino czerwone':9,'wino biale':8, 'whiskey':7,'rum':6}
bezalko.update(A)

print(bezalko)

# 3. Wyswietl wszystkie nazwy płynów.
print(bezalko.keys())

# 4. Wyswietl wszystkie oceny płynów.
print(bezalko.values())

# 5. Posortuj nazwy płynów alfabetycznie
print(sorted(bezalko))

# 6. Odwróć kolejność sortowania nazw płynów
print(sorted((bezalko),reverse=True))

# 7. Posortuj oceny od najmniejszej do najwiekszej.
print('rozwiazanie nr 7:',sorted((bezalko.items()),reverse=True,key=lambda x: x[1]))

# 8. Stwórz nowy słownik, który bedzie miał przypisane rateingi od najmniejszego do największego do alfabetycznej kolejności nazw.
def raitings(zmienna):
    klucze=sorted(bezalko)
    wartosci=sorted((bezalko.items()),key=lambda x: x[1])
    
    zip_iterator = zip(klucze, wartosci)
    nowy_s=dict(zip_iterator)
    return nowy_s
wyniki8=raitings(bezalko)
print(wyniki8)

# 9. Stworz słownik który będzie zawierał wszystkie listy z ćwiczenia nr 3.
