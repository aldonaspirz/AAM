# 1. Stwórz pętle po elementach listy nr 4 oraz wyświetl każdy z nich.
#  4. Stwórz pętle po kluczach słownika nr 2. i wyświetl każdy z kluczy.



lista=['cola', 'fanta', 'lemoniada', 'orange juice', 'pepsi', 'pinapple juice', 'piwo', 'piwo bezalkoholowe', 'rum', 'sok porzeczkowy', 'sprite', 'whiskey', 'wino biale', 'wino czerwone', 'woda', 'woda gazowana']
for i in lista:
    print(i)
# 2. Stwórz pętle po posortowanych elementach listy nr 4 i wyświetl je po kolei
lista.sort()
for i in lista:
    
    print(i)

# 3. Wyświetlając elementy z pkt. 2 wyświetl jego index.
for i,v in enumerate(lista):
    print('zadanie 3',i,v)  

#  4. Stwórz pętle po kluczach słownika nr 2. i wyświetl każdy z kluczy.
# patrz zadanie nr 1    

# 5. Stwórz pętle po kluczach słownika nr 2. i wyświetl każdy z kluczy oraz odpowiadającą
# mu wartość.
slownik={'woda': 10, 'cola': 9, 'orange juice': 8, 'lemoniada': 7, 'woda gazowana': 6, 'fanta': 5, 'sprite': 4, 'pinapple juice': 3, 'piwo bezalkoholowe': 2, 'sok porzeczkowy': 1, 'pepsi': 0, 'piwo': 10, 'wino czerwone': 9, 'wino biale': 8, 'whiskey': 7, 'rum': 6}
for i in slownik.items():
    print(i)

# 6. Stwórz pętle tylko wartościach w słowniku.
for key,value in slownik.items():
    print(value)
    
    

# 7. Stwórz pętle która iteruje po kluczach i wartościach jednoczesnie i wyświetl oba.

for key, value in slownik.items():
    print(key ,value)

for key in slownik:
    print('przykład 1:',key)

for key in slownik.items():
    print('przykład 2:',key)

for key in slownik.values():
    print('przykład 3:',key)