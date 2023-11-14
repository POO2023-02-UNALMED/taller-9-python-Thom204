from tkinter import Tk, Button, Entry
root = Tk()
root.title("Calculadora")
root.resizable(0, 0)
root.geometry("500x240")

numero = []
i = 0

def get_numbers(n):
    global i
    pantalla.insert(i, n)
    i += 1

def get_operation(operator):
    global i
    opertor_length = len(operator)
    pantalla.insert(i, operator)
    i+=opertor_length

def calculate():
    equation = pantalla.get()
    try:
        ans = eval(equation)
        pantalla.delete(0, 'end')
        pantalla.insert(0, str(ans))

    except:
        pantalla.delete(0, 'end')
        pantalla.insert(0, "Syntax error")

def clear_display():
    pantalla.delete(0, 'end')


pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4)

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('1')).grid(row=1, column=0, padx=1,pady=1  )
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('2')).grid(row=1, column=1,padx=0,pady=1 )
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('3')).grid(row=1, column=2,padx=1,pady=1 )
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('4')).grid(row=2, column=0,padx=1,pady=1 )
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('5')).grid(row=2, column=1,padx=1,pady=1 )
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('6')).grid(row=2, column=2,padx=1,pady=1 )
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('7')).grid(row=3, column=0,padx=1,pady=1 )
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('8')).grid(row=3, column=1,padx=1,pady=1 )
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: get_numbers('9')).grid(row=3, column=2,padx=1,pady=1 )
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0,command=lambda: get_numbers('.')).grid(row=4, column=2,columnspan=1, rowspan=1,sticky="nsew" )
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, command=lambda :calculate(),cursor="hand2").grid(row=4, column=0, columnspan=2, rowspan=1,sticky="nsew" )
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: get_operation('+')).grid(row=1, column=3,columnspan=1, rowspan=1,sticky="nsew" )
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: get_operation('-')).grid(row=2, column=3,columnspan=1, rowspan=1,sticky="nsew" )
boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: get_operation('*')).grid(row=3, column=3,columnspan=1, rowspan=1,sticky="nsew")
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda: get_operation('/')).grid(row=4, column=3,columnspan=1, rowspan=1,sticky="nsew" )


root.mainloop()
