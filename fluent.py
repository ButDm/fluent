# 13 - 7

import tkinter
import tkinter.messagebox
#price = [500.0, 300.0, 700.0, 1000.0, 800.0, 1300.0, 1300.0]

class MYGUI():
    def __init__(self):

#        self.price = price
        self.main_window = tkinter.Tk()
        self.main_window.title('GUI Python')
        self.main_window.geometry('340x180')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)
        self.rb1 = tkinter.Radiobutton(self.main_window,
                            text="Дневное время (с 6:00 до 17:59)",
                            font='13', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.main_window,
                            text="Вечернее время (с 18:00 до 23:59)",
                            font='13', variable=self.radio_var, value=2)

        self.rb3 = tkinter.Radiobutton(self.main_window,
                            text="Непиковый период (с полуночи до 05:59)",
                            font='13', variable=self.radio_var, value=3)
        self.rb1.place(x=10, y=20)
        self.rb2.place(x=10, y=50)
        self.rb3.place(x=10, y=80)


#        self.top_frame.pack()

#        self.button1 = tkinter.Button(self.bottom_frame,
#                                    text='Посчитать стоимость работ',
#                                    command=self.calculate_total)
#        self.button2 = tkinter.Button(self.bottom_frame, text='Выход',
#                                    command=self.main_window.destroy)

        self.label = tkinter.Label(self.main_window,
                        text='Введите количество минут', font='13')
        self.entry = tkinter.Entry(self.main_window, width=10, font='13')

        self.label.place(x=10, y=110)
        self.entry.place(x=220, y=110)


        self.button1 = tkinter.Button(self.bottom_frame,
                                    text='Посчитать стоимость', font='13',
                                    command=self.calculate_total)
        self.button2 = tkinter.Button(self.bottom_frame,
                                text='Выход', font='13',
                                command=self.main_window.destroy)
#        self.button1.pack(side='left')
#        self.button2.pack(side='left')
        self.button1.pack(side='left')
        self.button2.pack(side='left')

        self.bottom_frame.pack(side='bottom')

#        tkinter.mainloop()
        self.main_window.mainloop()

    def calculate_total(self):
        print('111')
        self.total = 0.0
        self.prices = [10, 12, 5]
        self.str_total = ''

#        self.price = [500.0, 300.0, 700.0, 1000.0, 800.0, 1300.0, 1300.0]
        if self.radio_var.get() == 1:
            print(self.prices[0])
            print(int(self.entry.get()))

            self.total = self.prices[0] * int(self.entry.get())
            self.str_total += "Дневное время (с 6:00 до 17:59)" +\
                                "\nТариф: " +\
                                str(self.prices[0]) + '  руб.\n'
        elif self.radio_var.get() == 2:
            self.total = self.prices[1] * int(self.entry.get())
            self.str_total += "Вечернее время (с 18:00 до 23:59)" +\
                                "\nТариф: " +\
                                str(self.prices[1]) + '  руб.\n'
        elif self.radio_var.get() == 3:
            self.total = self.prices[2] * int(self.entry.get())
            self.str_total += "Непиковый период (с полуночи до 05:59)" +\
                                "\nТариф: " +\
                                str(self.prices[2]) + '  руб.\n'


        print(self.str_total + '\n' + 'Общая сумма = ' + str(self.total))

        tkinter.messagebox.showinfo('', self.str_total +
                        'Общая сумма затрат = '+ str(self.total))

my_gui = MYGUI()


