#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:21:49 2018

@author: liuchuang


图像识别

"""


import pyautogui 


a=pyautogui.locateOnScreen('symbol5.png')


print(a)

b=pyautogui.center(a)

print(b)

pyautogui.doubleClick(b)
