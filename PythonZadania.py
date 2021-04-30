# a = 10
# Każdej z nastepujacych wartosci przypisac do niezaleznej zmiennej.
# • Pole okregu 1 o promieniu a.
# • Obwod okregu 1 o promieniu a.
import math
def poleOkregu(a):
    pole=a*a*math.pi
    return pole
    

def obwodOkregu(a):
    obwod=a*2*math.pi
    return obwod
pole1=poleOkregu(10)
print(pole1)
obwod1=obwodOkregu(10)
print(obwod1)




# b = 20
# • Pole kwadratu 1 o ramieniu b.
# • Obwod kwadratu 1 o ramieniu b

def polekwadrat(b):
    pole=b*b
    return pole

def obwodkwadrat(b):
    obwod=4*b
    return obwod

asd = polekwadrat(20)
print(asd)
asd2= obwodkwadrat(20)
print(asd2)

# kwadrat(20)

# # Oblicz wartosci x1 oraz x2 dla wielomianu 
# # f(x) = 4x2 − 2x − 5
import numpy as np
coeff = [4,2,-5]
x=[]
x=np.roots(coeff)
print('x1=', x[0], 'x2=', x[1])