# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:41:32 2019

@author: ASUS
"""

import tkinter as tk  # 使用Tkinter前需要先導入

window = tk.Tk() 
window.title('My Window') 


def hit_me():
    imageshow = tk.PhotoImage(file="test.png")
    photo.configure(image=imageshow)
    window.mainloop()

 
b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.grid(row=0,column=0)
photo = tk.Label(window)
photo.grid(row=0,column=1)
 
window.mainloop()
