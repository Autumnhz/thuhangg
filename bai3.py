# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:57:04 2024

@author: Student
"""

n = int(input("N = "))
if n >= 10 and n <= 99:
    pd = n%10
    pn = n//10
    S = pd + pn
    print("Kết quả:", S)
else:
    print("Không hợp lệ.")
    