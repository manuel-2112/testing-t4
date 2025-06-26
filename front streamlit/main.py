import streamlit as st
import requests
from typing import Optional

# Configuración de la URL base de la API
API_BASE_URL = "http://localhost:8000"

# Configuración de la página de Streamlit
st.set_page_config(page_title="GymHero Frontend", layout="wide")

# Función para registrar un nuevo usuario
def register_user(email: str, password: str, full_name: Optional[str] = None):
    url = f"{API_BASE_URL}/auth/register"
    payload = {
        "email": email,
        "password": password,
        "full_name": full_name
    }
    response = requests.post(url, json=payload)
    return response

# Función para iniciar sesión y obtener el token de acceso
def login_user(username: str, password: str):
    url = f"{API_BASE_URL}/auth/login"
    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url, data=payload, headers=headers)
    return response

# Función para verificar si el usuario está autenticado
def is_authenticated():
    return 'token' in st.session_state

# Funciones para gestionar Ejercicios
def fetch_exercises(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/exercises/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def create_exercise(name: str, description: Optional[str], target_body_part_id: int,
                   exercise_type_id: int, level_id: int, token: str):
    url = f"{API_BASE_URL}/exercises/"
    payload = {
        "name": name,
        "description": description,
        "target_body_part_id": target_body_part_id,
        "exercise_type_id": exercise_type_id,
        "level_id": level_id
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

def update_exercise(exercise_id: int, name: Optional[str], description: Optional[str],
                   target_body_part_id: Optional[int], exercise_type_id: Optional[int],
                   level_id: Optional[int], token: str):
    url = f"{API_BASE_URL}/exercises/{exercise_id}"
    payload = {
        "name": name,
        "description": description,
        "target_body_part_id": target_body_part_id,
        "exercise_type_id": exercise_type_id,
        "level_id": level_id
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.put(url, json=payload, headers=headers)
    return response

def delete_exercise(exercise_id: int, token: str):
    url = f"{API_BASE_URL}/exercises/{exercise_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers)
    return response

# Funciones para gestionar Tipos de Ejercicio
def fetch_exercise_types(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/exercise-types/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def create_exercise_type(name, token):
    url = f"{API_BASE_URL}/exercise-types/"
    payload = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json=payload, headers=headers)

def update_exercise_type(exercise_type_id, name, token):
    url = f"{API_BASE_URL}/exercise-types/{exercise_type_id}"
    payload = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, json=payload, headers=headers)

def delete_exercise_type(exercise_type_id, token):
    url = f"{API_BASE_URL}/exercise-types/{exercise_type_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(url, headers=headers)

# Funciones para gestionar Usuarios (solo para superusuarios)
def fetch_users(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/users/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def create_user(email, password, full_name, token):
    url = f"{API_BASE_URL}/users/"
    payload = {"email": email, "password": password, "full_name": full_name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json=payload, headers=headers)

def update_user(user_id, email, is_active, full_name, password, is_superuser, token):
    url = f"{API_BASE_URL}/users/{user_id}"
    payload = {
        "email": email,
        "is_active": is_active,
        "full_name": full_name,
        "password": password,
        "is_superuser": is_superuser
    }
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, json=payload, headers=headers)

def delete_user(user_id, token):
    url = f"{API_BASE_URL}/users/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(url, headers=headers)

# Funciones para gestionar Niveles
def fetch_levels(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/levels/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def create_level(name, token):
    url = f"{API_BASE_URL}/levels/"
    payload = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json=payload, headers=headers)

def update_level(level_id, name, token):
    url = f"{API_BASE_URL}/levels/{level_id}"
    payload = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, json=payload, headers=headers)

def delete_level(level_id, token):
    url = f"{API_BASE_URL}/levels/{level_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(url, headers=headers)

# Funciones para gestionar Partes del Cuerpo
def fetch_body_parts(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/body-parts/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def create_body_part(name, token):
    url = f"{API_BASE_URL}/body-parts/"
    payload = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json=payload, headers=headers)

def update_body_part(body_part_id, name, token):
    url = f"{API_BASE_URL}/body-parts/{body_part_id}"
    payload = {"name": name}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, json=payload, headers=headers)

def delete_body_part(body_part_id, token):
    url = f"{API_BASE_URL}/body-parts/{body_part_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(url, headers=headers)

# Funciones para gestionar Planes de Entrenamiento
def fetch_training_plans(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/training-plans/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def fetch_my_training_plans(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/training-plans/all/my"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, params=params, headers=headers)

def create_training_plan(name, description, token):
    url = f"{API_BASE_URL}/training-plans/"
    payload = {"name": name, "description": description}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json=payload, headers=headers)

def update_training_plan(training_plan_id, name, description, token):
    url = f"{API_BASE_URL}/training-plans/{training_plan_id}"
    payload = {"name": name, "description": description}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, json=payload, headers=headers)

def delete_training_plan(training_plan_id, token):
    url = f"{API_BASE_URL}/training-plans/{training_plan_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(url, headers=headers)

def add_training_unit_to_plan(training_plan_id, training_unit_id, token):
    url = f"{API_BASE_URL}/training-plans/{training_plan_id}/training-units/{training_unit_id}/add"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, headers=headers)

def remove_training_unit_from_plan(training_plan_id, training_unit_id, token):
    url = f"{API_BASE_URL}/training-plans/{training_plan_id}/training-units/{training_unit_id}/remove"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, headers=headers)

def fetch_training_units_in_plan(training_plan_id, token):
    url = f"{API_BASE_URL}/training-plans/{training_plan_id}/training-units"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers)

