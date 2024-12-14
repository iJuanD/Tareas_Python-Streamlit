# Aplicación de Gestión de Tareas 📝

Este proyecto es una aplicación desarrollada en **Python** que permite gestionar tareas diarias de manera sencilla y eficiente. Está diseñada para ofrecer funcionalidades básicas de administración de tareas, incluyendo la persistencia de datos mediante una base de datos SQL, y soporta exportar e importar tareas utilizando archivos JSON.

---

## 🚀 Funcionalidades Principales

- **Agregar Tareas:**  
  Permite al usuario agregar nuevas tareas con un título y una descripción.

- **Listar Tareas:**  
  Muestra todas las tareas almacenadas con su estado (pendiente o completada).

- **Marcar Tareas como Completadas:**  
  Posibilita marcar tareas específicas como completadas para un mejor seguimiento.

- **Eliminar Tareas:**  
  Permite eliminar tareas específicas, ideal para mantener un registro actualizado.

- **Guardar y Cargar Tareas:**  
  Soporte para exportar las tareas a un archivo JSON y cargarlas desde el mismo archivo.

---

## ⚙️ Tecnologías Utilizadas

- **Lenguaje de Programación:** Python  
- **Persistencia de Datos:** Base de datos en SQL utilizando SQLAlchemy  
- **Gestión de Datos:** Módulo `json` para importar/exportar tareas  
- **Interfaz:** Construido con [Streamlit](https://streamlit.io) para una experiencia gráfica interactiva.

---

## 🛠️ Instalación y Configuración

### Prerrequisitos
1. **Python 3.8 o superior:** Asegúrate de tener instalado Python. Puedes descargarlo desde [python.org](https://www.python.org/).
2. **Entorno virtual (opcional):** Se recomienda crear un entorno virtual para manejar las dependencias.

### Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>


## Dependencias Necesarias

las puedes instalar con el siguiente comando
pip install -r requirements.txt

## Ejecuta la aplicación con el comando:

```bash
streamlit run app.py
