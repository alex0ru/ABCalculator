# А/В Калькулятор

import tkinter as tk
from tkinter import messagebox as mb


# Обработчик закрытия программы
def do_close():
    wMain.destroy()
    
# Обработка результатов
def do_processing():
    # Считывание данных из полей ввода
    n1 = int(entVisit.get())
    c1 = int(entConv.get())
    n2 = int(entVisit2.get())
    c2 = int(entConv2.get())
    
    # Проверка данных из полей ввода
    if n1 <= 0 or n2 <= 0:
        mb.showerror(title='Ошибка!', message='Количество посетителей должно быть больше 0 !')
        return
    
    # Открытие окна результатов
    popup_result(n1, c1, n2, c2)

# Добавление окна А/В Результат
def popup_result(n1, c1, n2, c2):
    wResult = tk.Toplevel()
    wResult.geometry('275x250')
    wResult.title('А/В Результат')
    
    # Кнопка закрытия окна
    btnClosePopup = tk.Button(wResult, text='Закрыть', font=('Helvetica', 10, 'bold'), command=wResult.destroy)
    btnClosePopup.place(y=200, x=150, width=90, height=30)
    
    # Установка фокуса на созданное окно
    wResult.focus_force()


# Создание главного окна программы
wMain = tk.Tk()
wMain.geometry('275x250')
wMain.title('А/В Калькулятор')

#-----
# Заголовок контрольной группы
lblTitle = tk.Label(text='Контрольная группа', font=('Helvetica', 14, 'bold'), fg='red')
lblTitle.place(y=10, x=10)

# Поля ввода
lblVisit = tk.Label(text='Посетители:', font=('Helvetica', 12, 'bold'), fg='red')
lblVisit.place(y=41, x=10)

entVisit = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entVisit.place(y=41, x=125, width=130, height=24)
entVisit.insert(tk.END, '0')

lblConv = tk.Label(text='Конверсии:', font=('Helvetica', 12, 'bold'), fg='red')
lblConv.place(y=70, x=10)

entConv = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entConv.place(y=70, x=125, width=130, height=20)
entConv.insert(tk.END, '0')

# Заголовок тестовой группы
lblTitle2 = tk.Label(text='Тестовая группа', font=('Helvetica', 14, 'bold'), fg='green')
lblTitle2.place(y=100, x=10)

# Поля ввода
lblVisit2 = tk.Label(text='Посетители:', font=('Helvetica', 12, 'bold'), fg='green')
lblVisit2.place(y=131, x=10)

entVisit2 = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entVisit2.place(y=131, x=125, width=130, height=20)
entVisit2.insert(tk.END, '0')

lblConv2 = tk.Label(text='Конверсии:', font=('Helvetica', 12, 'bold'), fg='green')
lblConv2.place(y=160, x=10)

entConv2 = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entConv2.place(y=160, x=125, width=130, height=20)
entConv2.insert(tk.END, '0')


#-----
# Кнопка "Рассчитать"
btnCalc = tk.Button(wMain, text='Рассчитать', font=('Helvetica', 10, 'bold'), command=do_processing)
btnCalc.place(y=200, x=30, width=90, height=30)

# Кнопка закрытия программы
btnClose = tk.Button(wMain, text='Закрыть', font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(y=200, x=150, width=90, height=30)

# Запуск цикла mainloop
wMain.mainloop()