# Funciones para gestionar Unidades de Entrenamiento
def fetch_training_units(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/training-units/all"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(url, params=params, headers=headers)

def fetch_my_training_units(skip=0, limit=10, token=None):
    url = f"{API_BASE_URL}/training-units/all/my"
    params = {"skip": skip, "limit": limit}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, params=params, headers=headers)

def create_training_unit(name, description, token):
    url = f"{API_BASE_URL}/training-units/"
    payload = {"name": name, "description": description}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(url, json=payload, headers=headers)

def update_training_unit(training_unit_id, name, description, token):
    url = f"{API_BASE_URL}/training-units/{training_unit_id}"
    payload = {"name": name, "description": description}
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, json=payload, headers=headers)

def delete_training_unit(training_unit_id, token):
    url = f"{API_BASE_URL}/training-units/{training_unit_id}"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.delete(url, headers=headers)

def add_exercise_to_unit(training_unit_id, exercise_id, token):
    url = f"{API_BASE_URL}/training-units/{training_unit_id}/exercises/{exercise_id}/add"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, headers=headers)

def remove_exercise_from_unit(training_unit_id, exercise_id, token):
    url = f"{API_BASE_URL}/training-units/{training_unit_id}/exercises/{exercise_id}/remove"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.put(url, headers=headers)

def fetch_exercises_in_unit(training_unit_id, token):
    url = f"{API_BASE_URL}/training-units/{training_unit_id}/exercises"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers)

# Funciones para obtener detalles del usuario actual (opcional)
def fetch_current_user(token):
    url = f"{API_BASE_URL}/users/me"
    headers = {"Authorization": f"Bearer {token}"}
    return requests.get(url, headers=headers)

# Barra lateral para la navegación
st.sidebar.title("GymHero")
selection = st.sidebar.radio("Navegación", [
    "Inicio", 
    "Registrarse", 
    "Iniciar Sesión", 
    "Ejercicios", 
    "Tipos de Ejercicio",
    "Usuarios",
    "Niveles",
    "Partes del Cuerpo",
    "Planes de Entrenamiento",
    "Unidades de Entrenamiento"
])

# Página de Inicio
if selection == "Inicio":
    st.title("¡Bienvenido a GymHero!")
    st.write("Gestiona tus ejercicios y planes de entrenamiento de manera sencilla.")

# Página de Registro
elif selection == "Registrarse":
    st.title("Registrarse")
    with st.form("register_form"):
        email = st.text_input("Correo Electrónico")
        password = st.text_input("Contraseña", type="password")
        full_name = st.text_input("Nombre Completo (Opcional)")
        submit = st.form_submit_button("Crear Cuenta")
    
    if submit:
        if not email or not password:
            st.error("Por favor, completa todos los campos requeridos.")
        else:
            response = register_user(email, password, full_name)
            if response.status_code == 201:
                st.success("¡Registro exitoso! Puedes iniciar sesión ahora.")
            else:
                try:
                    error = response.json()
                    st.error(f"Error en el registro: {error.get('detail', response.text)}")
                except:
                    st.error(f"Error en el registro: {response.text}")

# Página de Inicio de Sesión
elif selection == "Iniciar Sesión":
    st.title("Iniciar Sesión")
    with st.form("login_form"):
        username = st.text_input("Correo Electrónico")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Iniciar Sesión")
    
    if submit:
        if not username or not password:
            st.error("Por favor, completa todos los campos requeridos.")
        else:
            response = login_user(username, password)
            if response.status_code == 200:
                data = response.json()
                st.session_state['token'] = data['access_token']
                st.success("¡Inicio de sesión exitoso!")
            else:
                try:
                    error = response.json()
                    st.error(f"Error al iniciar sesión: {error.get('detail', response.text)}")
                except:
                    st.error(f"Error al iniciar sesión: {response.text}")

