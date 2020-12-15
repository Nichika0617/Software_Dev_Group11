# -*- coding: utf-8 ^*^
from tkinter import messagebox as tkMessageBox
import sys
import tkinter
import os

os.chdir(os.path.dirname(__file__))

#画面表示
root = tkinter.Tk()
#背景画像

#ファイルを参照
back = tkinter.PhotoImage(file="watercolor.ppm")
#画像の大きさを調整
canvas = tkinter.Canvas(bg="black", width=400, height=400)

#画像の位置を設定
canvas.place(x=0, y=0)

#画像を表示する
canvas.create_image(0, 0, image=back, anchor=tkinter.NW)
#ウィンドウの名前を設定
root.title("todo_app")

#ウィンドウの大きさを設定
root.geometry("400x400")

static = tkinter.Label(root,text="Lets programming your life")
static.place(x=120, y=10)

#ボタンに機能をつける関数
def check(event):
    global Val1
    global Val2
    global Val3
    global Val4
    global Val5
    global Val6
    global Val7

    text=""

    if Val1.get() == True:
        text += "1 is OK!\n"
    else:
        text += "You forgot checking 1.\n"

    if Val2.get() == True:
        text += "2 is OK!\n"
    else:
        text += "You forgot checking 2.\n"

    if Val3.get() == True:
        text += "3 is OK!\n"
    else:
        text += "You forgot checking 3.\n"

    if Val4.get() == True:
        text += "4 is OK!\n"
    else:
        text += "You forgot checking 4.\n"

    if Val5.get() == True:
        text += "5 is OK!\n"
    else:
        text += "You forgot checking 5.\n"

    if Val6.get() == True:
        text += "6 is OK!\n"
    else:
        text += "You forgot checking 6.\n"

    if Val7.get() == True:
        text += "7 is OK!\n"
    else:
        text += "You forgot checking 7.\n"

    tkMessageBox.showinfo('info',text)

#チェックボックス
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val3 = tkinter.BooleanVar()
Val4 = tkinter.BooleanVar()
Val5 = tkinter.BooleanVar()
Val6 = tkinter.BooleanVar()
Val7 = tkinter.BooleanVar()

CheckBox1 = tkinter.Checkbutton(variable=Val1)
CheckBox1.place(x=0, y=50)

CheckBox2 = tkinter.Checkbutton(variable=Val2)
CheckBox2.place(x=0, y=90)

CheckBox3 = tkinter.Checkbutton(variable=Val3)
CheckBox3.place(x=0, y=130)

CheckBox4 = tkinter.Checkbutton(variable=Val4)
CheckBox4.place(x=0, y=170)

CheckBox5 = tkinter.Checkbutton(variable=Val5)
CheckBox5.place(x=0, y=210)

CheckBox6 = tkinter.Checkbutton(variable=Val6)
CheckBox6.place(x=0, y=250)

CheckBox7 = tkinter.Checkbutton(variable=Val7)
CheckBox7.place(x=0, y=290)

#ボタン
button1 = tkinter.Button(root, text=u'check',width=30)
button1.bind("<Button-1>",check)
button1.place(x=180, y=350)



#文章で言うところの句読点みたいなものなので忘れずに。
root.mainloop()

