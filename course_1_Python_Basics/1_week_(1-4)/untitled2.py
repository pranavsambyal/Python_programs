# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 00:31:23 2019

@author: REBOOT
"""

a=input("Enter a string")
i=0
for i in a:
    i=i+1
    a[i]=str(int(a[i])+13)
    i=i+1
print(a)