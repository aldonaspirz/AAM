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

print(poleOkregu(10))
print(obwodOkregu(10))




# b = 20
# • Pole kwadratu 1 o ramieniu b.
# • Obwod kwadratu 1 o ramieniu b

def polekwadrat(b):
    pole=b*b
    return pole

def obwodkwadrat(b):
    obwod=4*b
    return obwod

print(polekwadrat(20))
print(obwodkwadrat(20))

# kwadrat(20)

# # Oblicz wartosci x1 oraz x2 dla wielomianu 
# # f(x) = 4x2 − 2x − 5
# import numpy as np
# coeff = [4,2,-5]
# np.roots(coeff)
# print(np.roots(coeff))