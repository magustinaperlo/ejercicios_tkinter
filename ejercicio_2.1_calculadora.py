# Ejercicio 2.1 Calculadora Ejercicio 2.1 Escribir una aplicación GUI (llamada Calculadora) que funcione como 
# una simple calculadora. 

# La aplicación lleva: 
# 1 - Tres etiquetas (Primer número, Segundo número y Resultado) 
# 2 - 3 lineEdit (el lineEdit de Resultado no se puede modificar) 
# 3 - 6 Botones (+, -, *, /, % y RESET). El botón CLEAR debe borrar los 3 lineEdit. Al presionar (+, -, *, / o %) el único campo que se modifica 
# es Resultado.

import tkinter as tk

ventana = tk.Tk()
ventana.title('Calculadora')

primero = tk.DoubleVar()
segundo = tk.DoubleVar()
resultado = tk.DoubleVar()

def sumar():
    resultado.set(primero.get() + segundo.get())

def restar():
    resultado.set(primero.get() - segundo.get())

def multiplicar():
    resultado.set(primero.get() * segundo.get())

def dividir():
    resultado.set(primero.get() / segundo.get())

def calcular_porcentaje():
    resultado.set(primero.get() * segundo.get() / 100)

def clear():
    primero.set(value=0.0)
    segundo.set(value=0.0)
    resultado.set(value=0.0)
    entry_primero.delete(0, tk.END)
    entry_segundo.delete(0, tk.END)

label_primero = tk.Label(ventana, text='Primer número')
label_primero.grid(row=0, column=0, padx=5, pady=5)

label_segundo = tk.Label(ventana, text='Segundo número')
label_segundo.grid(row=1, column=0, padx=5, pady=5)

label_resultado = tk.Label(ventana, text='Resultado')
label_resultado.grid(row=2, column=0, padx=5, pady=5)

entry_primero = tk.Entry(ventana, textvariable=primero)
entry_primero.delete(0, tk.END)
entry_primero.grid(row=0, column=1, padx=5, pady=5)

entry_segundo = tk.Entry(ventana, textvariable=segundo)
entry_segundo.delete(0, tk.END)
entry_segundo.grid(row=1, column=1, padx=5, pady=5)

entry_resultado = tk.Entry(ventana, textvariable=resultado, state="readonly")
entry_resultado.grid(row=2, column=1, padx=5, pady=5)

button_suma = tk.Button(ventana, text='+', command=sumar)
button_suma.grid(row=3, column=0, ipadx=25, padx=5, pady=5)

button_resta = tk.Button(ventana, text='-', command=restar)
button_resta.grid(row=3, column=1, ipadx=25, padx=5, pady=5)

button_multiplicacion = tk.Button(ventana, text='*', command=multiplicar)
button_multiplicacion.grid(row=4, column=0, ipadx=25, padx=5, pady=5)

button_division = tk.Button(ventana, text='/', command=dividir)
button_division.grid(row=4, column=1, ipadx=25, padx=5, pady=5)

button_porcentaje = tk.Button(ventana, text='%', command=calcular_porcentaje)
button_porcentaje.grid(row=5, column=0, ipadx=25, padx=5, pady=5)

button_clear = tk.Button(ventana, text='CLEAR', command=clear)
button_clear.grid(row=5, column=1, ipadx=25, padx=5, pady=5)

ventana.mainloop()
