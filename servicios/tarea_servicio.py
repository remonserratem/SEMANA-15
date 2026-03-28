# Esta clase contiene la lógica de negocio del sistema

from modelos.tarea import Tarea


class TareaServicio:

    def __init__(self):
        # Lista donde se almacenan las tareas
        self.tareas = []

        # Contador para asignar ID automático
        self.contador_id = 1


    def agregar_tarea(self, descripcion):
        """
        Crea una nueva tarea y la agrega a la lista
        """
        tarea = Tarea(self.contador_id, descripcion)
        self.tareas.append(tarea)

        self.contador_id += 1

        return tarea


    def completar_tarea(self, id):
        """
        Marca una tarea como completada
        """
        for tarea in self.tareas:
            if tarea.id == id:
                tarea.completada = True
                return tarea


    def eliminar_tarea(self, id):
        """
        Elimina una tarea de la lista
        """
        self.tareas = [t for t in self.tareas if t.id != id]


    def listar_tareas(self):
        """
        Retorna todas las tareas
        """
        return self.tareas