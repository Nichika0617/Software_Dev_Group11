#-*- coding: utf8 -*-
from tkinter import messagebox as tkMessageBox
from tkinter import font
import sys
import tkinter
import datetime
dt_now = datetime.datetime.now() #日付
from functools import partial #ボタンコマンドに引数を渡す
import pickle #プログラムを実行し終えたあとも作成したオブジェクトを保存するモジュール．
import os

os.chdir(os.path.dirname(__file__))#画像ファイルと同じディレクトリへ

#処理はこの間に書く．
#新規ウィンドウ作成
root = tkinter.Tk()
#背景画像
#ファイルを参照．ppmファイルなら表示可能
back = tkinter.PhotoImage(file="watercolor.ppm")
#画像の大きさを調整
canvas = tkinter.Canvas(bg="black", width=400, height=400)
#画像の位置を設定
canvas.place(x=0, y=0)
#画像を表示する
canvas.create_image(0, 0, image=back, anchor=tkinter.NW)

#ウィンドウの名前を設定
root.title(u"todo_app")
#ウィンドウの大きさを設定
root.geometry("800x450")
staticfont = font.Font(family="Helvetica",size=20,weight="bold",) #フォント作成
month = dt_now.month
static = tkinter.Label(root,text=str(month)+"月のToDoリスト",font = staticfont,foreground='#6595ed') #起動した月を表示
#年year、月month、日day、時間hour、分minute、秒second、マイクロ秒microsecondを整数intで取得できる。dt_now.dayなど．
static.place(x=120, y=10)
textBox = tkinter.Label(root,text="ToDoタスクを入力↓↓",font = staticfont,foreground='#ffa500')
textBox.place(x=500, y=10)
Explanation = "入力\n追加したいタスクを入力して\n[タスクを追加]ボタンをクリックすると，\nToDoリストに上から順番に追加されます．\n\n削除\n消したいタスクの番号のみを入力して，\n[タスクの削除]ボタンをクリックすると\nその番号のタスクを消すことができます．"
Explanation_font = font.Font(family="Helvetica",size=15,weight="bold") #フォント作成
useExplanation = tkinter.Label(root,text=Explanation,font = Explanation_font,foreground='#66cdaa')
useExplanation.place(x=450, y=120)

dic_toDo = {}
deadline_list = [0,0,0,0,0,0,0]
toDoNum = 7 #追加できるtoDoの数

def AddTask():
    inputText1 = textBox.get()
    inputText1_1 = task_deadline.get()
    error_count = 0
    try:
        inputText1_2 = int(inputText1_1)
    except ValueError:
        tkMessageBox.showinfo('エラー',"数字を入力してください.\n入力された期限↓↓\n　「 " + str(task_deadline.get())+" 」")
        error_count = 1
    if len(inputText1) <= 1:
        tkMessageBox.showinfo('エラー',"タスクが短すぎます．正しく入力されているか確認してください．\n入力されたタスク↓↓\n　「 " + str(textBox.get())+" 」")
        textBox.delete("0","end") #テキストボックスの内容を削除
        error_count = 1
    elif error_count == 0:
        for i in range(toDoNum):
            if task_entry[i].get() == '':#task_entry[i]の中身が空だったら
                task_entry[i].configure(state="normal")
                inputTask = str(dt_now.month) + "/" + inputText1_1 +" "+ ":" + " " + inputText1
                task_entry[i].insert(tkinter.END,inputTask)
                task_entry[i].configure(state="readonly") #追加したタスクを書き換えられないように．
                textBox.delete("0","end") #テキストボックスの内容を削除
                break
            elif i == (toDoNum-1):#task_entry[i]の中身がiの範囲全て空ではない場合
                tkMessageBox.showinfo('エラー',"これ以上追加できません．リストからタスクを削除してください．")
            
def DeleteTask():
    inNum = textBox.get()
    if inNum == "1" or  inNum == "2" or inNum == "3" or inNum == "4" or inNum == "5" or inNum == "6" or inNum == "7":
        inNum = int(inNum)
        textBox.delete("0", "end")
        task_entry[inNum-1].configure(state="normal")
        task_entry[inNum-1].delete("0","end")
        task_entry[inNum-1].configure(state="readonly")




#チェックボックス
box = {}
CheckBox = {}
Val = {}
for i in range(toDoNum):
    Val[i] = tkinter.BooleanVar()
    Val[i].set(False)
    CheckBox[i] = tkinter.Checkbutton(variable=Val[i])
    CheckBox[i].place(x=20,y=50+(i*40))
    box[i] = tkinter.Label(root,text=str(i+1))
    box[i].place(x=0,y=50+(i*40))
"""

Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
CheckBox1 = tkinter.Checkbutton(variable=Val1)
CheckBox1.place(x=10, y=50)
box1 = tkinter.Label(root,text="1")
box1.place(x=0, y=50)
CheckBox2 = tkinter.Checkbutton(variable=Val2)
CheckBox2.place(x=10, y=90)
box2 = tkinter.Label(root,text="2")
box2.place(x=0, y=90)
"""


#タスク確認ボタン
button1 = tkinter.Button(text="タスク確認",width=30)
button1.bind("<Button-1>")
button1.place(x=60, y=350)

#タスク追加ボタン
add_buttom = tkinter.Button(text="タスクを追加",width=15,command=AddTask)
add_buttom.config(bg="#F0F8FF")
add_buttom.place(x=630, y=350)

#タスク削除ボタン
#delete_buttom = tkinter.Button(root,text="タスクを削除",width=15,command=partial(AddTask,-1))
delete_buttom = tkinter.Button(text="タスクを削除",width=10,command=DeleteTask)
delete_buttom.place(x=420, y=350)

#閉じるボタン
quit_buttom = tkinter.Button(text="終了",width=10)
quit_buttom.place(x=680, y=420)

#ロードボタン
load_buttom = tkinter.Button(text="ロード",width=10)
load_buttom.place(x=420, y=420)

# エントリー(右側のテキストボックス)
textBox = tkinter.Entry(width=40)
textBox.place(x=420, y=50)
textBox.insert(tkinter.END,"ここにタスクを入力して，[追加]ボタンでタスクを追加")
# エントリー(期限入力)
task_deadline = tkinter.Entry(width=30)
task_deadline.place(x=480, y=80)
task_deadline.insert(tkinter.END,"ここに期限を入力  例(1/7日なら'7'と入力)")
"""
print("追加したいタスクを入力してください") #ターミナルで日本語入力
inText = input()
textBox.insert(0,inText) #0文字目から
"""

#タスクを表示する用のエントリー(左側の閲覧用テキストボックス)
task_entry = {}
for i in range(toDoNum):
    task_entry[i] = tkinter.Entry(width=35)
    task_entry[i].place(x=50, y=50+(i*40))
    task_entry[i].configure(state='readonly')
"""
task1_entry = tkinter.Entry(width=35)
task1_entry.place(x=40, y=50)
task1_entry.configure(state='readonly')
task2_entry = tkinter.Entry(width=35)
task2_entry.place(x=40, y=90)
task2_entry.configure(state='readonly')
"""
################################################

#メインループ
root.mainloop()