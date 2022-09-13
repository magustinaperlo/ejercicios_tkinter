# Juego Matemático. 

# Escribir una aplicación GUI (llamada Juego Matemático) como la que 
# se ve en la figura. 
# La aplicación lleva: 
# 1 - 7 etiquetas (Juegos:, 2, Buenos:, 1, Malos:, 1 y -) las etiquetas que 
# son números arrancan en vacías. La etiqueta - (entre medio de los dos 
# lineEdit) arranca con signo de pregunta (?) y cambia dependiendo el 
# valor del radioButton (Sumar = +, Restar = -, Multiplicar = * y Dividir = /). 
# 2 - 3 lineEdit (Sólo el lineEdit Resultado puede ser modificado) 
# 3 - 2 Botones (Nuevo Numero y Resultado)

# Un poco más de complejidad ¿Porqué no? 
# Puedes agregar 3 radioButton más para que el jugador pueda elegir 
# la dificultad. 
# Si elige Fácil (los números aleatorios serán de 0 a 10), si 
# elige Medio (los números aleatorios serán de 0 a 100) y si 
# elige Difícil (los números aleatorios serán de 0 a 1000). 
# Cada vez que elija una dificultad todo vuelve a 0. 
# Y puedes agregar un contador (LCD Number) que haga una cuenta 
# regresiva de 60 segundos (si el jugador no responde antes del tiempo 
# pierde ese juego). El tiempo en segundos puede ser también 
# dependiendo de la dificultad.

import tkinter as tk
from random import randint

ventana = tk.Tk()
ventana.title('Juego Matemático')

numero_1 = tk.IntVar()
numero_2 = tk.IntVar()
resultado = tk.DoubleVar()
resultado_real = tk.DoubleVar()
operaciones = tk.IntVar()
juegos = tk.IntVar()
buenos = tk.IntVar()
malos = tk.IntVar()
signo = tk.StringVar(value='?')
dificultad = tk.IntVar(value=10)
lista_signos = ('+', '-', '*', '/')

def nuevo_numero():
    button_nuevo_numero.config(state='disabled')
    entry_resultado.config(state='normal')
    entry_resultado.delete(0, tk.END)
    label_numero_juegos.config(text=juegos.get())
    juegos.set(juegos.get() + 1)
    numero_1.set(randint(0, dificultad.get()))
    numero_2.set(randint(0, dificultad.get()))
    operaciones.set(randint(1, 4))

    while numero_2.get() == 0 and operaciones.get() == 4:
        operaciones.set(randint(1, 4))
    
    label_signo.config(text=lista_signos[operaciones.get() - 1])
    button_resultado.config(state='active')
    
def perder():
    malos.set(malos.get() + 1)
    label_numero_malos.config(text=malos.get())

def calcular():
    button_resultado.config(state='disabled')
    button_nuevo_numero.config(state='active')
    entry_resultado.config(state='disabled')
    try:
        match operaciones.get():
            case 1:
                resultado_real.set(numero_1.get() + numero_2.get())
            case 2:
                resultado_real.set(numero_1.get() - numero_2.get())
            case 3:
                resultado_real.set(numero_1.get() * numero_2.get())
            case 4:
                resultado_real.set(numero_1.get() / numero_2.get())

        if round(resultado_real.get(), 1) == round(resultado.get(), 1):
            buenos.set(buenos.get() + 1)
            label_numero_buenos.config(text=buenos.get())
        else:
            perder()
    except:
        perder()

def reiniciar():
    juegos.set(0)
    label_numero_juegos.config(text=juegos.get())
    buenos.set(0)
    label_numero_buenos.config(text=buenos.get())
    malos.set(0)
    label_numero_malos.config(text=malos.get())
    button_resultado.config(state='disabled')
    button_nuevo_numero.config(state='active')

label_juegos = tk.Label(ventana, text='Juegos: ')
label_juegos.grid(row=7, column=2, padx=5, pady=5, sticky=tk.E)

label_numero_juegos = tk.Label(ventana, text=juegos.get())
label_numero_juegos.grid(row=7, column=3, padx=5, pady=5, sticky=tk.W)

label_buenos = tk.Label(ventana, text='Buenos: ')
label_buenos.grid(row=8, column=2, padx=5, pady=5, sticky=tk.E)

label_numero_buenos = tk.Label(ventana, text=buenos.get())
label_numero_buenos.grid(row=8, column=3, padx=5, pady=5, sticky=tk.W)

label_malos = tk.Label(ventana, text='Malos: ')
label_malos.grid(row=9, column=2, padx=5, pady=5, sticky=tk.E)

label_numero_malos = tk.Label(ventana, text=malos.get())
label_numero_malos.grid(row=9, column=3, padx=5, pady=5, sticky=tk.W)

label_signo = tk.Label(ventana, text=signo.get())
label_signo.grid(row=0, column=1, padx=5, pady=5)

label_dificultad = tk.Label(ventana, text='Dificultad')
label_dificultad.grid(row=6, column=0, padx=5, pady=5)

radiobutton_sumar = tk.Radiobutton(ventana, text='Sumar', variable=operaciones, value=1, state="disabled")
radiobutton_sumar.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

radiobutton_restar = tk.Radiobutton(ventana, text='Restar', variable=operaciones, value=2, state="disabled")
radiobutton_restar.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

radiobutton_multiplicar = tk.Radiobutton(ventana, text='Multiplicar', variable=operaciones, value=3, state="disabled")
radiobutton_multiplicar.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

radiobutton_dividir = tk.Radiobutton(ventana, text='Dividir', variable=operaciones, value=4, state="disabled")
radiobutton_dividir.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)

radiobutton_facil = tk.Radiobutton(ventana, text='Fácil', variable=dificultad, value=10, command=reiniciar)
radiobutton_facil.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)

radiobutton_medio = tk.Radiobutton(ventana, text='Medio', variable=dificultad, value=100, command=reiniciar)
radiobutton_medio.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)

radiobutton_dificil = tk.Radiobutton(ventana, text='Difícil', variable=dificultad, value=1000, command=reiniciar)
radiobutton_dificil.grid(row=9, column=0, padx=5, pady=5, sticky=tk.W)

entry_numero_1 = tk.Entry(ventana, textvariable=numero_1, state="readonly")
entry_numero_1.grid(row=0, column=0, padx=5, pady=5)

entry_numero_2 = tk.Entry(ventana, textvariable=numero_2, state="readonly")
entry_numero_2.grid(row=0, column=2, padx=5, pady=5)

entry_resultado = tk.Entry(ventana, textvariable=resultado)
entry_resultado.grid(row=4, column=3, padx=5, pady=5)
entry_resultado.delete(0, tk.END)
entry_resultado.config(state="readonly")

button_nuevo_numero = tk.Button(ventana, text='Nuevo número', command=nuevo_numero)
button_nuevo_numero.grid(row=1, column=3, ipadx=25, padx=5, pady=5)

button_resultado = tk.Button(ventana, text='Resultado', command=calcular, state='disabled')
button_resultado.grid(row=5, column=3, ipadx=25, padx=5, pady=5)

ventana.mainloop()