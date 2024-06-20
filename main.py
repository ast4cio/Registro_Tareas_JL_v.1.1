from gestor_tareas import GestorTareas
from menu import mostrar_menu, solicitar_tarea

def main():
    gestor = GestorTareas('tareas.json')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            descripcion, fecha_limite, prioridad, categoria = solicitar_tarea()
            tarea = gestor.crear_tarea(descripcion, fecha_limite, prioridad, categoria)
            print(f"Tarea creada con ID {tarea.id}")

        elif opcion == '2':
            print("\nTareas existentes:")
            tareas = gestor.leer_tareas()
            for tarea in tareas:
                print(f"ID: {tarea.id}, Descripción: {tarea.descripcion}, Fecha Límite: {tarea.fecha_limite}, "
                      f"Prioridad: {tarea.prioridad}, Categoría: {tarea.categoria}, Estado: {tarea.estado}")

        elif opcion == '3':
            id_tarea = int(input("ID de la tarea a actualizar: "))
            descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
            fecha_limite = input("Nueva fecha límite (YYYY-MM-DD, dejar vacío para no cambiar): ")
            prioridad = input("Nueva prioridad (baja, media, alta, dejar vacío para no cambiar): ")
            categoria = input("Nueva categoría (dejar vacío para no cambiar): ")
            estado = input("Nuevo estado (pendiente, en progreso, completada, dejar vacío para no cambiar): ")

            kwargs = {}
            if descripcion: kwargs['descripcion'] = descripcion
            if fecha_limite: kwargs['fecha_limite'] = fecha_limite
            if prioridad: kwargs['prioridad'] = prioridad
            if categoria: kwargs['categoria'] = categoria
            if estado: kwargs['estado'] = estado

            tarea = gestor.actualizar_tarea(id_tarea, **kwargs)
            if tarea:
                print("Tarea actualizada.")
            else:
                print("Tarea no encontrada.")

        elif opcion == '4':
            id_tarea = int(input("ID de la tarea a eliminar: "))
            gestor.eliminar_tarea(id_tarea)
            print("Tarea eliminada.")

        elif opcion == '5':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
