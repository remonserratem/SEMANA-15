# Clase que representa una tarea del sistema

class Tarea:

    def __init__(self, id, descripcion):
        # Identificador único de la tarea
        self.id = id

        # Texto de la tarea
        self.descripcion = descripcion

        # Estado de la tarea (False = pendiente / True = completada)
        self.completada = False