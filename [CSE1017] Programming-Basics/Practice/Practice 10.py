from tkinter import *

class MainWindow() :
    def __init__(self) :
        self.__master = Tk()
        self.__master.title("변환기")
        self.__master.geometry("350x320")
        self.__master.resizable(False, False)

        self.frame = Frame(self.__master)
        self.frame.pack(padx=10, pady=10)

        self.create_widgets()

    def entry_set_text(entry, text) :
        entry.delete(0, END)
        entry.insert(0, text)
        return

    def clear_entrys(*entrys) :
        for x in entrys :
            x.delete(0, END)

    def create_widgets(self) :
        self.text_celsius = Label(self.frame, text="섭씨")
        self.text_fahrenheit = Label(self.frame, text="화씨")
        self.text_celsius.grid(row=0, column=0, padx=2)
        self.text_fahrenheit.grid(row=0, column=1, padx=2)

        self.entry_celsius = Entry(self.frame, width=15)
        self.entry_fahrenheit = Entry(self.frame, width=15)
        self.entry_celsius.grid(row=1, column=0, padx=2)
        self.entry_fahrenheit.grid(row=1, column=1, padx=2)

        self.button_clear_1 = Button(self.frame, text="지우기", width=10, command=lambda: MainWindow.clear_entrys(self.entry_celsius, self.entry_fahrenheit))
        self.button_clear_1.grid(row=1, column=2, padx=2)

        self.button_ctof = Button(self.frame, text="변환", width=7, command=lambda: self.ctof(self.entry_celsius, self.entry_fahrenheit))
        self.button_ctof.grid(row=2, column=0, padx=2)
        self.button_ftoc = Button(self.frame, text="변환", width=7, command=lambda: self.ftoc(self.entry_celsius, self.entry_fahrenheit))
        self.button_ftoc.grid(row=2, column=1, padx=2)


        spacer = Frame(self.frame)
        spacer.grid(row=3, column=0, pady=10)


        self.text_centimeter = Label(self.frame, text="센티미터")
        self.text_feet = Label(self.frame, text="피트")
        self.text_centimeter.grid(row=4, column=0, padx=2)
        self.text_feet.grid(row=4, column=1, padx=2)

        self.entry_centimeter = Entry(self.frame, width=15)
        self.entry_feet = Entry(self.frame, width=15)
        self.entry_centimeter.grid(row=5, column=0, padx=2)
        self.entry_feet.grid(row=5, column=1, padx=2)

        self.button_clear_2 = Button(self.frame, text="지우기", width=10, command=lambda: MainWindow.clear_entrys(self.entry_centimeter, self.entry_feet))
        self.button_clear_2.grid(row=5, column=2, padx=2)

        self.button_cmtoft = Button(self.frame, text="변환", width=7, command=lambda: self.cmtoft(self.entry_centimeter, self.entry_feet))
        self.button_cmtoft.grid(row=6, column=0, padx=2)
        self.button_fttocm = Button(self.frame, text="변환", width=7, command=lambda: self.fttocm(self.entry_centimeter, self.entry_feet))
        self.button_fttocm.grid(row=6, column=1, padx=2)


        spacer = Frame(self.frame)
        spacer.grid(row=7, column=0, pady=10)


        self.text_kilogram = Label(self.frame, text="킬로그램")
        self.text_pound = Label(self.frame, text="파운드")
        self.text_kilogram.grid(row=8, column=0, padx=2)
        self.text_pound.grid(row=8, column=1, padx=2)

        self.entry_kilogram = Entry(self.frame, width=15)
        self.entry_pound = Entry(self.frame, width=15)
        self.entry_kilogram.grid(row=9, column=0, padx=2)
        self.entry_pound.grid(row=9, column=1, padx=2)

        self.button_clear_3 = Button(self.frame, text="지우기", width=10, command=lambda: MainWindow.clear_entrys(self.entry_kilogram, self.entry_pound))
        self.button_clear_3.grid(row=9, column=2, padx=2)

        self.button_kgtolb = Button(self.frame, text="변환", width=7, command=lambda: self.kgtolb(self.entry_kilogram, self.entry_pound))
        self.button_kgtolb.grid(row=10, column=0, padx=2)
        self.button_lbtokg = Button(self.frame, text="변환", width=7, command=lambda: self.lbtokg(self.entry_kilogram, self.entry_pound))
        self.button_lbtokg.grid(row=10, column=1, padx=2)

        self.button_quit = Button(self.frame, text="종료", width=10, command=self.frame.quit)
        self.button_quit.grid(row=11, column=2, padx=2, pady=10)


    def ctof(self, entry_c, entry_f) :
        if entry_c.get().isdigit() or (entry_c.get() != "" and entry_c.get()[0] == '-' and entry_c.get()[1:].isdigit()) :
            MainWindow.entry_set_text(entry_f, str(int((int(entry_c.get()) * 1.8) + 32))) #소수점 버림
            #MainWindow.entry_set_text(entry_f, str(round((int(entry_c.get()) * 1.8) + 32, 1)))
        else :
            entry_f.delete(0, END)

    def ftoc(self, entry_c, entry_f) :
        if entry_f.get().isdigit() or (entry_f.get() != "" and entry_f.get()[0] == '-' and entry_f.get()[1:].isdigit()) :
            MainWindow.entry_set_text(entry_c, str(int((int(entry_f.get()) - 32) / 1.8))) #소수점 버림
            #MainWindow.entry_set_text(entry_c, str(round((int(entry_f.get()) - 32) / 1.8, 1)))
        else :
            entry_c.delete(0, END)

    def cmtoft(self, entry_cm, entry_ft) :
        if entry_cm.get().isdigit() or (entry_cm.get() != "" and entry_cm.get()[0] == '-' and entry_cm.get()[1:].isdigit()) :
            MainWindow.entry_set_text(entry_ft, str(round(int(entry_cm.get()) * 0.03281, 1)))
        else :
            entry_ft.delete(0, END)

    def fttocm(self, entry_cm, entry_ft) :
        if entry_ft.get().isdigit() or (entry_ft.get() != "" and entry_ft.get()[0] == '-' and entry_ft.get()[1:].isdigit()) :
            MainWindow.entry_set_text(entry_cm, str(round(int(entry_ft.get()) * 30.48, 1)))
        else :
            entry_cm.delete(0, END)

    def kgtolb(self, entry_kg, entry_lb) :
        if entry_kg.get().isdigit() or (entry_kg.get() != "" and entry_kg.get()[0] == '-' and entry_kg.get()[1:].isdigit()) :
            MainWindow.entry_set_text(entry_lb, str(round(int(entry_kg.get()) * 2.2046, 1)))
        else :
            entry_lb.delete(0, END)

    def lbtokg(self, entry_kg, entry_lb) :
        if entry_lb.get().isdigit() or (entry_lb.get() != "" and entry_lb.get()[0] == '-' and entry_lb.get()[1:].isdigit()) :
            MainWindow.entry_set_text(entry_kg, str(round(int(entry_lb.get()) * 0.4536, 1)))
        else :
            entry_kg.delete(0, END)

    def start_main_loop(self) :
        self.__master.mainloop()

    def get_master(self) :
        return self.__master

main = MainWindow()
main.start_main_loop()