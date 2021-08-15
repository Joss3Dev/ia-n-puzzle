from tkinter import *
from tkinter import ttk


window = Tk()
window.title("N-Puzzle")
window.geometry("900x500")
window.configure(bg='bisque2')


Label(window, text="Ingrese el tamaño (N) del puzzle que desea resolver:", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=20)
n = StringVar()
Entry(window, textvariable=n, width=3).place(x=20, y=40)

laberAlgoritmo = Label(window, text="Elija el algoritmo con el cual desea resolver el puzzle:", font=('arial', 10, 'bold'), bg="bisque2").place(x=20, y=60)
algoritmos = ttk.Combobox(window, values=['BFS', 'Distancia de Manhattan', 'Piezas en lugar incorrecto'])
algoritmos.place(x=20, y=80)
algoritmos.current(0)


def procesar_puzzle():
    # Se evalua que la n obtenida sea un numero
    n_error = False
    print(n.get())
    try:
        int(n.get())
    except:
        n_error = True

    if not n_error:
        # Genera el puzzle con el tamaño pasado

        algoritmo_elegido = algoritmos.current()
        # Filtra el algoritmo con el cual va a resolver
        # BFS
        if algoritmo_elegido == 0:
            a=0
        # Distancia de Manhattan
        elif algoritmo_elegido == 1:
            a = 0
        # Piezas en lugar incorrecto
        elif algoritmo_elegido == 2:
            a=0
    else:
        error_numero = Label(window, text="Ingrese un numero para N.", fg="red")
        error_numero.pack()
        window.after(7000, error_numero.destroy)


button = Button(window, text="Generar", bg='bisque3', width=15, command=procesar_puzzle)
button.place(x=140, y=120)

mainloop()



