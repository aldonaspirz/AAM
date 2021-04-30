import math

import numpy as np
# a = 10
# Każdej z nastepujacych wartosci przypisac do niezaleznej zmiennej.
# • Pole okregu 1 o promieniu a.
# • Obwod okregu 1 o promieniu a.



def pole_okregu(a):
    pole=a*a*math.pi
    return pole
    

def obwod_okregu(a):
    obwod=a*2*math.pi
    return obwod
pole1=pole_okregu(10)
obwod1=obwod_okregu(10)
print(pole1,obwod1)






# b = 20
# • Pole kwadratu 1 o ramieniu b.
# • Obwod kwadratu 1 o ramieniu b

def pole_kwadrat(b):
    pole=b*b
    return pole

def obwod_kwadrat(b):
    obwod=4*b
    return obwod

asd = pole_kwadrat(20)
asd2= obwod_kwadrat(20)
print(asd,asd2)

# kwadrat(20)

# # Oblicz wartosci x1 oraz x2 dla wielomianu 
# # f(x) = 4x2 − 2x − 5


coeff = [4,2,-5]
x=[]
x=np.roots(coeff)
print('x1=', x[0], 'x2=', x[1])
