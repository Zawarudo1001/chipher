# -*- coding: cp1251 -*-

from random import randint, choice
from Utility import *
from math import *


def GenerateSuperRow()->list:
    row = []
    for k in range(8):
        row.append(sum(row) + randint(1,3))
    return row


def GenerateNormalRow(srow, N, M)->list:
    row = [(item * N) % M for item in srow]
    return row

SecKey = GenerateSuperRow()

m = sum(SecKey) + randint(1,20)
Nlist = []
for i in range(0, 1000):
    if gcd(m, i) == 1:
        Nlist.append(i)
n = choice(Nlist)

OpenKey = GenerateNormalRow(SecKey, n, m)


def KnapsackEncode(msg):
    encoded = []
    for letter in  msg:
        code = 0
        print(format(letter, "08b"))
        for j in range(8):
            print((letter % 2) * OpenKey[-(1+j)])
            code += (letter % 2) * OpenKey[-(1+j)]
            letter = letter // 2
        encoded.append(code)
    return encoded


def KnapsackDecode(msg):
    #msg хранит исходную шифрограмму
    samples = []
    n_1 = 0
    for u in range(0, m):
        if (n * u) % m == 1:
            n_1 = u
            break

    print("n^-1 =", n_1)
    word = []
    for letter in msg:
        word.append((letter * n_1) % m)
    print("Mod results : ", word)
    #word хранит результат деления по модулю. Осталось только упаковать рюкзак
    #это следует сделать при помощи закрытого ключа SecKey

    decoded = []
    #decoded в свою очередь хранит байты расшифрованного сообщения
    for number in word:
        temp = number
        s = 0
        for j in range(7, -1, -1):
            s = s // 2
            if SecKey[j] <= temp:
                temp -= SecKey[j]
                s += 128
        decoded.append(s)
        print(s, format(s, "08b"))
    return decoded

'''
SecKey = [2,3,6,13,27,52,105,210]
OpenKey = [62,93,168,403,417,352,315,210]
m = 420
n = 607
'''


print("SecuredKey : ", SecKey)
print("m = {}, n = {}".format(m, n))
print("OpenKey : ", OpenKey)

Message = Encode1251Char(input())
print("Message : ", Message)

ChipheredMessage = KnapsackEncode(Message)
print("ChipheredMessage : ", ChipheredMessage)


DecodedMessage = Decode1251Char(KnapsackDecode(ChipheredMessage))
print("DecodedMessage : ", DecodedMessage)