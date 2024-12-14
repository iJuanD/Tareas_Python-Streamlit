import streamlit as st
from main import agregar_tarea, listar_tareas, marcar_completada, eliminar_tarea, exportar_tareas, importar_tareas
import json
import os

import json
import os

def exportar_tareas(archivo):
    # Obtener las tareas desde la base de datos o fuente
    tareas = listar_tareas()  # Esta función debe retornar la lista de tareas
    if not tareas:
        raise ValueError("No hay tareas para exportar.")

    # Validar que el archivo tenga extensión .json
    if not archivo.endswith(".json"):
        archivo += ".json"

    # Guardar las tareas en el archivo dentro del proyecto
    with open(os.path.join(os.getcwd(), archivo), "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)


# Título de la aplicación
st.title("Gestión de Tareas")
st.write("¡Bienvenido a la aplicación Basica para la gestion de tareas!")

# Navegación en la interfaz
menu = st.sidebar.radio("Menú", ["Agregar Tarea", "Listar Tareas", "Marcar Tarea Completada", "Eliminar Tarea", "Exportar Tareas", "Importar Tareas"])

# Opción: Agregar Tarea
if menu == "Agregar Tarea":
    st.header("Agregar Tarea")
    with st.form("Agregar Tarea"):
        titulo = st.text_input("Título de la tarea")
        descripcion = st.text_area("Descripción de la tarea")
        submit = st.form_submit_button("Agregar")
        if submit and titulo:
            agregar_tarea(titulo, descripcion)
            st.success(f"Tarea '{titulo}' agregada con éxito.")

# Opción: Listar Tareas
elif menu == "Listar Tareas":
    st.header("Lista de Tareas")
    tareas = listar_tareas()  # Ahora retorna una lista de tareas

    if tareas:  # Comprobar que no esté vacía
        # Convertir la lista de tareas en un DataFrame para mostrarla como tabla
        import pandas as pd
        df_tareas = pd.DataFrame(tareas)
        df_tareas["estado"] = df_tareas["estado"].apply(lambda x: "✅ Completada" if x else "⏳ Pendiente")
        st.table(df_tareas)
    else:
        st.write("No hay tareas registradas Actualmente.")


# Opción: Marcar Tarea Completada
elif menu == "Marcar Tarea Completada":
    st.header("Marcar Tarea como Completada")
    id_tarea = st.number_input("ID de la tarea a completar", min_value=1, step=1)
    if st.button("Marcar como completada"):
        marcar_completada(id_tarea)
        st.success(f"Tarea con ID {id_tarea} marcada como completada.")

# Opción: Eliminar Tarea
elif menu == "Eliminar Tarea":
    
    st.header("Lista de Tareas Actuales")
    tareas = listar_tareas()  # Ahora retorna una lista de tareas

    if tareas:  # Comprobar que no esté vacía
        # Convertir la lista de tareas en un DataFrame para mostrarla como tabla
        import pandas as pd
        df_tareas = pd.DataFrame(tareas)
        df_tareas["estado"] = df_tareas["estado"].apply(lambda x: "✅ Completada" if x else "⏳ Pendiente")
        st.table(df_tareas)
    else:
        st.write("No hay tareas registradas Actualmente.")
        
    st.header("Eliminar Tarea")
    id_tarea = st.number_input("ID de la tarea a eliminar", min_value=1, step=1)
    if st.button("Eliminar tarea"):
        eliminar_tarea(id_tarea)
        st.success(f"Tarea con ID {id_tarea} eliminada.")

# Opción: Exportar Tareas
elif menu == "Exportar Tareas":
    st.header("Exportar Tareas")
    archivo = st.text_input("Nombre del archivo (por ejemplo, tareas.json)")
    if st.button("Exportar"):
        try:
            exportar_tareas(archivo)
            st.success(f"Tareas exportadas a '{archivo}'. El archivo exportado se encontrara en el DIRECTORIO DEL PROYECTO.")
        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"Ocurrió un error al exportar las tareas: {str(e)}")


# Opción: Importar Tareas
elif menu == "Importar Tareas":
    st.header("Importar Tareas")
    archivo = st.file_uploader("Selecciona el archivo para importar (por ejemplo, tareas.json)", type=["json"])
    if archivo is not None:
        try:
            contenido = archivo.read().decode("utf-8")  # Leer el contenido del archivo como texto
            importar_tareas(contenido)  # Pasar el contenido como string
            st.success("Tareas importadas correctamente.")
        except Exception as e:
            st.error(f"Ocurrió un error al importar las tareas: {e}")



