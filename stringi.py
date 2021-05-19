
def iteracja(zmienna):
    for i in zmienna:
        words=[]

        for j in i:
        
            words.append(j)
            return words[0]

def iteracja_1(zmienna):
    for i in zmienna:
        words=[]

        for j in i:
        
            words.append(j)
        return words[-1]

def iteracja_2(zmienna):
    for i in zmienna:
        words=[]
        a=0

        for j in i:
            
            words.append(j)
        a=len(words)
        

        return words[int(a/2)]

def iteracja_3(zmienna):
    for i in zmienna:
        words=[]
       

        for j in i:
            
            words.append(j)
        
        

        return words[-5:-1]

def iteracja_4(zmienna):
    for i in zmienna:
        words=[]
       

        for j in i:
            
            words.append(j)
        
        

        return words[0:4]

def iteracja_6(zmienna):
    for i in zmienna:
        words=[]
        a=0

        for j in i:
            
            words.append(j)
        a=len(words)
        

        return words[(int(a/2)):-4]

def iteracja_7(zmienna):
    for i in zmienna:
        words=[]
       

        for j in i:
            
            words.append(j)
        
    return words[0:4], words[-4:-1]

        
def iteracja_8(zmienna):
    
    return zmienna.upper()

def iteracja_9(zmienna):
    
    return zmienna.upper()


wynik=iteracja(['konstantynopolitańczykowianeczka'])
wynik_1=iteracja_1(['konstantynopolitańczykowianeczka'])
wynik_2=iteracja_2(['konstantynopolitańczykowianeczka'])
wynik_3=iteracja_3(['konstantynopolitańczykowianeczka'])
wynik_4=iteracja_4(['konstantynopolitańczykowianeczka'])
wynik_6=iteracja_6(['konstantynopolitańczykowianeczka'])
wynik_7=iteracja_7(['konstantynopolitańczykowianeczka'])
wynik_8=iteracja_8('konstantynopolitańczykowianeczka')

print(wynik, wynik_1, wynik_2,wynik_3, wynik_4,wynik_6,wynik_7, wynik_8)