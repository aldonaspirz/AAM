# Zdefiniuj zmienna ze slowem ’konstantynopolitańczykowianeczka’ oraz do nowych zmiennych
# przypisz następujące rzeczy:

# 1. pierwsza literę.
def iteracja(zmienna):
    nowa_z = zmienna[0]
    return nowa_z
# 2. ostatnia literę
def iteracja_1(zmienna):
    nowa_z = zmienna[-1]
    return nowa_z
    
        
# 3. środkowa literę
def iteracja_2(zmienna):
    a = len(zmienna)

    nowa_z= zmienna[int(a/2)]
    return nowa_z

# 5. ostatnie cztery litery.
def iteracja_3(zmienna):
    nowa_z= zmienna[-5:-1]
    return nowa_z


# 4. pierwsze cztery litery
def iteracja_4(zmienna):
    nowa_z=zmienna[0:4]
    return nowa_z

# 6. litery od srodkowej od czwartej od konca.

def iteracja_6(zmienna):
    a=len(zmienna)
    nowa_z=zmienna[(int(a/2)):-4]

    return nowa_z

# 7. uzywając liter 4 pierwszych i ostatnich stworz nowy ciag znakow
def iteracja_7(zmienna):
    nowa_z=zmienna[0:4]+zmienna[-4:]
    return nowa_z

# 8. zamien wszystkie litery w wyrazie na Wielkie litery
def iteracja_8(zmienna):
    
    return zmienna.upper()
# 9. zamien 4 pierwsze i ostatnie litery na Wielkie i stworz nowy wyraz aby odpowiadal tresci
# słowu oryginalnemu.
def iteracja_9(zmienna):
    
    return zmienna[:4].upper() +zmienna[-4:].upper()


wynik=iteracja('konstantynopolitańczykowianeczka')
wynik_1=iteracja_1('konstantynopolitańczykowianeczka')
wynik_2=iteracja_2('konstantynopolitańczykowianeczka')
wynik_3=iteracja_3('konstantynopolitańczykowianeczka')
wynik_4=iteracja_4('konstantynopolitańczykowianeczka')
wynik_6=iteracja_6('konstantynopolitańczykowianeczka')
wynik_7=iteracja_7('konstantynopolitańczykowianeczka')
wynik_8=iteracja_8('konstantynopolitańczykowianeczka')
wynik_9=iteracja_9('konstantynopolitańczykowianeczka')
print(wynik, wynik_1, wynik_2,wynik_3, wynik_4,wynik_6,wynik_7, wynik_8,wynik_9)