# Página de Gestión de Ejercicios
elif selection == "Ejercicios":
    st.title("Gestión de Ejercicios")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar los ejercicios.")
    else:
        token = st.session_state['token']
        # Sub-secciones para diferentes acciones
        ejercicio_action = st.selectbox("Selecciona una acción", ["Ver Ejercicios", "Crear Ejercicio", "Actualizar Ejercicio", "Eliminar Ejercicio"])
        
        # Ver Ejercicios
        if ejercicio_action == "Ver Ejercicios":
            st.header("Lista de Ejercicios")
            with st.form("fetch_form"):
                skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                limit = st.number_input("Límite", min_value=1, value=10, step=1)
                fetch_submit = st.form_submit_button("Obtener Ejercicios")
            
            if fetch_submit:
                response = fetch_exercises(skip, limit, token)
                if response.status_code == 200:
                    exercises = response.json()
                    if exercises:
                        for exercise in exercises:
                            st.subheader(exercise['name'])
                            st.write(f"**Descripción:** {exercise.get('description', 'N/A')}")
                            st.write(f"**ID:** {exercise['id']}")
                            st.write(f"**Parte del Cuerpo Objetivo ID:** {exercise['target_body_part_id']}")
                            st.write(f"**Tipo de Ejercicio ID:** {exercise['exercise_type_id']}")
                            st.write(f"**Nivel ID:** {exercise['level_id']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron ejercicios con los parámetros proporcionados.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener ejercicios: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener ejercicios: {response.text}")
        
        # Crear Ejercicio
        elif ejercicio_action == "Crear Ejercicio":
            st.header("Crear Nuevo Ejercicio")
            with st.form("create_form"):
                name = st.text_input("Nombre del Ejercicio")
                description = st.text_area("Descripción (Opcional)")
                target_body_part_id = st.number_input("ID de la Parte del Cuerpo Objetivo", min_value=1, step=1)
                exercise_type_id = st.number_input("ID del Tipo de Ejercicio", min_value=1, step=1)
                level_id = st.number_input("ID del Nivel", min_value=1, step=1)
                create_submit = st.form_submit_button("Crear Ejercicio")
            
            if create_submit:
                if not name or not target_body_part_id or not exercise_type_id or not level_id:
                    st.error("Por favor, completa todos los campos requeridos.")
                else:
                    response = create_exercise(name, description, target_body_part_id, exercise_type_id, level_id, token)
                    if response.status_code == 201:
                        st.success("¡Ejercicio creado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al crear el ejercicio: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al crear el ejercicio: {response.text}")
        
        # Actualizar Ejercicio
        elif ejercicio_action == "Actualizar Ejercicio":
            st.header("Actualizar Ejercicio Existente")
            with st.form("update_form"):
                exercise_id = st.number_input("ID del Ejercicio a Actualizar", min_value=1, step=1)
                name = st.text_input("Nuevo Nombre del Ejercicio (Opcional)")
                description = st.text_area("Nueva Descripción (Opcional)")
                target_body_part_id = st.number_input("Nuevo ID de la Parte del Cuerpo Objetivo (Opcional)", min_value=1, step=1)
                exercise_type_id = st.number_input("Nuevo ID del Tipo de Ejercicio (Opcional)", min_value=1, step=1)
                level_id = st.number_input("Nuevo ID del Nivel (Opcional)", min_value=1, step=1)
                update_submit = st.form_submit_button("Actualizar Ejercicio")
            
            if update_submit:
                if not exercise_id:
                    st.error("Por favor, proporciona el ID del ejercicio a actualizar.")
                else:
                    response = update_exercise(
                        exercise_id,
                        name if name else None,
                        description if description else None,
                        target_body_part_id if target_body_part_id else None,
                        exercise_type_id if exercise_type_id else None,
                        level_id if level_id else None,
                        token
                    )
                    if response.status_code == 200:
                        st.success("¡Ejercicio actualizado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al actualizar el ejercicio: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al actualizar el ejercicio: {response.text}")
        
        # Eliminar Ejercicio
        elif ejercicio_action == "Eliminar Ejercicio":
            st.header("Eliminar Ejercicio")
            with st.form("delete_form"):
                exercise_id = st.number_input("ID del Ejercicio a Eliminar", min_value=1, step=1)
                delete_submit = st.form_submit_button("Eliminar Ejercicio")
            
            if delete_submit:
                if not exercise_id:
                    st.error("Por favor, proporciona el ID del ejercicio a eliminar.")
                else:
                    response = delete_exercise(exercise_id, token)
                    if response.status_code == 200:
                        st.success("¡Ejercicio eliminado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al eliminar el ejercicio: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al eliminar el ejercicio: {response.text}")

# Página de Gestión de Tipos de Ejercicio
elif selection == "Tipos de Ejercicio":
    st.title("Gestión de Tipos de Ejercicio")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar los tipos de ejercicio.")
    else:
        token = st.session_state['token']
        # Sub-secciones: Ver, Crear, Actualizar, Eliminar
        tipo_action = st.selectbox("Selecciona una acción", ["Ver Tipos", "Crear Tipo", "Actualizar Tipo", "Eliminar Tipo"])
        
        # Ver Tipos de Ejercicio
        if tipo_action == "Ver Tipos":
            st.header("Lista de Tipos de Ejercicio")
            with st.form("fetch_exercise_types_form"):
                skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                limit = st.number_input("Límite", min_value=1, value=10, step=1)
                fetch_submit = st.form_submit_button("Obtener Tipos de Ejercicio")
            
            if fetch_submit:
                response = fetch_exercise_types(skip, limit, token)
                if response.status_code == 200:
                    exercise_types = response.json()
                    if exercise_types:
                        for et in exercise_types:
                            st.subheader(et['name'])
                            st.write(f"**ID:** {et['id']}")
                            st.write(f"**Creado en:** {et['created_at']}")
                            st.write(f"**Actualizado en:** {et['updated_at']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron tipos de ejercicio con los parámetros proporcionados.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener tipos de ejercicio: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener tipos de ejercicio: {response.text}")
        
        # Crear Tipo de Ejercicio
        elif tipo_action == "Crear Tipo":
            st.header("Crear Nuevo Tipo de Ejercicio")
            with st.form("create_exercise_type_form"):
                name = st.text_input("Nombre del Tipo de Ejercicio")
                submit = st.form_submit_button("Crear Tipo")
            
            if submit:
                if not name:
                    st.error("Por favor, proporciona un nombre para el tipo de ejercicio.")
                else:
                    response = create_exercise_type(name, token)
                    if response.status_code == 201:
                        st.success("¡Tipo de ejercicio creado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al crear el tipo de ejercicio: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al crear el tipo de ejercicio: {response.text}")
        
        # Actualizar Tipo de Ejercicio
        elif tipo_action == "Actualizar Tipo":
            st.header("Actualizar Tipo de Ejercicio Existente")
            with st.form("update_exercise_type_form"):
                exercise_type_id = st.number_input("ID del Tipo de Ejercicio a Actualizar", min_value=1, step=1)
                name = st.text_input("Nuevo Nombre del Tipo de Ejercicio")
                submit = st.form_submit_button("Actualizar Tipo")
            
            if submit:
                if not exercise_type_id or not name:
                    st.error("Por favor, proporciona el ID y el nuevo nombre del tipo de ejercicio.")
                else:
                    response = update_exercise_type(exercise_type_id, name, token)
                    if response.status_code == 200:
                        st.success("¡Tipo de ejercicio actualizado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al actualizar el tipo de ejercicio: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al actualizar el tipo de ejercicio: {response.text}")
        
        # Eliminar Tipo de Ejercicio
        elif tipo_action == "Eliminar Tipo":
            st.header("Eliminar Tipo de Ejercicio")
            with st.form("delete_exercise_type_form"):
                exercise_type_id = st.number_input("ID del Tipo de Ejercicio a Eliminar", min_value=1, step=1)
                submit = st.form_submit_button("Eliminar Tipo")
            
            if submit:
                if not exercise_type_id:
                    st.error("Por favor, proporciona el ID del tipo de ejercicio a eliminar.")
                else:
                    response = delete_exercise_type(exercise_type_id, token)
                    if response.status_code == 200:
                        st.success("¡Tipo de ejercicio eliminado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al eliminar el tipo de ejercicio: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al eliminar el tipo de ejercicio: {response.text}")

