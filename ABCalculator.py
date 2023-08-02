# А/В Калькулятор

import tkinter as tk


# Обработчик закрытия программы
def do_close():
    wMain.destroy()

# Добавление окна А/В Результат
def popup_result():
    wResult = tk.Toplevel()
    wResult.geometry('275x250')
    wResult.title('А/В Результат')
    
    # Кнопка закрытия окна
    btnClosePopup = tk.Button(wResult, text='Закрыть', font=('Helvetica', 10, 'bold'), command=wResult.destroy)
    btnClosePopup.place(y=200, x=150, width=90, height=30)


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

entVisit = tk.Entry(font=('Helvetica', 12, 'bold'))
entVisit.place(y=41, x=125, width=130, height=24)

lblConv = tk.Label(text='Конверсии:', font=('Helvetica', 12, 'bold'), fg='red')
lblConv.place(y=70, x=10)

entConv = tk.Entry(font=('Helvetica', 12, 'bold'))
entConv.place(y=70, x=125, width=130, height=20)

# Заголовок тестовой группы
lblTitle2 = tk.Label(text='Тестовая группа', font=('Helvetica', 14, 'bold'), fg='green')
lblTitle2.place(y=100, x=10)

# Поля ввода
lblVisit2 = tk.Label(text='Посетители:', font=('Helvetica', 12, 'bold'), fg='green')
lblVisit2.place(y=127, x=10)

entVisit2 = tk.Entry(font=('Helvetica', 12, 'bold'))
entVisit2.place(y=127, x=125, width=130, height=20)

lblConv2 = tk.Label(text='Конверсии:', font=('Helvetica', 12, 'bold'), fg='green')
lblConv2.place(y=154, x=10)

entConv2 = tk.Entry(font=('Helvetica', 12, 'bold'))
entConv2.place(y=154, x=125, width=130, height=20)


#-----
# Кнопка "Рассчитать"
btnCalc = tk.Button(wMain, text='Рассчитать', font=('Helvetica', 10, 'bold'), command=popup_result)
btnCalc.place(y=200, x=30, width=90, height=30)

# Кнопка закрытия программы
btnClose = tk.Button(wMain, text='Закрыть', font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(y=200, x=150, width=90, height=30)

# Запуск цикла mainloop
wMain.mainloop()
