from datetime import datetime

class Tarea:
    def __init__(self, descripcion, fecha_limite, prioridad, categoria):
        self.id = self.generar_id()
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.categoria = categoria
        self.estado = 'pendiente'

    @staticmethod
    def generar_id():
        return int(datetime.now().timestamp() * 1000)

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        tarea = Tarea(
            descripcion=data['descripcion'],
            fecha_limite=data['fecha_limite'],
            prioridad=data['prioridad'],
            categoria=data['categoria']
        )
        tarea.id = data['id']
        tarea.estado = data['estado']
        return tarea
