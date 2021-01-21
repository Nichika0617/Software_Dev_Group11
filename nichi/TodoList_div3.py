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
from collections import OrderedDict
import cronpi #定時にpush通知を送信するプログラムを実行


os.chdir(os.path.dirname(__file__))#画像ファイルと同じディレクトリへ

#新規ウィンドウ作成
root = tkinter.Tk()
root.title(u"todo_app")
root.geometry("800x450")

#main_frameの設定
main_frame = tkinter.Frame(width=800,height=450)
main_frame.grid(row=0, column=0, sticky="nsew")#frameを重ねる

#背景画像
#ファイルを参照．ppmファイルなら表示可能
main_back = tkinter.PhotoImage(file="cat.ppm")
#画像の大きさを調整
canvas = tkinter.Canvas(main_frame,bg="black", width=800, height=450)
#画像の位置を設定
canvas.place(x=0, y=0)
#画像を表示する
canvas.create_image(0, 0, image=main_back, anchor=tkinter.NW)

changePageButton = tkinter.Button(main_frame, text="ToDoリスト",width=10,height=5, command=lambda : changePage(frame1))
changePageButton.place(x=350,y=350)

#frame1の設定
frame1 = tkinter.Frame(width=800,height=450)
frame1.grid(row=0, column=0, sticky="nsew")
frame1.propagate(0)
changePageButton = tkinter.Button(frame1, text="back", command=lambda : changePage(main_frame))
changePageButton.place(x=740,y=0)


#背景画像
#ファイルを参照．ppmファイルなら表示可能
back = tkinter.PhotoImage(file="watercolor.ppm")
#画像の大きさを調整
canvas = tkinter.Canvas(frame1,bg="black", width=400, height=400)
#画像の位置を設定
canvas.place(x=0, y=0)
#画像を表示する
canvas.create_image(0, 0, image=back, anchor=tkinter.NW)


staticfont = font.Font(family="Helvetica",size=20,weight="bold",) #フォント作成
month = dt_now.month
static = tkinter.Label(frame1,text=str(month)+"月のToDoリスト",font = staticfont,foreground='#6595ed') #起動した月を表示
#年year、月month、日day、時間hour、分minute、秒second、マイクロ秒microsecondを整数intで取得できる。dt_now.dayなど．
static.place(x=120, y=10)
textBox = tkinter.Label(frame1,text="ToDoタスクを入力↓↓",font = staticfont,foreground='#ffa500')
textBox.place(x=500, y=10)
Explanation = "入力\n追加したいタスクを入力して\n[タスクを追加]ボタンをクリックすると，\nToDoリストに上から順番に追加されます．\n\n削除\n消したいタスクの番号のみを入力して，\n[タスクの削除]ボタンをクリックすると\nその番号のタスクを消すことができます．"
Explanation_font = font.Font(family="Helvetica",size=15,weight="bold") #フォント作成
useExplanation = tkinter.Label(frame1,text=Explanation,font = Explanation_font,foreground='#66cdaa')
useExplanation.place(x=450, y=120)

#番号をkey,toDoをvalueとして辞書化　→　{0:toDo1, 1: toDo2, 2:toDo3, 3:toDo4, 4:toDo, 5:toDo, 6:toDo} #7個の番号はtask_entry[i]に対応させている
toDo_dic = {0:"", 1:"", 2:"", 3:"", 4: "", 5:"", 6:""} #初期valueは空白
#番号をkey,日付をvalueとして辞書化　 →  {0:date1, 1:date2, 2:date3, 3:date4, 4:date5, 5:date6, 6:date7} 
date_dic = {0:31, 1:31, 2:31, 3:31, 4:31, 5:31, 6:31} #初期valueは31日
toDoNum = 7 #追加できるtoDoの数,task_entryの数に対応

