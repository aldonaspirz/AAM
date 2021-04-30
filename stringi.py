
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


wynik=iteracja(['konstantynopolitańczykowianeczka'])
wynik_1=iteracja_1(['konstantynopolitańczykowianeczka'])
wynik_2=iteracja_2(['konstantynopolitańczykowianeczka'])

print(wynik, wynik_1, wynik_2)