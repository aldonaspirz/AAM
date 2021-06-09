import math
def rownanie_kwadratowe(a,b,c):
    if a!=0:
        delta=b*b-4*a*c
        if delta>0:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)

        if delta<0:
            pass
        if delta==0:
            x=-b/(2*a)
            return x
    else:
         pass
    return x1,x2


wynik=rownanie_kwadratowe(-1,2,3)
print(wynik)