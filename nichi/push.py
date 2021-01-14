#push通知を送信するためのプログラム
import pickle #プログラムを実行し終えたあとも作成したオブジェクトを保存するモジュール．
import datetime 
import os

"""
 AppleScliptを実行するためのコマンド．
 何も指定しなければスクリプトエディタからの通知となってしまうが，with title　でタイトルを指定できる．
"""

dt_now = datetime.datetime.now() #日付
now_day = dt_now.day
#年year、月month、日day、時間hour、分minute、秒second、マイクロ秒microsecondを整数intで取得できる。dt_now.dayなど．
toDo_dic = {0:"", 1:"", 2:"", 3:"", 4: "", 5:"", 6:""} #初期valueは空白
date_dic = {0:31, 1:31, 2:31, 3:31, 4:31, 5:31, 6:31} #初期valueは31日
toDoNum = 7 #追加できるtoDoの数,task_entryの数に対応
with open('todo.pickle', 'rb') as f: #リード，バイナリ
    load_toDo_dic = pickle.load(f)
with open('date.pickle', 'rb') as f: #リード，バイナリ
    load_date_dic = pickle.load(f)
for i in range(toDoNum):
    toDo_dic[i] = load_toDo_dic[i]
    date_dic[i] = load_date_dic[i]

#print(date_dic) #{0: 9, 1: 11, 2: 12, 3: 31, 4: 31, 5: 31, 6: 31}
#print(toDo_dic) #{0: '1/9 :  OS 12', 1: '1/11 :  OS11', 2: '1/12 :  OS ', 3: '', 4: '', 5: '', 6: ''}
pushText = "以下のタスクの期限まで，残り1日です．\n"
#print("今日は{}日です．".format(now_day))
for i in range(toDoNum):
    input_day = date_dic[i]
    task = toDo_dic[i] #1/9 :  OS 12 keyが0,1,2なのでそのまま対応したvalueを取り出す．
    print(task)
    diff_Deadline = input_day - now_day #入力された期限と実際の期限の差
    #print(diff_Deadline)
    if diff_Deadline == 1: #1日前に通知を送る．
        pushText += task + "\n"
    
os.system("osascript -e 'display notification \"{$pushText}\" with title \"todo.app\"'")
