# -*- coding: cp1251 -*-

from random import randint, choice
from math import *
from Utility import *


def factNum(n)->list:
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n//i)
    divs.pop(1)     #находим только собственны делатели числа
    return divs


def getFundRoot(p)->int:
    Pdivs = factNum(p-1)
    for g in range(2, p):
        t = True
        for num in Pdivs:
            if (g**num - 1) % p == 0:
                t = False
                break
        if t:
            return g
    return -1


def ElGamalEncode(msg, y, g, k, p):
    chiphered = []
    t = 0
    for letter in msg:
        chiphered.append( ((g**k[t])%p, (y**k[t])*letter%p ) )
        t += 1
    return chiphered


def ElGamalDecode(msg, x):
    decoded = []
    for letter in msg:  #для каждого кортежа зашифрованной последовательностси
        a, b = letter[0], letter[1]
        T = b * a**(p-1-x) % p
        decoded.append(T)
    return decoded


p = choice(listOfSimpleNumbers)
g = getFundRoot(p)
x = randint(1, p-1)
y = (g**x) % p


print(p, g, x, y)
# открытый ключ - p,g,y; закрытый ключ - x
Message = EncodeToAlph(Encode1251Char(input()))
print(Message)
k = [randint(2, p - 2) for i in range(len(Message))]
#k = 7
#выберем случайое k для каждого отдельного блока

ChipheredMessage = ElGamalEncode(Message, y, g, k, p)
print(ChipheredMessage)


DecodedMessage = ElGamalDecode(ChipheredMessage, x)
print(DecodedMessage)


Answer = Decode1251Char(DecodeFromAlph(DecodedMessage))
print(Answer)



