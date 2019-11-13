import tkinter
from tkinter import *


global textvariable

def btn_clicked(numbers):
	global operator
	operator = operator + str(numbers)
	text_input.set(operator)

def clear_display():
	global operator
	operator = ''
	text_input.set('')


def btn_equals():
        try:
                global operator
                sum_up = str(eval(operator))
                intr = str(sum_up)
                text_input.set(intr)
                operator = ''
        except ZeroDivisionError:
                err = "Divided By Zero!!"
                text_input.set(err)
        except ValueError:
                err2 = 'Value Error'
                text_input.set(err2)
        except SyntaxError:
                err3 = "Syntax Error"
                text_input.set(err3)





root = tkinter.Tk()
root.geometry('250x400+300+300')
root.resizable(0,0)
root.title('Calculator')
root.iconbitmap(r'C:/Users/dell/Desktop/script/calc.ico')

operator = ""
text_input = StringVar()



entry1 =Entry(
	root,
	justify = 'right',
	font = ('verdana', 20),
	textvariable = text_input,
	bg = '#ffffff',
	fg = '#000000',
)


entry1.pack(expand = True, fill = 'both')

row_1 = Frame(root)
row_1.pack(expand = True, fill = 'both')

row_2 = Frame(root)
row_2.pack(expand = True, fill = 'both')

row_3 = Frame(root)
row_3.pack(expand = True, fill = 'both')

row_4 = Frame(root)
row_4.pack(expand = True, fill = 'both')



button_1 = Button(
	row_1,
	text = "7",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(7)
)
button_1.pack(side = 'left', expand = True, fill = 'both')


button_2 = Button(
	row_1,
	text = "8",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(8)
)
button_2.pack(side = 'left', expand = True, fill = 'both')

button_3 = Button(
	row_1,
	text = "9",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(9)
)
button_3.pack(side = 'left', expand = True, fill = 'both')

button_mult = Button(
	row_1,
	text = "*",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked('*')
)
button_mult.pack(side = 'left', expand = True, fill = 'both')



button_4 = Button(
	row_2,
	text = "4",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(4)
)
button_4.pack(side = 'left', expand = True, fill = 'both')


button_5 = Button(
	row_2,
	text = "5",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(5)
)
button_5.pack(side = 'left', expand = True, fill = 'both')

button_6 = Button(
	row_2,
	text = "6",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(6)
)
button_6.pack(side = 'left', expand = True, fill = 'both')



button_minus = Button(
	row_2,
	text = "-",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked('-')
)
button_minus.pack(side = 'left', expand = True, fill = 'both')




button_7 = Button(
	row_3,
	text = "1",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(1)
)
button_7.pack(side = 'left', expand = True, fill = 'both')


button_8 = Button(
	row_3,
	text = "2",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(2)
)
button_8.pack(side = 'left', expand = True, fill = 'both')

button_9 = Button(
	row_3,
	text = "3",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked(3)
)
button_9.pack(side = 'left', expand = True, fill = 'both')

button_plus = Button(
	row_3,
	text = "+",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked('+')
)
button_plus.pack(side = 'left', expand = True, fill = 'both')



button_c = Button(
	row_4,
	text = "C",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = clear_display
)
button_c.pack(side = 'left', expand = True, fill = 'both')


button_0 = Button(
	row_4,
	text = "0",
	relief = 'groove',
	border = 0,
	font = ('verdana', 22),
	command = lambda : btn_clicked(0)
	
)
button_0.pack(side = 'left', expand = True, fill = 'both')



button_div = Button(
	row_4,
	text = "/",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = lambda : btn_clicked('/')
)
button_div.pack(side = 'left', expand = True, fill = 'both')

button_equal = Button(
	row_4,
	text = "=",
	font = ('verdana', 22),
	relief = 'groove',
	border = 0,
	command = btn_equals
)
button_equal.pack(side = 'left', expand = True, fill = 'both')


root.mainloop()