# Página de Gestión de Usuarios (Solo Superusuarios)
elif selection == "Usuarios":
    st.title("Gestión de Usuarios")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar los usuarios.")
    else:
        token = st.session_state['token']
        # Verificar si el usuario es superusuario
        # Suponiendo que tienes un endpoint para obtener el usuario actual
        user_response = fetch_current_user(token)
        if user_response.status_code == 200:
            current_user = user_response.json()
            if not current_user.get('is_superuser', False):
                st.error("No tienes permisos para acceder a esta sección.")
            else:
                # Sub-secciones: Ver, Crear, Actualizar, Eliminar
                user_action = st.selectbox("Selecciona una acción", ["Ver Usuarios", "Crear Usuario", "Actualizar Usuario", "Eliminar Usuario"])
                
                # Ver Usuarios
                if user_action == "Ver Usuarios":
                    st.header("Lista de Usuarios")
                    with st.form("fetch_users_form"):
                        skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                        limit = st.number_input("Límite", min_value=1, value=10, step=1)
                        fetch_submit = st.form_submit_button("Obtener Usuarios")
                    
                    if fetch_submit:
                        response = fetch_users(skip, limit, token)
                        if response.status_code == 200:
                            users = response.json()
                            if users:
                                for user in users:
                                    st.subheader(f"{user['email']}")
                                    st.write(f"**ID:** {user['id']}")
                                    st.write(f"**Activo:** {user['is_active']}")
                                    st.write(f"**Nombre Completo:** {user.get('full_name', 'N/A')}")
                                    st.markdown("---")
                            else:
                                st.info("No se encontraron usuarios con los parámetros proporcionados.")
                        else:
                            try:
                                error = response.json()
                                st.error(f"Error al obtener usuarios: {error.get('detail', response.text)}")
                            except:
                                st.error(f"Error al obtener usuarios: {response.text}")
                
                # Crear Usuario
                elif user_action == "Crear Usuario":
                    st.header("Crear Nuevo Usuario")
                    with st.form("create_user_form"):
                        email = st.text_input("Correo Electrónico")
                        password = st.text_input("Contraseña", type="password")
                        full_name = st.text_input("Nombre Completo (Opcional)")
                        is_superuser = st.checkbox("Es Superusuario")
                        submit = st.form_submit_button("Crear Usuario")
                    
                    if submit:
                        if not email or not password:
                            st.error("Por favor, completa todos los campos requeridos.")
                        else:
                            response = create_user(email, password, full_name, token)
                            if response.status_code == 201:
                                st.success("¡Usuario creado exitosamente!")
                            else:
                                try:
                                    error = response.json()
                                    st.error(f"Error al crear el usuario: {error.get('detail', response.text)}")
                                except:
                                    st.error(f"Error al crear el usuario: {response.text}")
                
                # Actualizar Usuario
                elif user_action == "Actualizar Usuario":
                    st.header("Actualizar Usuario Existente")
                    with st.form("update_user_form"):
                        user_id = st.number_input("ID del Usuario a Actualizar", min_value=1, step=1)
                        email = st.text_input("Nuevo Correo Electrónico (Opcional)")
                        is_active = st.checkbox("¿Está Activo?", value=True)
                        full_name = st.text_input("Nuevo Nombre Completo (Opcional)")
                        password = st.text_input("Nueva Contraseña (Opcional)", type="password")
                        is_superuser = st.checkbox("Es Superusuario")
                        submit = st.form_submit_button("Actualizar Usuario")
                    
                    if submit:
                        if not user_id:
                            st.error("Por favor, proporciona el ID del usuario a actualizar.")
                        else:
                            response = update_user(
                                user_id,
                                email if email else None,
                                is_active,
                                full_name if full_name else None,
                                password if password else None,
                                is_superuser,
                                token
                            )
                            if response.status_code == 200:
                                st.success("¡Usuario actualizado exitosamente!")
                            else:
                                try:
                                    error = response.json()
                                    st.error(f"Error al actualizar el usuario: {error.get('detail', response.text)}")
                                except:
                                    st.error(f"Error al actualizar el usuario: {response.text}")
                
                # Eliminar Usuario
                elif user_action == "Eliminar Usuario":
                    st.header("Eliminar Usuario")
                    with st.form("delete_user_form"):
                        user_id = st.number_input("ID del Usuario a Eliminar", min_value=1, step=1)
                        submit = st.form_submit_button("Eliminar Usuario")
                    
                    if submit:
                        if not user_id:
                            st.error("Por favor, proporciona el ID del usuario a eliminar.")
                        else:
                            response = delete_user(user_id, token)
                            if response.status_code == 200:
                                st.success("¡Usuario eliminado exitosamente!")
                            else:
                                try:
                                    error = response.json()
                                    st.error(f"Error al eliminar el usuario: {error.get('detail', response.text)}")
                                except:
                                    st.error(f"Error al eliminar el usuario: {response.text}")

