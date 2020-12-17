#-*- coding: utf8 -*-
from tkinter import messagebox as tkMessageBox
from tkinter import font
import sys
import tkinter
import datetime
dt_now = datetime.datetime.now() #日付
from functools import partial #ボタンコマンドに引数を渡す
import os

os.chdir(os.path.dirname(__file__))#画像ファイルと同じディレクトリへ

task_list = [0,0,0,0,0,0,0]
#タスクを追加する関数
def AddTask(num):
    taskfont = font.Font(family="Times New Roman",size=15) #フォント作成
    #inputText = textBox.get("1.0","end-1c") #1行めの0文字目からテキストボックスの終わりまで．
    #end-01cでは最後まで読み，最後の改行を削除．"END"のみでは駄目．
    i = 0
    try:
        while True:
            if task_list[i] == 0: #最初は0番目が0 = タスクが一つもないならば，一番上にタスクを表示．2番目が0なら，3番目が0なら・・
                if i+1 == 1: # i は配列にも対応するため0から始まる．＋1してタスク数と同じように．
                    inputText1 = textBox.get()
                    print(inputText1+"を，タスク"+str(i+1)+"に追加します．")
                    task1 = tkinter.Label(root,text=inputText1,font=taskfont)
                    task1.place(x=40, y=50+40*i)
                    #task1.place_forget()
                elif i+1 == 2:
                    inputText2 = textBox.get()
                    print(inputText2+"を，タスク"+str(i+1)+"に追加します．")
                    task2 = tkinter.Label(root,text=inputText2,font=taskfont)
                    task2.place(x=40, y=50+40*i)
                elif i+1 == 3:
                    inputText3 = textBox.get()
                    print(inputText3+"を，タスク"+str(i+1)+"に追加します．")
                    task3 = tkinter.Label(root,text=inputText3,font=taskfont)
                    task3.place(x=40, y=50+40*i)
                elif i+1 == 4:
                    inputText4 = textBox.get()
                    print(inputText4+"を，タスク"+str(i+1)+"に追加します．")
                    task4 = tkinter.Label(root,text=inputText4,font=taskfont)
                    task4.place(x=40, y=50+40*i)
                elif i+1 == 5:
                    inputText5 = textBox.get()
                    print(inputText5+"を，タスク"+str(i+1)+"に追加します．")
                    task5 = tkinter.Label(root,text=inputText5,font=taskfont)
                    task5.place(x=40, y=50+40*i)
                elif i+1 == 6:                
                    inputText6 = textBox.get()
                    print(inputText6+"を，タスク"+str(i+1)+"に追加します．")
                    task6 = tkinter.Label(root,text=inputText6,font=taskfont)
                    task6.place(x=40, y=50+40*i)
                elif i+1 == 7:
                    inputText7 = textBox.get()
                    print(inputText7+"を，タスク"+str(i+1)+"に追加します．")
                    task7 = tkinter.Label(root,text=inputText7,font=taskfont)
                    task7.place(x=40, y=50+40*i)
                task_list[i] = 1
                textBox.delete("0","end") #テキストボックスの内容を削除
                break
            else:
                i+=1
    except IndexError:
        tkMessageBox.showinfo('エラー',"これ以上追加できません．リストからタスクを削除してください．")
        print("タスクが全部埋まっています．")

def DeleteTask():
    inNum = textBox.get()
    if inNum == "1" or  inNum == "2" or inNum == "3" or inNum == "4" or inNum == "5" or inNum == "6" or inNum == "7":
        inNum = int(inNum)
        task_list[inNum-1] = 0 #配列の0番目がタスクの1番目 削除するので0とする
        print(str(inNum) + "番のタスクを削除します")
        textBox.delete("0", "end")
        space = "                         　　　　　　　　                                        "
        hide_space = tkinter.Label(root,text=space)#削除するのではなく，巨大は空白で隠す．
        hide_space.place(x=40, y=50+40*(inNum-1))
        textBox.delete("0", "end")
    else:
        textBox.delete("0", "end")
        print("番号"+str(inNum)+"に追加されているタスクはありません．")
        tkMessageBox.showinfo('エラー',"指定された番号のタスクを見つけることができませんでした．\n1~7の数字で指定してください．")
        
    


#ウィンドウを閉じる関数
def QuitApp():
    print("アプリを終了します．")
    root.destroy()

