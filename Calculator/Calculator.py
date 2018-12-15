from Tkinter import *

root = Tk()
root.title("Calculator")
Clear = True
current_LCD = ''

button_keys = {'Clear' : [1,0], '%' :[1,1], '+/-' : [1,2], '*' : [1,3], '9' : [2,0]
, '8' : [2,1], '7' : [2,2], '/' : [2,3], '6' : [3,0], '5' : [3,1], '4' : [3,2],
'+' : [3,3], '3' : [4,0], '2' : [4,1], '1' : [4,2], '-' : [4,3], '.' : [5,0],
'0' : [5,1], 'Ans' : [5,2], '=' : [5,3]} #Dictionary with all the keys and their location(row,column)

def LCD_display(key):
    global current_LCD
    global old_LCD
    global Clear
    if key == '=':
        old_LCD = str(eval(current_LCD))
        current_LCD = str(eval(current_LCD)) + '='
        Clear = False
    elif key == 'Clear':
        current_LCD = ''
        Clear = True
    elif key == '+/-' and Clear:
        current_LCD = current_LCD + '*(-1)'
    elif key == 'Ans' and Clear:
        current_LCD = current_LCD + old_LCD
    elif key == '%' and Clear:
        current_LCD = current_LCD + '/100.0'
    elif Clear:
        current_LCD = current_LCD + key


    calc_text = Label(root, text = current_LCD , height = 5, width = 30, relief = SOLID,
    bd = 10).grid(row = 0, columnspan = 4)


def misc_button(key, y, x):
    b = Button(root, text = key, width = 5, command = lambda : LCD_display(key)).grid(row = y, column = x)

for key in button_keys:
    misc_button(key, button_keys[key][0],button_keys[key][1])

calc_text = Label(root, text = current_LCD, height = 5, width = 30, relief = SOLID,
bd = 10).grid(row = 0, columnspan = 4)

root.mainloop()
