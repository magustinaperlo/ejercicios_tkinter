# Ejercicio 1.3 – Factorial. 

# Escribir una aplicación GUI (llamada Factorial) como la que se ve en 
# la figura. Cada ves que se haga clic en el botón "Siguiente", debe 
# calcular el factorial del primer lineEdit y mostrarlo en el segundo. Al 
# dar siguiente (n se incrementa en 1) n = 2 con su factorial correspondiente.
# Formula de factorial . 
# Factorial de 5 = 1 x 2 x 3 x 4 x 5 = 120 
# Factorial de 3 = 1 x 2 x 3 = 6 
# La aplicación lleva: 
# 1 - Dos etiquetas: una para n y otra para Factorial (n) 
# 2 - Dos lineEdit no editables 
# 3 - Un botón siguiente

import tkinter as tk

ventana = tk.Tk()
ventana.title('Factorial')

n = tk.IntVar(value=1)
factorial = tk.IntVar(value=1)

def calcular_factorial():
    n.set(n.get() + 1)
    factorial.set(factorial.get() * n.get())

label_n = tk.Label(ventana, text='n')
label_n.grid(row=0, column=0, padx=5, pady=5)

label_factorial = tk.Label(ventana, text='Factorial(n)')
label_factorial.grid(row=0, column=2, padx=5, pady=5)

entry_n = tk.Entry(ventana, textvariable=n, state="readonly")
entry_n.grid(row=0, column=1, padx=5, pady=5)

entry_factorial = tk.Entry(ventana, textvariable=factorial, state="readonly")
entry_factorial.grid(row=0, column=3, padx=5, pady=5)

button_siguiente = tk.Button(ventana, text='Siguiente', command=calcular_factorial)
button_siguiente.grid(row=0, column=4, padx=5, pady=5)

ventana.mainloop()