from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos

DATABASE_URL = "mysql://root@127.0.0.1/todo_python"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo para crear las tareas
class Tarea(Base):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String)
    estado = Column(Boolean, default=False)  # False: pendiente, True: completada

# Crear las tablas
Base.metadata.create_all(engine)

# Funciones CRUD
def agregar_tarea(titulo, descripcion):
    nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
    session.add(nueva_tarea)
    session.commit()
    print(f"Tarea '{titulo}' agregada con éxito.")

def listar_tareas():
    tareas = session.query(Tarea).all()
    lista_tareas = []  # Crear una lista para almacenar las tareas
    for tarea in tareas:
        lista_tareas.append({
            "id": tarea.id,
            "titulo": tarea.titulo,
            "descripcion": tarea.descripcion,
            "estado": tarea.estado
        })
    return lista_tareas  # Retornar la lista de tareas


def marcar_completada(id_tarea):
    tarea = session.query(Tarea).filter(Tarea.id == id_tarea).first()
    if tarea:
        tarea.estado = True
        session.commit()
        print(f"Tarea '{tarea.titulo}' marcada como completada.")
    else:
        print("Tarea no encontrada.")

def eliminar_tarea(id_tarea):
    tarea = session.query(Tarea).filter(Tarea.id == id_tarea).first()
    if tarea:
        session.delete(tarea)
        session.commit()
        print(f"Tarea '{tarea.titulo}' eliminada.")
    else:
        print("Tarea no encontrada.")

def exportar_tareas(archivo):
    tareas = session.query(Tarea).all()
    datos = [{"id": t.id, "titulo": t.titulo, "descripcion": t.descripcion, "estado": t.estado} for t in tareas]
    with open(archivo, "w") as f:
        import json
        json.dump(datos, f)
    print(f"Tareas exportadas a {archivo}.")

def importar_tareas(contenido):
    try:
        import json
        datos = json.loads(contenido)  # Parsear el contenido directamente
        for tarea in datos:
            nueva_tarea = Tarea(**tarea)
            session.merge(nueva_tarea)  # Actualizar o insertar la tarea
        session.commit()
        print("Tareas importadas correctamente.")
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON. Asegúrate de que tenga un formato válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


# Menú principal
def menu():
    while True:
        print("\nGestión de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Exportar tareas")
        print("6. Importar tareas")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            id_tarea = int(input("ID de la tarea a completar: "))
            marcar_completada(id_tarea)
        elif opcion == "4":
            id_tarea = int(input("ID de la tarea a eliminar: "))
            eliminar_tarea(id_tarea)
        elif opcion == "5":
            archivo = input("Nombre del archivo para exportar: ")
            exportar_tareas(archivo)
        elif opcion == "6":
            archivo = input("Nombre del archivo para importar: ")
            importar_tareas(archivo)
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()

 
