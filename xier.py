#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: bighu
# Created Time : 2021年11月27日 星期六 17时57分07秒
# File Name: xier.py
# Description: 希尔加密
"""
import numpy as np

class xier:
    def funTransStringToList(self,strdata):
        '''
        将字符串转换成int型数据并模26
        '''
        listData=[]
        # 便利这个字符串组
        for i in strdata:
            listData.append(ord(i)-97)
        return listData

    def funTransListToString_decode(self,listdata):
        '''
        将一个26以内的int列表转换成字符传(解密版)
        '''
        strData=""
        endData=listdata[-1]
        for i in listdata[:(len(listdata)+endData-2*self.n)]:
            strData+=chr(i+97)
        return strData

    def funTransListToString_encode(self,listdata):
        '''
        将一个26以内的int列表转换成字符传(加密版)
        '''
        strData=""
        for i in listdata:
            strData+=chr(i+97)
        return strData

    def funRepair(self,strdata):
        '''
        补位函数,参数位str字符串
        '''
        strlen=len(strdata)
        last=strlen%self.n
        for i in range(self.n-last+self.n-1):
            strdata+='a'
        strdata+=chr(last+97)
        return strdata
    
    def funMakeKey(self,listData):
        '''
        密钥产生函数
        listData:int列表
        '''
        allKey=[]
        for i in range(len(listData)):
            allKey.append(listData)
            listData=listData[1:]+listData[:1]
        return allKey

    def funvecPmatair(self,vec,mat,bdecode=False):
        '''
        向量乘矩阵
        '''
        tempvec = np.array(vec)
        tempmat= np.array(mat)
        if bdecode:
            tempmat=np.linalg.inv(mat)
        ans=[]
        for i in range(int(len(vec)/self.n)):
            temparr=tempvec[self.n*i:self.n*(i+1)] @ tempmat
            for j in range(self.n):
                ans.append(round(temparr[j]))
        return ans
    

    def funEncode(self,strdata):
        '''
        加密函数
        '''
        strdata=self.funRepair(strdata)
        Mcode=self.funvecPmatair(self.funTransStringToList(strdata),self.key)
        return self.funTransListToString_encode(Mcode)
    
    def funDecode(self,strdata):
        '''
        解密函数
        '''
        Ccode=self.funvecPmatair(self.funTransStringToList(strdata),self.key,True)
        return self.funTransListToString_decode(Ccode)

    def __init__(self,xeKey):
        '''
        通过密钥初始化部分函数
        '''
        keyList = self.funTransStringToList(xeKey)
        self.key = self.funMakeKey(keyList)
        self.n=len(keyList)

userKey = input("请输入本次加密或解密的密钥")
xe = xier(userKey)
message = input("请输入明文")
Mmess=xe.funEncode(message)
print(Mmess)
print(xe.funDecode(Mmess))

