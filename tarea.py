import random

class Tarea:
    def __init__(self, descripcion, fecha_limite, prioridad, categoria, tareas_existentes):
        self.id = self.generar_id_unico(tareas_existentes)
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.categoria = categoria
        self.estado = 'pendiente'

    @staticmethod
    def generar_id_unico(tareas_existentes):
        while True:
            id_generado = random.randint(10000, 99999)
            if not any(tarea.id == id_generado for tarea in tareas_existentes):
                return id_generado

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        tarea = Tarea(
            descripcion=data['descripcion'],
            fecha_limite=data['fecha_limite'],
            prioridad=data['prioridad'],
            categoria=data['categoria'],
            tareas_existentes=[]
        )
        tarea.id = data['id']
        tarea.estado = data['estado']
        return tarea