def AddTask():
    inputText1 = textBox.get() #toDoを読み込み
    inputText1_1 = task_deadline.get() #締め切りを読み込み
    error_count = 0
    if len(inputText1) <= 1: #toDoが1文字以下ならエラー
        tkMessageBox.showinfo('エラー',"タスクが短すぎます．正しく入力されているか確認してください．\n入力されたタスク↓↓\n　「 " + str(textBox.get())+" 」")
        textBox.delete("0","end") #テキストボックスの内容を削除
        error_count = 1
    else:
        try:
            inputText1_2 = int(inputText1_1)
        except ValueError:
            tkMessageBox.showinfo('エラー',"数字を入力してください.\n入力された期限↓↓\n　「 " + str(task_deadline.get())+" 」")
            error_count = 1
    if len(inputText1_1) >= 3 or inputText1_2 <=0 or inputText1_2 >= 32:
        if error_count != 1: #まだエラーが出ていないならば，(エラー連続表示を防ぐため．)
            tkMessageBox.showinfo('エラー',"入力できる範囲は1〜31です.\n入力された期限↓↓\n　「 " + str(task_deadline.get())+" 」")
            error_count = 1
    elif error_count == 0: #エラーが一つもなければエントリーボックスへ出力
        for i in range(toDoNum): #toDoNum個のエントリーボックスの中身を調べる,toDoNumは7個(task_entryの数)
            if task_entry[i].get() == '':#task_entry[i]の中身が空だったら
                task_entry[i].configure(state="normal")
                inputTask = str(dt_now.month) + "/" + inputText1_1 +" "+ ":" + " " + inputText1
                task_entry[i].insert(tkinter.END,inputTask) #task_entry[i]へ挿入
                task_entry[i].configure(state="readonly") #追加したタスクを書き換えられないように．
                toDo_dic[i] = inputTask    #辞書にtoDo追加
                date_dic[i] = inputText1_2 #辞書に日付追加
                textBox.delete("0","end") #テキストボックスの内容を削除
                task_deadline.delete("0","end")#日付入力ボックスの内容を削除
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
        toDo_dic[inNum-1] = "" #辞書のkey=iに対応するvalueを初期化
        date_dic[inNum-1] = 32 


def check(event):
    text = ""
    for i in range(toDoNum):    
        if Val[i].get() == True:
            text += str(i+1)+"を達成!\n"
            task_entry[i].configure(state="normal")
            task_entry[i].delete("0","end")
            task_entry[i].configure(state="readonly")
            toDo_dic[i] = "" #辞書のkey=iに対応するvalueを初期化
            date_dic[i] = 32
        else:
            text +=  str(i+1)+"未達成.\n"
    tkMessageBox.showinfo('タスク状況',text)

def QuitApp():
    root.destroy()

def store():
    with open('todo.pickle', 'wb') as f: #w書き込みモード,bバイナリモード
        pickle.dump(toDo_dic,f)
    with open('date.pickle', 'wb') as f: #w書き込みモード,bバイナリモード
        pickle.dump(date_dic,f)
    tkMessageBox.showinfo('保存完了',"ファイル「todo.pickle」,「date.pickle」にタスクを保存しました．")    

def LoadData():
    with open('todo.pickle', 'rb') as f: #リード，バイナリ
        load_toDo_dic = pickle.load(f)
    with open('date.pickle', 'rb') as f: #リード，バイナリ
        load_date_dic = pickle.load(f)
    for i in range(toDoNum):
        task_entry[i].configure(state="normal")
        task_entry[i].delete("0","end")
        task_entry[i].insert(tkinter.END,load_toDo_dic[i]) #task_entryへtoDoを出力
        task_entry[i].configure(state="readonly")
        toDo_dic[i] = load_toDo_dic[i]
        date_dic[i] = load_date_dic[i]
"""
Pythonでは、変数のスコープが代入の有無で変わる
関数内で代入されている：変数は関数内のローカルスコープに決定
関数内で代入されていない：変数はグローバルスコープに決定
らしい。。
"""

