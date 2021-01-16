import os

"""
 AppleScliptを実行するためのコマンド．
 何も指定しなければスクリプトエディタからの通知となってしまうが，with title　でタイトルを指定できる．
"""
a="この文章を表示したい"
os.system("osascript -e 'display notification \"{}\" with title \"todo.app\"'".format(a))
