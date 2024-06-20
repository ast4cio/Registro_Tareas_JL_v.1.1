import json
import os
from tarea import Tarea

class GestorTareas:
    def __init__(self, archivo):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as file:
                return [Tarea.from_dict(tarea) for tarea in json.load(file)]
        return []

    def guardar_tareas(self):
        with open(self.archivo, 'w') as file:
            json.dump([tarea.to_dict() for tarea in self.tareas], file, indent=4)

    def crear_tarea(self, descripcion, fecha_limite, prioridad, categoria):
        tarea = Tarea(descripcion, fecha_limite, prioridad, categoria)
        self.tareas.append(tarea)
        self.guardar_tareas()
        return tarea

    def leer_tareas(self, filtro=None, ordenar_por=None):
        tareas_filtradas = self.tareas
        if filtro:
            tareas_filtradas = [tarea for tarea in self.tareas if filtro(tarea)]
        if ordenar_por:
            tareas_filtradas = sorted(tareas_filtradas, key=ordenar_por)
        return tareas_filtradas

    def actualizar_tarea(self, id_tarea, **kwargs):
        tarea = next((tarea for tarea in self.tareas if tarea.id == id_tarea), None)
        if tarea:
            for key, value in kwargs.items():
                if hasattr(tarea, key):
                    setattr(tarea, key, value)
            self.guardar_tareas()
            return tarea
        return None

    def eliminar_tarea(self, id_tarea):
        self.tareas = [tarea for tarea in self.tareas if tarea.id != id_tarea]
        self.guardar_tareas()
