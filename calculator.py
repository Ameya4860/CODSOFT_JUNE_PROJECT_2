from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")
root.geometry("570x750+100+200")
root.resizable(False,False )
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
    label_result.config(text=result)

def calculate_sin():
    global equation
    try:
        angle = eval(equation)
        result = math.sin(math.radians(angle))
        equation = str(result)
    except:
        equation = "error"
    label_result.config(text=equation)

def calculate_cos():
    global equation
    try:
        angle = eval(equation)
        result = math.cos(math.radians(angle))
        equation = str(result)
    except:
        equation = "error"
    label_result.config(text=equation)

def calculate_tan():
    global equation
    try:
        angle = eval(equation)
        result = math.tan(math.radians(angle))
        equation = str(result)
    except:
        equation = "error"
    label_result.config(text=equation)

def under_root():
    global equation
    try:
        result = math.sqrt(eval(equation))
        equation = str(result)
    except:
        equation = "error"
    label_result.config(text=equation)

label_result = Label(root, width=3000, height=2, text="", font=("arial", 30))
label_result.pack()

Button(root, text="SIN", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=calculate_sin).place(x=150, y=600)
Button(root, text="COS", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=calculate_cos).place(x=300, y=600)
Button(root, text="TAN", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=calculate_tan).place(x=450, y=600)

Button(root , text="C" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#3697f5" , command= lambda:clear()).place(x=1 , y = 100)
Button(root , text="÷" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("/")).place(x=150 , y = 100)
Button(root , text="%" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36", command = lambda : show("%")).place(x=300 , y = 100)
Button(root , text="x" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("*")).place(x=450 , y = 100)


Button(root , text="7" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("7")).place(x=1 , y = 200)
Button(root , text="8" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("8")).place(x=150 , y = 200)
Button(root , text="9" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("9")).place(x=300 , y = 200)
Button(root , text="-" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("-")).place(x=450 , y = 200)


Button(root , text="4" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("4")).place(x=1 , y = 300)
Button(root , text="5" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("5")).place(x=150 , y = 300)
Button(root , text="6" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("6")).place(x=300 , y = 300)
Button(root , text="+" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("+")).place(x=450 , y = 300)

    
Button(root , text="1" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("1")).place(x=1 , y = 400)
Button(root , text="2" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("2")).place(x=150 , y = 400)
Button(root , text="3" , width = 5 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("3")).place(x=300 , y = 400)
Button(root , text="0" , width =11 , height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show("0")).place(x=10 , y = 500)



Button(root , text="." , width = 5, height = 1 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "#2a2d36" , command = lambda : show(".")).place(x=290 , y = 500)
Button(root , text="=" , width = 5 , height = 3 , font = ("arial" , 30 , "bold" ), bd= 1 ,fg = "#fff" , bg = "yellow" , command = lambda : calculate()).place(x=450 , y = 400)

Button(root, text="√", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36", command=under_root).place(x=1, y=600)

root.mainloop()
