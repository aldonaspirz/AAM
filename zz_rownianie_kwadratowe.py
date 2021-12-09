import math
import numpy as np
from numpy.lib.function_base import append


plik = open('dw.txt','r')
dane=plik.read()
dane3=dane.split(',',3)
dane4=[]
for i in dane3:
    i=int(i)
    dane4.append(i)
print(dane4)

a=dane4[0]
b=dane4[1]
c=dane4[2]



def rownanie_kwadratowe(a,b,c):

    if a!=0:
        delta=b*b-4*a*c
        if delta>0:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)
           
            return x1,x2
   

        
        
        if delta<0:
            pass
        if delta==0:
            x=-b/(2*a)
            return x
    else:
         pass
            

wynik=rownanie_kwadratowe(dane4[0],dane4[1],dane4[2])

print(wynik)
listax=[]



print(np.linspace(wynik[0], wynik[1], num=5))
listax=np.linspace(wynik[0], wynik[1], num=5)


listay=[]
a=dane4[0]
b=dane4[1]
c=dane4[2]
for i in listax:

        y=a*i*i+b*i+c
        print(i)
        listay.append(y)
        print(listay)
plik = open('dw1.txt','w')
listaxy=(listay)+ (listax)
plik.write(str(listaxy))

for index in range(len(listax)):
    plik.write(str(listax[index]) + " " + str(listay[index]) + "\n")
plik.close()

import matplotlib
import matplotlib.pyplot as plt

plt.plot(listax, listay)
plt.legend('y=ax')
plt.title('Wykres funkcji kwadratowej')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('plot.png', dpi=300)
plt.grid()
plt.tight_layout()
plt.show()


