import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER", "mi_usuario")
DB_PASSWORD = os.getenv("DB_PASSWORD", "mi_contraseña")
DB_HOST = os.getenv("DB_HOST", "localhost")  # Puede ser "localhost" o "127.0.0.1"
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mi_base_de_datos")

def conectar():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("✅ Conexión exitosa a la base de datos en Docker")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        return None
