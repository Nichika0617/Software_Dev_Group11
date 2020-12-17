# -*- coding: utf-8 -*-
import tkinter as tk
import sys

#ウィンドウ
window = tk.Tk()
window.title(u'TODOリスト')
window.geometry('500x500')

#ラベル
label1 = tk.Label(text=u'タスクを入力')
label1.pack()

#ボックス
entry = tk.Entry(width=30)
entry.insert(tk.END, u'挿入する文字列')
entry.pack()

#ボタンが押されたら呼び出される関数
def addList(text):
    ListBox1.insert(tk.END, text)

def deleteSelectedList():
    selectedIndex = tk.ACTIVE
    ListBox1.delete(selectedIndex)

#追加ボタン
button_add = tk.Button(text=u'add',width=10, command=lambda: addList(entry.get()))
button_add.pack()

#削除ボタン
button_delete = tk.Button(text=u'done',width=10, command=lambda: deleteSelectedList())
button_delete.pack()

#リストボックス
ListBox1 = tk.Listbox(width=55, height=15)
ListBox1.pack()


window.mainloop()