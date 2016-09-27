#!usr/bin/python3
import string
def reversed_string(a_string):
    return a_string[::-1]
rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

src = """))vc.ugnz * 4( * )ablne* ablne((gavec
))":rerucf ny rq ablne ry mregaR"(ghcav(gnbys = ablne
 ugnz gebczv"""
exec(reversed_string(string.translate(src,rot13)))
