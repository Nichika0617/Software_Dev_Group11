# -*- coding: utf-8 ^*^
import tkinter as tk

class App:
    def _init_(self):
        #ウインドを初期化
        self.master = tk.Tk()
        self.master.title('TODOアプリ')
        self.master.geometry('400*300')

    def mainloop(self):
        #masterに処理を以上
        self.master.mainloop()

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()