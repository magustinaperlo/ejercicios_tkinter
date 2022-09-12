# Ejercicio 1.1 - Contador Creciente.

# Escribir una aplicación GUI (llamada ContCreciente) como la que se
# ve en la figura. Cada vez que se haga clic en el botón "+", el valor del
# contador se incrementa en 1.
# El programa lleva 3 componentes:
# 1- Una Etiqueta "Contador"
# 2 - Un lineEdit no editable, que muestre el valor del contador
# 3 - Un Botón "+"

import tkinter as tk

ventana = tk.Tk()
ventana.title('ContCreciente')

contador = tk.IntVar()

def sumar():
    contador.set(contador.get() + 1)

label_contador = tk.Label(ventana, text='Contador', fg='black')
label_contador.grid(row=0, column=0, padx=5, pady=5)

entry_contador = tk.Entry(ventana, textvariable=contador, state="readonly")
entry_contador.grid(row=0, column=1, padx=5, pady=5)

button_sumar = tk.Button(ventana, text='+', command=sumar)
button_sumar.grid(row=0, column=2, padx=5, pady=5)

ventana.mainloop()