# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:39:35 2024

@author: Student
"""

y = int(input("Nhập năm sinh:"))
if y >= 0:
    n = 2024
    t = n - y
    print("Tuổi", t)
else:
    print("Không hợp lệ.")