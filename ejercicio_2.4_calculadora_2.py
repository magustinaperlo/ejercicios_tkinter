# Ejercicio 2.4 Calculadora 2. 

# Escribir una aplicación GUI (llamada Calculadora 2) como la que se ve 
# en la figura y que funcione como una calculadora. 
# La aplicación lleva: 
# 1 - 4 Etiquetas (Valor 1, Valor 2, Resultado y Operaciones) 
# 2 - 4 radioButton (Sumar, Restar, Multiplicar y Dividir) 
# 3 - 3 lineEdit (el lineEdit Resultado no puede ser modificado) 
# 4 - 1 botón Calcular, que al ser presionado realice la operación 
# correspondiente.

import tkinter as tk

ventana = tk.Tk()
ventana.title('Calculadora 2')

valor_1 = tk.DoubleVar()
valor_2 = tk.DoubleVar()
resultado = tk.DoubleVar()
operaciones = tk.StringVar(value='sumar')

def calcular():
    match operaciones.get():
        case 'sumar':
            resultado.set(valor_1.get() + valor_2.get())
        case 'restar':
            resultado.set(valor_1.get() - valor_2.get())
        case 'multiplicar':
            resultado.set(valor_1.get() * valor_2.get())
        case 'dividir':
            resultado.set(valor_1.get() / valor_2.get())

label_valor_1 = tk.Label(ventana, text='Valor 1')
label_valor_1.grid(row=1, column=0, padx=5, pady=5)

label_valor_2 = tk.Label(ventana, text='Valor 2')
label_valor_2.grid(row=2, column=0, padx=5, pady=5)

label_resultado = tk.Label(ventana, text='Resultado')
label_resultado.grid(row=3, column=0, padx=5, pady=5)

label_operaciones = tk.Label(ventana, text='Operaciones')
label_operaciones.grid(row=0, column=2, padx=5, pady=5)

radiobutton_sumar = tk.Radiobutton(ventana, text='Sumar', variable=operaciones, value='sumar')
radiobutton_sumar.grid(row=1, column=2, padx=5, pady=5)

radiobutton_restar = tk.Radiobutton(ventana, text='Restar', variable=operaciones, value='restar')
radiobutton_restar.grid(row=2, column=2, padx=5, pady=5)

radiobutton_multiplicar = tk.Radiobutton(ventana, text='Multiplicar', variable=operaciones, value='multiplicar')
radiobutton_multiplicar.grid(row=3, column=2, padx=5, pady=5)

radiobutton_dividir = tk.Radiobutton(ventana, text='Dividir', variable=operaciones, value='dividir')
radiobutton_dividir.grid(row=4, column=2, padx=5, pady=5)

entry_valor_1 = tk.Entry(ventana, textvariable=valor_1)
entry_valor_1.delete(0, tk.END)
entry_valor_1.grid(row=1, column=1, padx=5, pady=5)

entry_valor_2 = tk.Entry(ventana, textvariable=valor_2)
entry_valor_2.delete(0, tk.END)
entry_valor_2.grid(row=2, column=1, padx=5, pady=5)

entry_resultado = tk.Entry(ventana, textvariable=resultado, state="readonly")
entry_resultado.grid(row=3, column=1, padx=5, pady=5)

button_calcular = tk.Button(ventana, text='Calcular', command=calcular)
button_calcular.grid(row=4, column=1, ipadx=25, padx=5, pady=5)

ventana.mainloop()
