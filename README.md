# Aplicación de Gestión de Tareas 📝

Proyecto enfocado en una aplicación desarrollada en **Python** que permite gestionar tareas diarias de manera sencilla y eficiente. Está diseñada para ofrecer funcionalidades básicas de administración de tareas, incluyendo la persistencia de datos mediante una base de datos SQL, y soporta exportar e importar tareas utilizando archivos JSON.

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
- **Base de Datos:** Base de datos en SQL utilizando SQLAlchemy  
- **Gestión de Datos:** Módulo `json` para importar/exportar tareas  
- **Interfaz:** Construido con [Streamlit](https://streamlit.io).

---

## 🛠️ Instalación y Configuración

### Prerrequisitos
1. **Python 3.8 o superior:**. Puedes descargarlo desde [python.org](https://www.python.org/).
2. **Entorno virtual (opcional):** Se recomienda crear un entorno virtual para manejar las dependencias.

### Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd <nombre-del-repositorio>

## Dependencias Necesarias

las puedes instalar con el siguiente comando
```bash
pip install -r requirements.txt
```

## Ejecuta la aplicación con el comando:

```bash
streamlit run app.py

```

## Vistas del Proyecto

Agregar una tarea
![image](https://github.com/user-attachments/assets/2e4decf2-c4d8-4fbe-a880-0d04f201db6f)

Listar Tareas
![image](https://github.com/user-attachments/assets/3e5eb51f-3288-46b8-8a8c-5191d834d2a2)

Marcar una tarea como completa
![image](https://github.com/user-attachments/assets/b6cfa8a1-eac6-4c46-9501-f1fbfbbefc06)
 
Eliminar una tarea
![image](https://github.com/user-attachments/assets/a88a6cc5-ef93-45d1-a804-ff89d6b5e2e7)

Exportar tareas (tareas que luego de exportadas se guardan dentro del proyecto)
![image](https://github.com/user-attachments/assets/08344739-a900-4501-918c-7497d641f763)

![image](https://github.com/user-attachments/assets/71438067-d9e3-41e0-91ec-46b32a38c698)

Importar una tarea
![image](https://github.com/user-attachments/assets/f44dc16e-5964-4c91-b307-136312da0d67)


