
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




wynik=iteracja(['konstantynopolitańczykowianeczka'])
wynik_1=iteracja_1(['konstantynopolitańczykowianeczka'])
wynik_2=iteracja_2(['konstantynopolitańczykowianeczka'])
wynik_3=iteracja_3(['konstantynopolitańczykowianeczka'])
wynik_4=iteracja_4(['konstantynopolitańczykowianeczka'])

print(wynik, wynik_1, wynik_2,wynik_3, wynik_4)