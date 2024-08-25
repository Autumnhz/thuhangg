# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:24:11 2024

@author: student
"""

a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
A = (a**(1/2) - b**(1/2))
B = (a**(1/4) - b**(1/4))
C = ((a**(1/2)) + ((a*b)**(1/4)))
D = ((a**(1/4)) + (b**(1/4)))
k = (A/B) - (C/D)
print("Kết quả:", k)
