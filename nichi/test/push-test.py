import os
#import cronpi
#import tkinter
#import sys

"""
 AppleScliptを実行するためのコマンド．
 何も指定しなければスクリプトエディタからの通知となってしまうが，with title　でタイトルを指定できる．
"""
message =  "期限ですよ〜"


os.system("osascript -e 'display notification \"{}\"'".format(message))



