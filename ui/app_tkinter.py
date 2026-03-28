import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio


class AppTkinter:

    def __init__(self, root):

        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Instancia del servicio
        self.servicio = TareaServicio()

        # -------- CAMPO DE TEXTO --------

        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)

        # Evento de teclado (Enter)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # -------- BOTONES --------

        frame_botones = tk.Frame(root)
        frame_botones.pack()

        self.btn_agregar = tk.Button(
            frame_botones,
            text="Añadir Tarea",
            command=self.agregar_tarea
        )
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(
            frame_botones,
            text="Marcar Completada",
            command=self.completar_tarea
        )
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            command=self.eliminar_tarea
        )
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # -------- LISTA DE TAREAS --------

        self.lista = tk.Listbox(root, width=50, height=15)
        self.lista.pack(pady=10)

        # Evento de ratón (doble clic)
        self.lista.bind("<Double-1>", self.completar_tarea_evento)


    def agregar_tarea(self):
        """
        Agrega una tarea desde el campo de texto
        """

        descripcion = self.entry.get()

        if descripcion != "":
            tarea = self.servicio.agregar_tarea(descripcion)

            self.lista.insert(tk.END, f"{tarea.id}. {tarea.descripcion}")

            self.entry.delete(0, tk.END)


    def agregar_tarea_evento(self, event):
        """
        Permite agregar tarea presionando ENTER
        """
        self.agregar_tarea()


    def completar_tarea(self):
        """
        Marca una tarea seleccionada como completada
        """

        seleccion = self.lista.curselection()

        if seleccion:
            index = seleccion[0]

            texto = self.lista.get(index)

            id = int(texto.split(".")[0])

            tarea = self.servicio.completar_tarea(id)

            # Feedback visual
            self.lista.delete(index)

            self.lista.insert(index, f"{tarea.id}. [Hecho] {tarea.descripcion}")

            self.lista.itemconfig(index, fg="gray")


    def completar_tarea_evento(self, event):
        """
        Permite completar tarea con doble clic
        """
        self.completar_tarea()


    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada
        """

        seleccion = self.lista.curselection()

        if seleccion:
            index = seleccion[0]

            texto = self.lista.get(index)

            id = int(texto.split(".")[0])

            self.servicio.eliminar_tarea(id)

            self.lista.delete(index)