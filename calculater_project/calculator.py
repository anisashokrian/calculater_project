from tkinter import *


def button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        result.set(eval(result.get()))

    elif len(result.get()) < 8:
      result.set(result.get() + button_text)



window = Tk()
window.geometry("300x330")
window.title("Calculator")

buttons =  [#why comma after []?
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "+"]
 ]

result = StringVar()
Entry(window, textvariable=result, width= 20, state= "readonly", font=("Arial", 40)).place(x=0, y=0)

x_dict = 70
y_dict = 60
btn_width = 7
btn_height = 2

for row in range(4):
    for col in range(4):
        text = buttons[row][col]
        #window?
        btn = Button(window, text=text, width=btn_width, height=btn_height)
        btn.bind("<Button-1>", button_click)
        btn.place(x=20+col*x_dict, y=80+row*y_dict)

    print()












window.mainloop()