# -*- coding: utf-8 -*-

import tkinter as tk


root = tk.Tk()                # 窓を作る
root.title("ToDoリスト")   # 窓のタイトルを設定
root.geometry("640x480")      # 窓の大きさを設定

label = tk.Label(root, text="\n \n やっとtkinterが動きました")
label.pack()
root.mainloop()