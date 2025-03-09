from db import conectar

def obtener_usuarios():
    """Devuelve una lista con todos los usuarios de la base de datos."""
    conn = conectar()
    if not conn:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM usuarios;")
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios
    except Exception as e:
        print(f"❌ Error al obtener usuarios: {e}")
        return []

def crear_usuario(nombre, email):
    """Inserta un nuevo usuario en la base de datos."""
    conn = conectar()
    if not conn:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s) RETURNING id;", (nombre, email))
        nuevo_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return nuevo_id
    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")
        return None

def buscar_usuario_por_id(user_id):
    """Busca un usuario por su ID y lo devuelve."""
    conn = conectar()
    if not conn:
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = %s;", (user_id,))
        usuario = cursor.fetchone()
        conn.close()
        return usuario
    except Exception as e:
        print(f"❌ Error al buscar usuario: {e}")
        return None
