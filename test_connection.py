# test_connection.py
import snowflake.connector
from snowflake_config import SNOWFLAKE_CONFIG

def test_snowflake_connection():
    try:
        print("🔄 Intentando conectar a Snowflake...")
        conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
        cursor = conn.cursor()
        
        # Probar consulta básica
        cursor.execute("SELECT CURRENT_VERSION()")
        version = cursor.fetchone()
        
        cursor.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_WAREHOUSE()")
        user_info = cursor.fetchone()
        
        print("✅ ¡Conexión exitosa!")
        print(f"📊 Versión de Snowflake: {version[0]}")
        print(f"👤 Usuario: {user_info[0]}")
        print(f"🎭 Rol: {user_info[1]}")
        print(f"🏭 Warehouse: {user_info[2]}")
        
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    test_snowflake_connection()