def dateSort():
    i = 0
    sorted_toDo_dic =  {0:"", 1:"", 2:"", 3:"", 4: "", 5:"", 6:""}
    sorted_date_dic = OrderedDict(sorted(date_dic.items(), key=lambda x:x[1])) #date_dicをvalueでsort
    for k, v in sorted_date_dic.items():
        sorted_toDo_dic[i] = toDo_dic[k] 
        date_dic[i] = v #ソートされた日付を昇順でいれる
        i += 1
    i = 0
    for i in range(toDoNum):
        toDo_dic[i] = sorted_toDo_dic[i] #関数内で作ったsorted_toDo_dicをグローバルなtoDo_dicへ反映させる
        task_entry[i].configure(state="normal")
        task_entry[i].delete("0","end")
        task_entry[i].insert(tkinter.END,toDo_dic[i]) #task_entryへtoDoを出力
        task_entry[i].configure(state="readonly")

def changePage(page):
    '''
    画面遷移用の関数
    '''
    page.tkraise()

#チェックボックス
box,CheckBox,Val={},{},{}
for i in range(toDoNum):
    Val[i] = tkinter.BooleanVar()
    #Val[i].set(False)
    CheckBox[i] = tkinter.Checkbutton(frame1,variable=Val[i])
    CheckBox[i].place(x=20,y=50+(i*40))
    box[i] = tkinter.Label(frame1,text=str(i+1))
    box[i].place(x=0,y=50+(i*40))

#タスク確認ボタン
button1 = tkinter.Button(frame1,text="タスク確認",width=30)
button1.bind("<Button-1>",check)
button1.place(x=60, y=350)


#タスク追加ボタン
add_buttom = tkinter.Button(frame1,text="タスクを追加",width=15,command=lambda : AddTask())
add_buttom.place(x=630, y=350)

#タスク削除ボタン
#delete_buttom = tkinter.Button(root,text="タスクを削除",width=15,command=partial(AddTask,-1))
delete_buttom = tkinter.Button(frame1,text="タスクを削除",width=10,command=lambda : DeleteTask())
delete_buttom.place(x=420, y=350)

#保存ボタン
store_buttom = tkinter.Button(frame1,text="保存",width=10,command=lambda : store())
store_buttom.place(x=680, y=420)

#終了ボタン
quit_buttom = tkinter.Button(frame1,text="終了",width=10,command=lambda : QuitApp())
quit_buttom.place(x=550, y=420)

#ロードボタン
load_buttom = tkinter.Button(frame1,text="ロード",width=10,command=lambda : LoadData())
load_buttom.place(x=420, y=420)

#ソートボタン
sort_buttom = tkinter.Button(frame1,text="日付順に並び替え",width=30,command=lambda : dateSort())
sort_buttom.place(x=60, y=420)


time = "5:10pm"

cronpi.run_every_day("python3 /Users/e195765/Desktop/2年講義/ソフトウェア開発演習/group11/Software_Dev_Group11/nichi/push.py").on(time)
print("タスク終了1日前の{}に通知を送信します．".format(time))


# エントリー(右側のテキストボックス)
textBox = tkinter.Entry(frame1,width=40)
textBox.place(x=420, y=50)
textBox.insert(tkinter.END,"ここにタスクを入力して，[追加]ボタンでタスクを追加")
# エントリー(期限入力)
task_deadline = tkinter.Entry(frame1,width=30)
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
    task_entry[i] = tkinter.Entry(frame1,width=35,)
    task_entry[i].place(x=50, y=50+(i*40))
    task_entry[i].configure(state='readonly')
"""
元のやつ
task1_entry = tkinter.Entry(width=35)
task1_entry.place(x=40, y=50)
task1_entry.configure(state='readonly')
task2_entry = tkinter.Entry(width=35)
task2_entry.place(x=40, y=90)
task2_entry.configure(state='readonly')
"""
################################################

main_frame.tkraise()#最初に出てくるframeを設定
#メインループ
root.mainloop()

