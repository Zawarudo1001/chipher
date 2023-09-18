# -*- coding: cp1251 -*-

from math import *
from random import sample, choice
from Utility import *


def EylerFunction(p, q):
    return (p - 1) * (q - 1)


'''
RSA не может зашифровать число больше чем phi, если выберутся небольшие числа, 
нельзя будет расшифровать результат, например при числах 3 и 5, так как коды символов больше чем 15.
Поэтому из таблицы выборки простых чисел были предварительно убраны все значения менее 17
(так как коды символов русского алфавита в windows-1251 начинаются с 210 наименьшее произведение - 256)
'''

p, q = sample(tinylistOfSimpleNumbers, 2)       #возьмем два различных простых числа

n = p * q
phi = EylerFunction(p, q)
print("p = {}, q = {}, n = {}, phi = {}".format(p, q, n, phi))

pubKeyE = 0
Esamples = []
for k in range(0, n):
    if gcd(k, phi) == 1:
        Esamples.append(k)
pubKeyE = choice(Esamples)
print("Public key E =", pubKeyE)


SecKeyD = 0
for j in range(0, phi):
    if (j * pubKeyE) % phi == 1:
        SecKeyD = j
        break
print("Public key D =", SecKeyD)


def RsaEncode(word):
    #сюда поступает массив чисел, которые хранят коды символов в cp1251
    for i in range(len(word)):
        word[i] = (word[i]**pubKeyE) % n
    return word


def RsaDecode(word):
    #сюда послупает массив зашифрованных кодов символов в cp1251
    for j in range(len(word)):
        word[j] = (word[j]**SecKeyD) % n
    return word


Message = EncodeToAlph(Encode1251Char(input()))
print(Message)

ChipheredMessage = RsaEncode(Message)
print(ChipheredMessage)

DecodedMessage = RsaDecode(Message)
print(DecodedMessage)

Answer = Decode1251Char(DecodeFromAlph(DecodedMessage))
print(Answer)


#print(Decode1251Char(Encode1251Char('ТИМОХИН ВЯЧЕСЛАВ МАКСИМОВИЧ')))