# А/В Калькулятор

import tkinter as tk
from tkinter import messagebox as mb
import os
import math
from scipy.stats import norm


# Обработчик закрытия программы
def do_close():
    wMain.destroy()

# Функция форматирования процентов
def num_percent(num):
    return('{:.2f}'.format(num*100).rjust(10)+'%')

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
    wResult.geometry('500x500')
    wResult.title('А/В Результат')
    
    # Поле вывода текста
    txtOutput = tk.Text(wResult, font=('Helvetica', 10, 'bold'),)
    txtOutput.place(y=80, x=10, width=480, height=370)
    
    # Заголовок поля вывода текста
    txtOutput.insert(tk.END, 60*' '+'Контрольная'+10*' '+'Тестовая'+os.linesep)
    txtOutput.insert(tk.END, 60*' '+'группа'+21*' '+'группа'+os.linesep)
    txtOutput.insert(tk.END, 119*'-'+os.linesep)
    
    # Вывод конверсии и стандартного отклонения
    p1 = c1/n1
    p2 = c2/n2
    txtOutput.insert(tk.END, 'Конверсия'+37*' '+num_percent(p1)+16*' '+num_percent(p2)+os.linesep)
    sigma1 = math.sqrt(p1*(1-p1)/n1)
    sigma2 = math.sqrt(p2*(1-p2)/n2)
    txtOutput.insert(tk.END, 'Стандартное отклонение'+12*' '+num_percent(sigma1)+18*' '+num_percent(sigma2)+os.linesep)
    
    # Возможный разброс
    z1 = 1.96
    
    low1_95 = p1 - z1 * sigma1
    if low1_95 < 0:
        low1_95 = 0
    upp1_95 = p1 + z1 * sigma1
    if upp1_95 > 1:
        upp1_95 = 1
    
    low2_95 = p2 - z1 * sigma2
    if low2_95 < 0:
        low2_95 = 0
    upp2_95 = p2 + z1 * sigma2
    if upp2_95 > 1:
        upp2_95 = 1
    
    txtOutput.insert(tk.END, 119*'-'+os.linesep)
    txtOutput.insert(tk.END, '95%-возможный разброс'+os.linesep)
    txtOutput.insert(tk.END, 37*' '+'От:'+12*' '+num_percent(low1_95)+16*' '+num_percent(low2_95)+os.linesep)
    txtOutput.insert(tk.END, 37*' '+'До:'+12*' '+num_percent(upp1_95)+16*' '+num_percent(upp2_95)+os.linesep)
    
    z2 = 2.575
    
    low1_99 = p1 - z2 * sigma1
    if low1_99 < 0:
        low1_99 = 0
    upp1_99 = p1 + z2 * sigma1
    if upp1_99 > 1:
        upp1_99 = 1
    
    low2_99 = p2 - z2 * sigma2
    if low2_99 < 0:
        low2_99 = 0
    upp2_99 = p2 + z2 * sigma2
    if upp2_99 > 1:
        upp2_99 = 1
    
    txtOutput.insert(tk.END, 119*'-'+os.linesep)
    txtOutput.insert(tk.END, '99%-возможный разброс'+os.linesep)
    txtOutput.insert(tk.END, 37*' '+'От:'+12*' '+num_percent(low1_99)+16*' '+num_percent(low2_99)+os.linesep)
    txtOutput.insert(tk.END, 37*' '+'До:'+12*' '+num_percent(upp1_99)+16*' '+num_percent(upp2_99)+os.linesep)
    
    # Вычисление Z и P
    txtOutput.insert(tk.END, 119*'-'+os.linesep)
    
    z_score = (p2 - p1)/math.sqrt(sigma1*sigma1+sigma2*sigma2)
    txtOutput.insert(tk.END, 'Z = '+'{:.7f}'.format(z_score)+os.linesep)
    
    p_value = norm.sf(x=z_score, loc=0, scale=1)
    txtOutput.insert(tk.END, 'P = '+'{:.7f}'.format(p_value)+os.linesep)
    
    # Оценка результатов
    confidence_95 = False
    if p_value < 0.025 or p_value > 0.975:
        confidence_95 = True                # 95% (p = 2.5%)
    
    confidence_99 = False
    if p_value < 0.005 or p_value > 0.995:
        confidence_99 = True                # 99% (p = 0.5%)
    
    lblComment95 = tk.Label(wResult, text='95%-уверенность:', font=('Helvetica', 10, 'bold'))
    lblComment95.place(y=15, x=10)
    
    if confidence_95:
        lblResult95 = tk.Label(wResult, text='Да', font=('Helvetica', 12, 'bold'), fg='green')
        lblResult95.place(y=15, x=150)
    else:
        lblResult95 = tk.Label(wResult, text='Нет', font=('Helvetica', 12, 'bold'), fg='red')
        lblResult95.place(y=15, x=150)
    
    lblComment99 = tk.Label(wResult, text='99%-уверенность:', font=('Helvetica', 10, 'bold'))
    lblComment99.place(y=40, x=10)
    
    if confidence_99:
        lblResult99 = tk.Label(wResult, text='Да', font=('Helvetica', 12, 'bold'), fg='green')
        lblResult99.place(y=40, x=150)
    else:
        lblResult99 = tk.Label(wResult, text='Нет', font=('Helvetica', 12, 'bold'), fg='red')
        lblResult99.place(y=40, x=150)
    
    # Кнопка закрытия окна
    btnClosePopup = tk.Button(wResult, text='Закрыть', font=('Helvetica', 10, 'bold'), command=wResult.destroy)
    btnClosePopup.place(y=460, x=205, width=90, height=30)
    
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
entVisit.insert(tk.END, '0') # предустановленное значение 255

lblConv = tk.Label(text='Конверсии:', font=('Helvetica', 12, 'bold'), fg='red')
lblConv.place(y=70, x=10)

entConv = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entConv.place(y=70, x=125, width=130, height=20)
entConv.insert(tk.END, '0') # предустановленное значение 26

# Заголовок тестовой группы
lblTitle2 = tk.Label(text='Тестовая группа', font=('Helvetica', 14, 'bold'), fg='green')
lblTitle2.place(y=100, x=10)

# Поля ввода
lblVisit2 = tk.Label(text='Посетители:', font=('Helvetica', 12, 'bold'), fg='green')
lblVisit2.place(y=131, x=10)

entVisit2 = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entVisit2.place(y=131, x=125, width=130, height=20)
entVisit2.insert(tk.END, '0') # предустановленное значение 235

lblConv2 = tk.Label(text='Конверсии:', font=('Helvetica', 12, 'bold'), fg='green')
lblConv2.place(y=160, x=10)

entConv2 = tk.Entry(font=('Helvetica', 12, 'bold'), justify='center')
entConv2.place(y=160, x=125, width=130, height=20)
entConv2.insert(tk.END, '0') # предустановленное значение 18


#-----
# Кнопка "Рассчитать"
btnCalc = tk.Button(wMain, text='Рассчитать', font=('Helvetica', 10, 'bold'), command=do_processing)
btnCalc.place(y=200, x=30, width=90, height=30)

# Кнопка закрытия программы
btnClose = tk.Button(wMain, text='Закрыть', font=('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(y=200, x=150, width=90, height=30)

# Запуск цикла mainloop
wMain.mainloop()
