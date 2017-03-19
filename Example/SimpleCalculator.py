# 간단한 이항 계산 프로그램
#
# 작성자: 강민석
# 작성날짜: 2017년 3월 19일 (version 1.0)
#-*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

def entrySetText(entry, text) :
    entry.delete(0,END)
    entry.insert(0,text)
    return

def isNumber(str) :
    result=False

    try:
        float(str)
        result=2
        int(str)
        result=1
    except :
        None

    return result

def validate(action, text) :
    if action == '0' or text == "." or text == "-" or text == "+" or 0 < isNumber(text):
        return True
    else :
        return False

class MainWindow() :
    master = None

    def __init__(self) :
        self.master = Tk()

        frame = ttk.Frame(self.master)
        frame.pack()

        self.master.title("Simple Calculator")

        vcmd = (self.master.register(validate), '%d', '%P')
        self.num1 = ttk.Entry(frame, validate = 'key', validatecommand = vcmd)
        self.num2 = ttk.Entry(frame, validate = 'key', validatecommand = vcmd)
        self.result = ttk.Entry(frame)

        self.text_num1 = ttk.Label(frame, text="NUM 1")
        self.text_num2 = ttk.Label(frame, text="NUM 2")
        self.text_equal = ttk.Label(frame, text="=")

        self.quit = ttk.Button(frame,
        text="Quit", width=15,
        command=frame.quit)

        self.add = ttk.Button(frame,
        text="+", width=15,
        command=self.add)

        self.sub = ttk.Button(frame,
        text="-", width=15,
        command=self.sub)

        self.mul = ttk.Button(frame,
        text="*", width=15,
        command=self.mul)

        self.div = ttk.Button(frame,
        text="/", width=15,
        command=self.div)

        self.text_num1.grid(row=0, column=0)
        self.text_num2.grid(row=1, column=0)
        self.text_equal.grid(row=2, column=0)
        self.num1.grid(row=0, column=1)
        self.num2.grid(row=1, column=1)
        self.result.grid(row=2, column=1)
        self.add.grid(row=0, column=2)
        self.sub.grid(row=0, column=3)
        self.mul.grid(row=1, column=2)
        self.div.grid(row=1, column=3)
        self.quit.grid(row=2, column=3)

    def add(self) :
        num1 = self.num1.get()
        num2 = self.num2.get()

        if isNumber(num1) == 0 or isNumber(num2) == 0 :
            entrySetText(self.result, "ERROR")
        elif isNumber(num1) == 1 and isNumber(num2) == 1 :
            entrySetText(self.result, str(int(num1) + int(num2)))
        else :
            entrySetText(self.result, str(float(num1) + float(num2)))
    
    def sub(self) :
        num1 = self.num1.get()
        num2 = self.num2.get()

        if isNumber(num1) == 0 or isNumber(num2) == 0 :
            entrySetText(self.result, "ERROR")
        elif isNumber(num1) == 1 and isNumber(num2) == 1 :
            entrySetText(self.result, str(int(num1) - int(num2)))
        else :
            entrySetText(self.result, str(float(num1) - float(num2)))
        
    def mul(self) :
        num1 = self.num1.get()
        num2 = self.num2.get()

        if isNumber(num1) == 0 or isNumber(num2) == 0 :
            entrySetText(self.result, "ERROR")
        elif isNumber(num1) == 1 and isNumber(num2) == 1 :
            entrySetText(self.result, str(int(num1) * int(num2)))
        else :
            entrySetText(self.result, str(float(num1) * float(num2)))
        
    def div(self) :
        num1 = self.num1.get()
        num2 = self.num2.get()

        if isNumber(num1) == 0 or isNumber(num2) == 0 :
            entrySetText(self.result, "ERROR")
        elif isNumber(num1) == 1 and isNumber(num2) == 1 :
            entrySetText(self.result, str(int(num1) / int(num2)))
        else :
            entrySetText(self.result, str(float(num1) / float(num2)))

    def startMainLoop(self) :
        self.master.mainloop()

    def getMaster(self) :
        return self.master

main = MainWindow()
main.startMainLoop()