#チェックする関数
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
        text += "1 を達成!\n"
    else:
        text += "1 未達成.\n"

    if Val2.get() == True:
        text += "2 を達成!\n"
    else:
        text += "2 未達成.\n"

    if Val3.get() == True:
        text += "3 を達成!\n"
    else:
        text += "3 未達成.\n"

    if Val4.get() == True:
        text += "4 を達成!\n"
    else:
        text += "4 未達成.\n"

    if Val5.get() == True:
        text += "5 を達成!\n"
    else:
        text += "5 未達成.\n"

    if Val6.get() == True:
        text += "6 を達成!\n"
    else:
        text += "6 未達成.\n"

    if Val7.get() == True:
        text += "7 を達成!\n"
    else:
        text += "7 未達成.\n"

    tkMessageBox.showinfo('タスク状況',text)


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
staticfont = font.Font(family="Helvetica",size=20,weight="bold") #フォント作成
month = dt_now.month
static = tkinter.Label(root,text=str(month)+"月のToDoリスト",font = staticfont) #起動した月を表示
#年year、月month、日day、時間hour、分minute、秒second、マイクロ秒microsecondを整数intで取得できる。dt_now.dayなど．
static.place(x=120, y=10)
textBox = tkinter.Label(root,text="ToDoタスクを入力↓↓",font = staticfont)
textBox.place(x=500, y=10)
Explanation = "入力\n追加したいタスクを入力して\n[タスクを追加]ボタンをクリックすると，\nタスクリストに上から順番に追加されます．\n\n削除\n消したいタスクの番号のみを入力して，\n[タスクの削除]ボタンをクリックすると\nその番号のタスクを消すことができます．"
Explanation_font = font.Font(family="Helvetica",size=15,weight="bold") #フォント作成
useExplanation = tkinter.Label(root,text=Explanation,font = Explanation_font)
useExplanation.place(x=450, y=120)

"""
textBox = tkinter.Text(root,wrap=tkinter.CHAR,width=55)
'''
wrap=tk.NONE にすると、テキストが折り返しされない
wrap=tk.CHAR で文字単位でテキストが折り返される。
wrap=tk.WORD で単語単位でテキストが折り返される．
今回は文字単位のCHAR
'''
textBox.place(relx=0.505, rely=0.1)
root.columnconfigure(0, weight=1) #テキストボックスをウィンドウサイズに合わせて伸縮させる．
root.rowconfigure(0, weight=1)#テキストボックスをウィンドウサイズに合わせて伸縮させる．
"""

#チェックボックス
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val3 = tkinter.BooleanVar()
Val4 = tkinter.BooleanVar()
Val5 = tkinter.BooleanVar()
Val6 = tkinter.BooleanVar()
Val7 = tkinter.BooleanVar()

CheckBox1 = tkinter.Checkbutton(variable=Val1)
CheckBox1.place(x=10, y=50)
box1 = tkinter.Label(root,text="1")
box1.place(x=0, y=50)

CheckBox2 = tkinter.Checkbutton(variable=Val2)
CheckBox2.place(x=10, y=90)
box2 = tkinter.Label(root,text="2")
box2.place(x=0, y=90)

CheckBox3 = tkinter.Checkbutton(variable=Val3)
CheckBox3.place(x=10, y=130)
box3 = tkinter.Label(root,text="3")
box3.place(x=0, y=130)

CheckBox4 = tkinter.Checkbutton(variable=Val4)
CheckBox4.place(x=10, y=170)
box4 = tkinter.Label(root,text="4")
box4.place(x=0, y=170)

CheckBox5 = tkinter.Checkbutton(variable=Val5)
CheckBox5.place(x=10, y=210)
box5 = tkinter.Label(root,text="5")
box5.place(x=0, y=210)

CheckBox6 = tkinter.Checkbutton(variable=Val6)
CheckBox6.place(x=10, y=250)
box6 = tkinter.Label(root,text="6")
box6.place(x=0, y=250)

CheckBox7 = tkinter.Checkbutton(variable=Val7)
CheckBox7.place(x=10, y=290)
box7 = tkinter.Label(root,text="7")
box7.place(x=0, y=290)

#タスク確認ボタン
button1 = tkinter.Button(root, text="タスク確認",width=30)
button1.bind("<Button-1>",check)
button1.place(x=60, y=350)

#タスク追加ボタン
add_buttom = tkinter.Button(root,text="タスクを追加",width=15,command=partial(AddTask,1))
add_buttom.place(x=630, y=350)

#タスク削除ボタン
#delete_buttom = tkinter.Button(root,text="タスクを削除",width=15,command=partial(AddTask,-1))
delete_buttom = tkinter.Button(root,text="タスクを削除",width=15,command=DeleteTask)
delete_buttom.place(x=420, y=350)

#閉じるボタン
quit_buttom = tkinter.Button(root,text="終了",width=10,command=QuitApp)
quit_buttom.place(x=680, y=420)

# エントリー(テキストボックス)
textBox = tkinter.Entry(width=30)
textBox.place(x=470, y=50)
"""
print("追加したいタスクを入力してください") #ターミナルで日本語入力
inText = input()
textBox.insert(0,inText) #0文字目から
"""

#メインループ
root.mainloop()