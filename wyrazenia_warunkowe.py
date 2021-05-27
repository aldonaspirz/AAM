# Stwórz pętle po elementach listy nr 4 oraz wyświetl co drugi z nich.
slownik={'woda': 10, 'cola': 9, 'orange juice': 8, 'lemoniada': 7, 'woda gazowana': 6, 'fanta': 5, 'sprite': 4, 'pinapple juice': 3, 'piwo bezalkoholowe': 2, 'sok porzeczkowy': 1, 'pepsi': 0, 'piwo': 10, 'wino czerwone': 9, 'wino biale': 8, 'whiskey': 7, 'rum': 6}



dictlist=[]
for key, value in slownik.items():
    print(key ,value)
    temp = [key,value]
    dictlist.append(temp)

co_druga=dictlist[::2]
print(co_druga)

# 2. Stwórz pętle po kluczach słownika nr 2. i wyświetl tylko te krótsze niż 5 liter - inne pomiń.
for key, value in slownik.items():
    if len(key)<5:
        print(key)

# 3. Wyświetl co drugi klucz dłuższy niż 5 liter
for key, value in slownik.items():
    if len(key)>5:
        print('zadanie 3',key)

# Wyświetl ratingi większe niż 4
for key, value in slownik.items():
    if value>5:
        print(value)

# 5. Sprawdz które ratingi z poprzedniego punktu są liczbą pierwszą
for key, value in slownik.items():
    if value>5:
        print(value)
            if value