# Página de Gestión de Niveles
elif selection == "Niveles":
    st.title("Gestión de Niveles")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar los niveles.")
    else:
        token = st.session_state['token']
        # Sub-secciones: Ver, Crear, Actualizar, Eliminar
        nivel_action = st.selectbox("Selecciona una acción", ["Ver Niveles", "Crear Nivel", "Actualizar Nivel", "Eliminar Nivel"])
        
        # Ver Niveles
        if nivel_action == "Ver Niveles":
            st.header("Lista de Niveles")
            with st.form("fetch_levels_form"):
                skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                limit = st.number_input("Límite", min_value=1, value=10, step=1)
                fetch_submit = st.form_submit_button("Obtener Niveles")
            
            if fetch_submit:
                response = fetch_levels(skip, limit, token)
                if response.status_code == 200:
                    levels = response.json()
                    if levels:
                        for level in levels:
                            st.subheader(level['name'])
                            st.write(f"**ID:** {level['id']}")
                            st.write(f"**Creado en:** {level['created_at']}")
                            st.write(f"**Actualizado en:** {level['updated_at']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron niveles con los parámetros proporcionados.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener niveles: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener niveles: {response.text}")
        
        # Crear Nivel
        elif nivel_action == "Crear Nivel":
            st.header("Crear Nuevo Nivel")
            with st.form("create_level_form"):
                name = st.text_input("Nombre del Nivel")
                submit = st.form_submit_button("Crear Nivel")
            
            if submit:
                if not name:
                    st.error("Por favor, proporciona un nombre para el nivel.")
                else:
                    response = create_level(name, token)
                    if response.status_code == 201:
                        st.success("¡Nivel creado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al crear el nivel: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al crear el nivel: {response.text}")
        
        # Actualizar Nivel
        elif nivel_action == "Actualizar Nivel":
            st.header("Actualizar Nivel Existente")
            with st.form("update_level_form"):
                level_id = st.number_input("ID del Nivel a Actualizar", min_value=1, step=1)
                name = st.text_input("Nuevo Nombre del Nivel")
                submit = st.form_submit_button("Actualizar Nivel")
            
            if submit:
                if not level_id or not name:
                    st.error("Por favor, proporciona el ID y el nuevo nombre del nivel.")
                else:
                    response = update_level(level_id, name, token)
                    if response.status_code == 200:
                        st.success("¡Nivel actualizado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al actualizar el nivel: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al actualizar el nivel: {response.text}")
        
        # Eliminar Nivel
        elif nivel_action == "Eliminar Nivel":
            st.header("Eliminar Nivel")
            with st.form("delete_level_form"):
                level_id = st.number_input("ID del Nivel a Eliminar", min_value=1, step=1)
                submit = st.form_submit_button("Eliminar Nivel")
            
            if submit:
                if not level_id:
                    st.error("Por favor, proporciona el ID del nivel a eliminar.")
                else:
                    response = delete_level(level_id, token)
                    if response.status_code == 200:
                        st.success("¡Nivel eliminado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al eliminar el nivel: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al eliminar el nivel: {response.text}")

