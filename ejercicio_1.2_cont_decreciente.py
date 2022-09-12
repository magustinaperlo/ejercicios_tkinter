# Ejercicio 1.2 - Contador Decreciente.

# Escribir una aplicación GUI (llamada ContDecreciente) como la que se
# ve en la figura. Cada ves que se haga clic en el botón "-", al valor de
# contador se le resta 1.
# El programa lleva 3 componentes:
# 1 - Una Etiqueta "Contador"
# 2 - Un lineEdit no editable, que muestre el valor de contador y que
# inicie con el número 88
# 3 - Un Botón "-"

import tkinter as tk

ventana = tk.Tk()
ventana.title('ContDecreciente')

contador = tk.IntVar(value=88)

def restar():
    contador.set(contador.get() - 1)

label_contador = tk.Label(ventana, text='Contador')
label_contador.grid(row=0, column=0, padx=5, pady=5)

entry_contador = tk.Entry(ventana, textvariable=contador, state="readonly")
entry_contador.grid(row=0, column=1, padx=5, pady=5)

button_sumar = tk.Button(ventana, text='-', command=restar)
button_sumar.grid(row=0, column=2, padx=5, pady=5)

ventana.mainloop()