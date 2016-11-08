#!/usr/bin/env python3
# coding: utf-8
def encrypt(message):
    message_crypted = ""
    for letter in message:
        inputnb =ord(letter)
        x = inputnb // 16
        y = inputnb % 16
        output = ((5*x-y)% 16)* 16 + ydir
        message_crypted +=chr(output)
    return message_crypted

def decrypt(message):
    message_crypted = ""
    for letter in message:
        inputnb =ord(letter)
        x = inputnb // 16
        y = inputnb % 16
        output = (13*(x + y) % 16) * 16 + y
        message_crypted +=chr( output)
    return message_crypted
message = "Algorythme" #1,wÿ©ôh / Algorythme
print(encrypt(message))
