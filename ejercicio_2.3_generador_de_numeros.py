# Ejercicio 2.3 Generador de números 

# Escribir una aplicación GUI (llamada Generador de números). Su 
# función será: al pulsar el botón Generar, generará un número 
# aleatorio en el rango de los dos Spin Box. 
# La aplicación lleva: 
# 1 - 3 Etiquetas (Número 1, Número 2 y Número Generado) 
# 2 - 2 Spin Box 
# 3 - 1 lineEdit que no pueda ser modificado 
# 4 - 1 Botón "Generar"

import tkinter as tk
from random import randint

ventana = tk.Tk()
ventana.title('Generador de números')

numero_1 = tk.IntVar()
numero_2 = tk.IntVar()
numero_generado = tk.IntVar()

def generar():
    print(numero_1.get(), 'asdasdas')
    if numero_1.get() <= numero_2.get():
        numero_generado.set(randint(numero_1.get(), numero_2.get()))
    else:
        numero_generado.set(randint(numero_2.get(), numero_1.get()))

label_numero_1 = tk.Label(ventana, text='Número 1')
label_numero_1.grid(row=0, column=0, padx=5, pady=5)

label_numero_2 = tk.Label(ventana, text='Número 2')
label_numero_2.grid(row=1, column=0, padx=5, pady=5)

label_numero_generado = tk.Label(ventana, text='Número generado')
label_numero_generado.grid(row=2, column=0, padx=5, pady=5)

spinbox_numero_1 = tk.Spinbox(ventana, textvariable=numero_1, from_=-100, to=100, increment=1, state="readonly")
spinbox_numero_1.grid(row=0, column=1, padx=5, pady=5)

spinbox_numero_2 = tk.Spinbox(ventana, textvariable=numero_2, from_=-100, to=100, increment=1, state="readonly")
spinbox_numero_2.grid(row=1, column=1, padx=5, pady=5)

entry_numero_generado = tk.Entry(ventana, textvariable=numero_generado)
entry_numero_generado.grid(row=2, column=1, padx=5, pady=5)

button_generar = tk.Button(ventana, text='Generar', command=generar)
button_generar.grid(row=3, column=1, padx=5, pady=5)

ventana.mainloop()