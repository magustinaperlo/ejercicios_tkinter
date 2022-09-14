# Ejercicio 2.2 Películas.

# Escribir una aplicación GUI (llamada Películas). Su función será: al
# pulsar el botón Añadir, agregará en el listWidget el contenido de
# lineEdit (Películas).
# La aplicación lleva:
# 1 - 2 Etiquetas (Escribe el título de una película y Películas)
# 2 - Un lineEdit donde se escribirá el nombre de la película
# 3 - Un listWidget que registra las películas añadidas
# 4 - Un botón "Añadir"

import tkinter as tk

ventana = tk.Tk()
ventana.title('Películas')

pelicula = tk.StringVar()
lista_peliculas = tk.StringVar()

def agregar():
    listbox_peliculas.insert(tk.END, entry_pelicula.get())
    entry_pelicula.delete(0, tk.END)

label_titulo = tk.Label(ventana, text='Escribe el título de una película')
label_titulo.grid(row=0, column=0, padx=5, pady=5)

label_peliculas = tk.Label(ventana, text='Películas')
label_peliculas.grid(row=0, column=1, padx=5, pady=5)

entry_pelicula = tk.Entry(ventana, textvariable=pelicula)
entry_pelicula.grid(row=1, column=0, padx=5, pady=5)

listbox_peliculas = tk.Listbox(ventana)
listbox_peliculas.grid(row=1, column=1, padx=5, pady=5)

button_agregar = tk.Button(ventana, text='Añadir', command=agregar)
button_agregar.grid(row=2, column=0, padx=5, pady=5)

ventana.mainloop()
