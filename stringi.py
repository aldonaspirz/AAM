# 1. pierwsza literę.
def iteracja(zmienna):
    for i in zmienna:
        words=[]

        for j in i:
        
            words.append(j)
            return words[0]
# 2. ostatnia literę
def iteracja_1(zmienna):
    for i in zmienna:
        words=[]

        for j in i:
        
            words.append(j)
        return words[-1]
# 3. środkowa literę
def iteracja_2(zmienna):
    for i in zmienna:
        words=[]
        a=0

        for j in i:
            
            words.append(j)
        a=len(words)
        

        return words[int(a/2)]
# 5. ostatnie cztery litery.
def iteracja_3(zmienna):
    for i in zmienna:
        words=[]
       

        for j in i:
            
            words.append(j)
        
        

        return words[-5:-1]
# 4. pierwsze cztery litery
def iteracja_4(zmienna):
    for i in zmienna:
        words=[]
       

        for j in i:
            
            words.append(j)
        
        

        return words[0:4]

# 6. litery od srodkowej od czwartej od konca.

def iteracja_6(zmienna):
    for i in zmienna:
        words=[]
        a=0

        for j in i:
            
            words.append(j)
        a=len(words)
        

        return words[(int(a/2)):-4]

# 7. uzywając liter 4 pierwszych i ostatnich stworz nowy ciag znakow
def iteracja_7(zmienna):
    for i in zmienna:
        words=[]
       

        for j in i:
            
            words.append(j)
        
    return words[0:4] + words[-4:]

        # 8. zamien wszystkie litery w wyrazie na Wielkie litery
def iteracja_8(zmienna):
    
    return zmienna.upper()
# 9. zamien 4 pierwsze i ostatnie litery na Wielkie i stworz nowy wyraz aby odpowiadal tresci
# słowu oryginalnemu.
def iteracja_9(zmienna):
    
    return zmienna[:4].upper() +zmienna[-4:].upper()


wynik=iteracja(['konstantynopolitańczykowianeczka'])
wynik_1=iteracja_1(['konstantynopolitańczykowianeczka'])
wynik_2=iteracja_2(['konstantynopolitańczykowianeczka'])
wynik_3=iteracja_3(['konstantynopolitańczykowianeczka'])
wynik_4=iteracja_4(['konstantynopolitańczykowianeczka'])
wynik_6=iteracja_6(['konstantynopolitańczykowianeczka'])
wynik_7=iteracja_7(['konstantynopolitańczykowianeczka'])
wynik_8=iteracja_8('konstantynopolitańczykowianeczka')
wynik_9=iteracja_9('konstantynopolitańczykowianeczka')
print(wynik, wynik_1, wynik_2,wynik_3, wynik_4,wynik_6,wynik_7, wynik_8,wynik_9)