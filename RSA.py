# -*- coding: cp1251 -*-

from math import *
from random import sample, choice
from Utility import *


def EylerFunction(p, q):
    return (p - 1) * (q - 1)


'''
RSA �� ����� ����������� ����� ������ ��� phi, ���� ��������� ��������� �����, 
������ ����� ������������ ���������, �������� ��� ������ 3 � 5, ��� ��� ���� �������� ������ ��� 15.
������� �� ������� ������� ������� ����� ���� �������������� ������ ��� �������� ����� 17
(��� ��� ���� �������� �������� �������� � windows-1251 ���������� � 210 ���������� ������������ - 256)
'''

p, q = sample(tinylistOfSimpleNumbers, 2)       #������� ��� ��������� ������� �����

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
    #���� ��������� ������ �����, ������� ������ ���� �������� � cp1251
    for i in range(len(word)):
        word[i] = (word[i]**pubKeyE) % n
    return word


def RsaDecode(word):
    #���� ��������� ������ ������������� ����� �������� � cp1251
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


#print(Decode1251Char(Encode1251Char('������� �������� ����������')))