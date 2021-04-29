# a = 10
# Każdej z nastepujacych wartosci przypisac do niezaleznej zmiennej.
# • Pole okregu 1 o promieniu a.
# • Obwod okregu 1 o promieniu a.
import math
def poleOkregu(a):
    pole=a*a*math.pi
    obwod=a*2*math.pi
    print(pole)
    print(obwod)


poleOkregu(10)



# b = 20
# • Pole kwadratu 1 o ramieniu b.
# • Obwod kwadratu 1 o ramieniu b

def kwadrat(b):
    pole=b*b
    obwod=4*b
    print(pole,obwod)

kwadrat(20)