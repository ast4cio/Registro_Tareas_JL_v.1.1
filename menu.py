def mostrar_menu():
    print("\nBienvenido a TASK MASTER 1.1")
    print("1. Crear Tarea")
    print("2. Leer Tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")

def solicitar_tarea():
    descripcion = input("Descripción: ")
    fecha_limite = input("Fecha límite (YYYY-MM-DD): ")
    prioridad = input("Prioridad (baja, media, alta): ")
    categoria = input("Categoría: ")
    return descripcion, fecha_limite, prioridad, categoria
