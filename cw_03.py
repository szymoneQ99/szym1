# zadanie 1 -------------
from mimetypes import init

A = [1/x for x in range(1, 11)]
B = [2**i for i in range(11)]
C = [x for x in B if x % 4 == 0]

#print(A)
#print(B)
#print(C)

# zadanie 2 -----------

n = 4
a = [[i]*n for i in range(n)]
a[0][0] = 7
print(a)
b = a[0][0], a[1][1], a[2][2], a[3][3]
print(b)

# zadanie 3 -------------

#slownik = dict = {'ziemniaki': 'kg', 'chleb': 'szt', 'mleko 1l': 'szt', 'kawa': 'szt', 'winogrona': 'kg'}
#print(dict.values("szt"))


# zadanie 4 -------

import math

def monotonicznosc(a, b):
    if (a > 0):
        return print("Funkcja jest rosnąca")
    elif (a < 0):
        return print("Funkcja jest malejąca")
    else:
        return print("Funkcja jest stała")

print(monotonicznosc(2,4))
print(monotonicznosc(-2,4))
print(monotonicznosc(0,4))

# zadanie 5 -----------

import math
#a1 = input("Podaj cyfre a1: ")
#b1 = input("Podaj cyfre b1: ")
#a2 = input("Podaj cyfre a2: ")
#b2 = input("Podaj cyfre b2: ")
#if (int(a1) == int(a2)):
#    print("Proste sa rownolegle")
#elif (int(a1) * int(a2) == (-1)):
#    print("Proste sa prostopadle")
#else:  
#    print("Proste nie sa rownolegle ani  prostopadle")

# zadanie 6 ---------------

import math
from math import sqrt
x=2
y=3
a=6
b=4
wynik = ((x - a)**2) + ((y - b)**2)
print("Promien wynosi: " + str(sqrt(wynik)))

# zadanie 7 --------------

import math
a = 3
b = 4
przeciwprostokatna = (a**2 + b**2)
print("Przeciwprostokatna ma wartosc: " + str(sqrt(przeciwprostokatna)))

# zadanie 8 ---------------

a = 1
r = 1
ile = 10
liczby = range(1,10,1)
def ciag(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
        for i in liczby:
            suma += i
        return suma
print(ciag(1,2,3,4,5,6,7,8,9,10))

# zadanie 9 -------------------

a = 1
r = 1
ile = 10
liczby = range(1,10,1)
def ciag(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        suma = 1
        for i in liczby:
            suma *= i
        return suma
print(ciag(1,2,3,4,5,6,7,8,9,10))

# zadanie 10 --------------


def lista_zakupow(** lista):
    for co in lista:
        print("Ilosc produktow ")
        print(co)
        print(" kupuje")
        print(lista[co])
        lista_zakupow = (ziemniaki-"5", mleko-"2", chleb-"3")