# Página de Gestión de Partes del Cuerpo
elif selection == "Partes del Cuerpo":
    st.title("Gestión de Partes del Cuerpo")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar las partes del cuerpo.")
    else:
        token = st.session_state['token']
        # Sub-secciones: Ver, Crear, Actualizar, Eliminar
        body_part_action = st.selectbox("Selecciona una acción", ["Ver Partes del Cuerpo", "Crear Parte del Cuerpo", "Actualizar Parte del Cuerpo", "Eliminar Parte del Cuerpo"])
        
        # Ver Partes del Cuerpo
        if body_part_action == "Ver Partes del Cuerpo":
            st.header("Lista de Partes del Cuerpo")
            with st.form("fetch_body_parts_form"):
                skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                limit = st.number_input("Límite", min_value=1, value=10, step=1)
                fetch_submit = st.form_submit_button("Obtener Partes del Cuerpo")
            
            if fetch_submit:
                response = fetch_body_parts(skip, limit, token)
                if response.status_code == 200:
                    body_parts = response.json()
                    if body_parts:
                        for bp in body_parts:
                            st.subheader(bp['name'])
                            st.write(f"**ID:** {bp['id']}")
                            st.write(f"**Creado en:** {bp['created_at']}")
                            st.write(f"**Actualizado en:** {bp['updated_at']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron partes del cuerpo con los parámetros proporcionados.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener partes del cuerpo: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener partes del cuerpo: {response.text}")
        
        # Crear Parte del Cuerpo
        elif body_part_action == "Crear Parte del Cuerpo":
            st.header("Crear Nueva Parte del Cuerpo")
            with st.form("create_body_part_form"):
                name = st.text_input("Nombre de la Parte del Cuerpo")
                submit = st.form_submit_button("Crear Parte")
            
            if submit:
                if not name:
                    st.error("Por favor, proporciona un nombre para la parte del cuerpo.")
                else:
                    response = create_body_part(name, token)
                    if response.status_code == 201:
                        st.success("¡Parte del cuerpo creada exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al crear la parte del cuerpo: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al crear la parte del cuerpo: {response.text}")
        
        # Actualizar Parte del Cuerpo
        elif body_part_action == "Actualizar Parte del Cuerpo":
            st.header("Actualizar Parte del Cuerpo Existente")
            with st.form("update_body_part_form"):
                body_part_id = st.number_input("ID de la Parte del Cuerpo a Actualizar", min_value=1, step=1)
                name = st.text_input("Nuevo Nombre de la Parte del Cuerpo")
                submit = st.form_submit_button("Actualizar Parte")
            
            if submit:
                if not body_part_id or not name:
                    st.error("Por favor, proporciona el ID y el nuevo nombre de la parte del cuerpo.")
                else:
                    response = update_body_part(body_part_id, name, token)
                    if response.status_code == 200:
                        st.success("¡Parte del cuerpo actualizada exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al actualizar la parte del cuerpo: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al actualizar la parte del cuerpo: {response.text}")
        
        # Eliminar Parte del Cuerpo
        elif body_part_action == "Eliminar Parte del Cuerpo":
            st.header("Eliminar Parte del Cuerpo")
            with st.form("delete_body_part_form"):
                body_part_id = st.number_input("ID de la Parte del Cuerpo a Eliminar", min_value=1, step=1)
                submit = st.form_submit_button("Eliminar Parte")
            
            if submit:
                if not body_part_id:
                    st.error("Por favor, proporciona el ID de la parte del cuerpo a eliminar.")
                else:
                    response = delete_body_part(body_part_id, token)
                    if response.status_code == 200:
                        st.success("¡Parte del cuerpo eliminada exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al eliminar la parte del cuerpo: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al eliminar la parte del cuerpo: {response.text}")

# Página de Gestión de Planes de Entrenamiento
elif selection == "Planes de Entrenamiento":
    st.title("Gestión de Planes de Entrenamiento")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar los planes de entrenamiento.")
    else:
        token = st.session_state['token']
        # Sub-secciones: Ver, Crear, Actualizar, Eliminar, Gestionar Unidades
        plan_action = st.selectbox("Selecciona una acción", [
            "Ver Planes de Entrenamiento", 
            "Crear Plan de Entrenamiento", 
            "Actualizar Plan de Entrenamiento", 
            "Eliminar Plan de Entrenamiento",
            "Gestionar Unidades en un Plan"
        ])
        
        # Ver Planes de Entrenamiento
        if plan_action == "Ver Planes de Entrenamiento":
            st.header("Lista de Planes de Entrenamiento")
            with st.form("fetch_training_plans_form"):
                skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                limit = st.number_input("Límite", min_value=1, value=10, step=1)
                fetch_my = st.checkbox("Obtener solo mis Planes de Entrenamiento")
                fetch_submit = st.form_submit_button("Obtener Planes de Entrenamiento")
            
            if fetch_submit:
                if fetch_my:
                    response = fetch_my_training_plans(skip, limit, token)
                else:
                    response = fetch_training_plans(skip, limit, token)
                
                if response.status_code == 200:
                    training_plans = response.json()
                    if training_plans:
                        for plan in training_plans:
                            st.subheader(plan['name'])
                            st.write(f"**ID:** {plan['id']}")
                            st.write(f"**Descripción:** {plan.get('description', 'N/A')}")
                            st.write(f"**Creado en:** {plan['created_at']}")
                            st.write(f"**Actualizado en:** {plan['updated_at']}")
                            st.write(f"**Propietario ID:** {plan['owner_id']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron planes de entrenamiento con los parámetros proporcionados.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener planes de entrenamiento: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener planes de entrenamiento: {response.text}")
        
        # Crear Plan de Entrenamiento
        elif plan_action == "Crear Plan de Entrenamiento":
            st.header("Crear Nuevo Plan de Entrenamiento")
            with st.form("create_training_plan_form"):
                name = st.text_input("Nombre del Plan de Entrenamiento")
                description = st.text_area("Descripción (Opcional)")
                submit = st.form_submit_button("Crear Plan")
            
            if submit:
                if not name:
                    st.error("Por favor, proporciona un nombre para el plan de entrenamiento.")
                else:
                    response = create_training_plan(name, description, token)
                    if response.status_code == 201:
                        st.success("¡Plan de entrenamiento creado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al crear el plan de entrenamiento: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al crear el plan de entrenamiento: {response.text}")
        
        # Actualizar Plan de Entrenamiento
        elif plan_action == "Actualizar Plan de Entrenamiento":
            st.header("Actualizar Plan de Entrenamiento Existente")
            with st.form("update_training_plan_form"):
                plan_id = st.number_input("ID del Plan de Entrenamiento a Actualizar", min_value=1, step=1)
                name = st.text_input("Nuevo Nombre del Plan de Entrenamiento")
                description = st.text_area("Nueva Descripción (Opcional)")
                submit = st.form_submit_button("Actualizar Plan")
            
            if submit:
                if not plan_id or not name:
                    st.error("Por favor, proporciona el ID y el nuevo nombre del plan de entrenamiento.")
                else:
                    response = update_training_plan(plan_id, name, description, token)
                    if response.status_code == 200:
                        st.success("¡Plan de entrenamiento actualizado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al actualizar el plan de entrenamiento: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al actualizar el plan de entrenamiento: {response.text}")
        
        # Eliminar Plan de Entrenamiento
        elif plan_action == "Eliminar Plan de Entrenamiento":
            st.header("Eliminar Plan de Entrenamiento")
            with st.form("delete_training_plan_form"):
                plan_id = st.number_input("ID del Plan de Entrenamiento a Eliminar", min_value=1, step=1)
                submit = st.form_submit_button("Eliminar Plan")
            
            if submit:
                if not plan_id:
                    st.error("Por favor, proporciona el ID del plan de entrenamiento a eliminar.")
                else:
                    response = delete_training_plan(plan_id, token)
                    if response.status_code == 200:
                        st.success("¡Plan de entrenamiento eliminado exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al eliminar el plan de entrenamiento: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al eliminar el plan de entrenamiento: {response.text}")
        
        # Gestionar Unidades en un Plan de Entrenamiento
        elif plan_action == "Gestionar Unidades en un Plan":
            st.header("Gestionar Unidades en un Plan de Entrenamiento")
            with st.form("manage_units_form"):
                plan_id = st.number_input("ID del Plan de Entrenamiento", min_value=1, step=1)
                action = st.selectbox("Selecciona una acción", ["Agregar Unidad", "Eliminar Unidad"])
                training_unit_id = st.number_input("ID de la Unidad de Entrenamiento", min_value=1, step=1)
                submit = st.form_submit_button("Realizar Acción")
            
            if submit:
                if not plan_id or not training_unit_id:
                    st.error("Por favor, proporciona el ID del plan y el ID de la unidad de entrenamiento.")
                else:
                    if action == "Agregar Unidad":
                        response = add_training_unit_to_plan(plan_id, training_unit_id, token)
                        if response.status_code == 200:
                            st.success("¡Unidad de entrenamiento agregada al plan exitosamente!")
                        else:
                            try:
                                error = response.json()
                                st.error(f"Error al agregar la unidad al plan: {error.get('detail', response.text)}")
                            except:
                                st.error(f"Error al agregar la unidad al plan: {response.text}")
                    elif action == "Eliminar Unidad":
                        response = remove_training_unit_from_plan(plan_id, training_unit_id, token)
                        if response.status_code == 200:
                            st.success("¡Unidad de entrenamiento eliminada del plan exitosamente!")
                        else:
                            try:
                                error = response.json()
                                st.error(f"Error al eliminar la unidad del plan: {error.get('detail', response.text)}")
                            except:
                                st.error(f"Error al eliminar la unidad del plan: {response.text}")

