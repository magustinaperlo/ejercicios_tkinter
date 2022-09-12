# Ejercicio 1.4 Contador. 

# Escribir una aplicación GUI (llamada Contador) como la que se ve en 
# la figura. Con 3 botones (Count Up - Para incrementar, Count Down - 
# Para restar y Reset - Para comenzar de cero). 
# La aplicación lleva: 1 - Una etiqueta "Contador" 
# 2 - Un lineEdit no editable, que muestre el contador y que inicie en 0 
# 3 - 3 Botones

import tkinter as tk

ventana = tk.Tk()
ventana.title('Contador')

contador = tk.IntVar()

def count_up():
    contador.set(contador.get() + 1)

def count_down():
    contador.set(contador.get() - 1)

def reset():
    contador.set(value=0)

label_contador = tk.Label(ventana, text='Contador')
label_contador.grid(row=0, column=0, padx=5, pady=5)

entry_contador = tk.Entry(ventana, textvariable=contador, state="readonly")
entry_contador.grid(row=0, column=1, padx=5, pady=5)

button_up = tk.Button(ventana, text='Count Up', command=count_up)
button_up.grid(row=0, column=2, padx=5, pady=5)

button_down = tk.Button(ventana, text='Count Down', command=count_down)
button_down.grid(row=0, column=3, padx=5, pady=5)

button_reset = tk.Button(ventana, text='Reset', command=reset)
button_reset.grid(row=0, column=4, padx=5, pady=5)

ventana.mainloop()