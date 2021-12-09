#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: bighu
# Created Time : 2021年12月02日 星期四 17时16分48秒
# File Name: paillier.py
# Description: paillier密码
"""
import gmpy2 as gy
import random
import libnum

class Paillier(object):
    def __init__(self, pubKey=None, priKey=None):
        self.pubKey = pubKey
        self.priKey = priKey

    def __gen_prime__(self, p):
        while not gy.is_prime(p):
            p += 1
        return p
    
    def funL(self, x, n):
        '''
        L函数
        '''
        res = gy.div((x - 1), n)
        return res
    
    def funmakeKey(self):
        while True:
            rs = random.randint(10**30,10**31)
            rb = random.randint(10**30,10**31)
            p = self.__gen_prime__(rs)
            q = self.__gen_prime__(rb)
            n = p * q
            lmd =(p - 1) * (q - 1)
            if gy.gcd(n, lmd) == 1:
                break
        g = n + 1
        mu = gy.invert(lmd, n)
        self.pubKey = [n, g]
        self.priKey = [lmd, mu]
        return
        
    def decipher(self, ciphertext):
        n, g = self.pubKey
        lmd, mu = self.priKey
        m =  self.funL(gy.powmod(ciphertext, lmd, n ** 2), n) * mu % n
        plaintext = libnum.n2s(int(m))
        return plaintext

    def encipher(self, plaintext):
        m = libnum.s2n(plaintext)
        n, g = self.pubKey
        r = random.randint(2,n)
        while gy.gcd(n, r)  != 1:
            r += 1
        ciphertext = gy.powmod(g, m, n ** 2) * gy.powmod(r, n, n ** 2) % (n ** 2)
        return ciphertext

if __name__ == "__main__":
    pai = Paillier()
    pai.funmakeKey()
    pubKey = pai.pubKey
    print("公钥：",pubKey)
    plaintext = input("请输入要加密的数据: ")
    ciphertext = pai.encipher(plaintext)
    print("密文为：", ciphertext)
    deciphertext = pai.decipher(ciphertext)
    print("解密后得到: ",deciphertext)