# Página de Gestión de Unidades de Entrenamiento
elif selection == "Unidades de Entrenamiento":
    st.title("Gestión de Unidades de Entrenamiento")
    
    if not is_authenticated():
        st.warning("Por favor, inicia sesión para gestionar las unidades de entrenamiento.")
    else:
        token = st.session_state['token']
        # Sub-secciones: Ver, Crear, Actualizar, Eliminar, Gestionar Ejercicios
        unit_action = st.selectbox("Selecciona una acción", [
            "Ver Unidades de Entrenamiento", 
            "Crear Unidad de Entrenamiento", 
            "Actualizar Unidad de Entrenamiento", 
            "Eliminar Unidad de Entrenamiento",
            "Gestionar Ejercicios en una Unidad"
        ])
        
        # Ver Unidades de Entrenamiento
        if unit_action == "Ver Unidades de Entrenamiento":
            st.header("Lista de Unidades de Entrenamiento")
            with st.form("fetch_training_units_form"):
                skip = st.number_input("Omitir", min_value=0, value=0, step=1)
                limit = st.number_input("Límite", min_value=1, value=10, step=1)
                fetch_my = st.checkbox("Obtener solo mis Unidades de Entrenamiento")
                fetch_submit = st.form_submit_button("Obtener Unidades de Entrenamiento")
            
            if fetch_submit:
                if fetch_my:
                    response = fetch_my_training_units(skip, limit, token)
                else:
                    response = fetch_training_units(skip, limit, token)
                
                if response.status_code == 200:
                    training_units = response.json()
                    if training_units:
                        for unit in training_units:
                            st.subheader(unit['name'])
                            st.write(f"**ID:** {unit['id']}")
                            st.write(f"**Descripción:** {unit.get('description', 'N/A')}")
                            st.write(f"**Creado en:** {unit['created_at']}")
                            st.write(f"**Actualizado en:** {unit['updated_at']}")
                            st.write(f"**Propietario ID:** {unit['owner_id']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron unidades de entrenamiento con los parámetros proporcionados.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener unidades de entrenamiento: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener unidades de entrenamiento: {response.text}")
        
        # Crear Unidad de Entrenamiento
        elif unit_action == "Crear Unidad de Entrenamiento":
            st.header("Crear Nueva Unidad de Entrenamiento")
            with st.form("create_training_unit_form"):
                name = st.text_input("Nombre de la Unidad de Entrenamiento")
                description = st.text_area("Descripción (Opcional)")
                submit = st.form_submit_button("Crear Unidad")
            
            if submit:
                if not name:
                    st.error("Por favor, proporciona un nombre para la unidad de entrenamiento.")
                else:
                    response = create_training_unit(name, description, token)
                    if response.status_code == 201:
                        st.success("¡Unidad de entrenamiento creada exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al crear la unidad de entrenamiento: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al crear la unidad de entrenamiento: {response.text}")
        
        # Actualizar Unidad de Entrenamiento
        elif unit_action == "Actualizar Unidad de Entrenamiento":
            st.header("Actualizar Unidad de Entrenamiento Existente")
            with st.form("update_training_unit_form"):
                unit_id = st.number_input("ID de la Unidad de Entrenamiento a Actualizar", min_value=1, step=1)
                name = st.text_input("Nuevo Nombre de la Unidad de Entrenamiento")
                description = st.text_area("Nueva Descripción (Opcional)")
                submit = st.form_submit_button("Actualizar Unidad")
            
            if submit:
                if not unit_id or not name:
                    st.error("Por favor, proporciona el ID y el nuevo nombre de la unidad de entrenamiento.")
                else:
                    response = update_training_unit(unit_id, name, description, token)
                    if response.status_code == 200:
                        st.success("¡Unidad de entrenamiento actualizada exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al actualizar la unidad de entrenamiento: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al actualizar la unidad de entrenamiento: {response.text}")
        
        # Eliminar Unidad de Entrenamiento
        elif unit_action == "Eliminar Unidad de Entrenamiento":
            st.header("Eliminar Unidad de Entrenamiento")
            with st.form("delete_training_unit_form"):
                unit_id = st.number_input("ID de la Unidad de Entrenamiento a Eliminar", min_value=1, step=1)
                submit = st.form_submit_button("Eliminar Unidad")
            
            if submit:
                if not unit_id:
                    st.error("Por favor, proporciona el ID de la unidad de entrenamiento a eliminar.")
                else:
                    response = delete_training_unit(unit_id, token)
                    if response.status_code == 200:
                        st.success("¡Unidad de entrenamiento eliminada exitosamente!")
                    else:
                        try:
                            error = response.json()
                            st.error(f"Error al eliminar la unidad de entrenamiento: {error.get('detail', response.text)}")
                        except:
                            st.error(f"Error al eliminar la unidad de entrenamiento: {response.text}")
        
        # Gestionar Ejercicios en una Unidad de Entrenamiento
        elif unit_action == "Gestionar Ejercicios en una Unidad":
            st.header("Gestionar Ejercicios en una Unidad de Entrenamiento")
            with st.form("manage_exercises_form"):
                unit_id = st.number_input("ID de la Unidad de Entrenamiento", min_value=1, step=1)
                action = st.selectbox("Selecciona una acción", ["Agregar Ejercicio", "Eliminar Ejercicio"])
                exercise_id = st.number_input("ID del Ejercicio", min_value=1, step=1)
                submit = st.form_submit_button("Realizar Acción")
            
            if submit:
                if not unit_id or not exercise_id:
                    st.error("Por favor, proporciona el ID de la unidad y el ID del ejercicio.")
                else:
                    if action == "Agregar Ejercicio":
                        response = add_exercise_to_unit(unit_id, exercise_id, token)
                        if response.status_code == 200:
                            st.success("¡Ejercicio agregado a la unidad de entrenamiento exitosamente!")
                        else:
                            try:
                                error = response.json()
                                st.error(f"Error al agregar el ejercicio a la unidad: {error.get('detail', response.text)}")
                            except:
                                st.error(f"Error al agregar el ejercicio a la unidad: {response.text}")
                    elif action == "Eliminar Ejercicio":
                        response = remove_exercise_from_unit(unit_id, exercise_id, token)
                        if response.status_code == 200:
                            st.success("¡Ejercicio eliminado de la unidad de entrenamiento exitosamente!")
                        else:
                            try:
                                error = response.json()
                                st.error(f"Error al eliminar el ejercicio de la unidad: {error.get('detail', response.text)}")
                            except:
                                st.error(f"Error al eliminar el ejercicio de la unidad: {response.text}")
        
        # Opcional: Ver Ejercicios en una Unidad de Entrenamiento
        st.header("Ver Ejercicios en una Unidad de Entrenamiento")
        with st.form("view_exercises_in_unit_form"):
            unit_id = st.number_input("ID de la Unidad de Entrenamiento", min_value=1, step=1)
            submit = st.form_submit_button("Obtener Ejercicios")
        
        if submit:
            if not unit_id:
                st.error("Por favor, proporciona el ID de la unidad de entrenamiento.")
            else:
                response = fetch_exercises_in_unit(unit_id, token)
                if response.status_code == 200:
                    exercises = response.json()
                    if exercises:
                        for exercise in exercises:
                            st.subheader(exercise['name'])
                            st.write(f"**ID:** {exercise['id']}")
                            st.write(f"**Descripción:** {exercise.get('description', 'N/A')}")
                            st.write(f"**Parte del Cuerpo Objetivo ID:** {exercise['target_body_part_id']}")
                            st.write(f"**Tipo de Ejercicio ID:** {exercise['exercise_type_id']}")
                            st.write(f"**Nivel ID:** {exercise['level_id']}")
                            st.markdown("---")
                    else:
                        st.info("No se encontraron ejercicios en esta unidad de entrenamiento.")
                else:
                    try:
                        error = response.json()
                        st.error(f"Error al obtener ejercicios de la unidad: {error.get('detail', response.text)}")
                    except:
                        st.error(f"Error al obtener ejercicios de la unidad: {response.text}")

# Página de Gestión de Usuarios (Perfil Personal)
# Opcionalmente, podrías agregar una sección para que los usuarios gestionen su propio perfil
# Esta sección no está incluida en el listado original de endpoints, pero es una buena práctica

# Agregar un botón de Logout en la barra lateral
if is_authenticated():
    if st.sidebar.button("Cerrar Sesión"):
        del st.session_state['token']
        st.success("¡Has cerrado sesión exitosamente!")

