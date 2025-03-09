from usuarios import obtener_usuarios, crear_usuario, buscar_usuario_por_id
from tabular import tabular

def mostrar_menu():
    """Muestra un menú en la consola con opciones disponibles."""
    menu_opciones = [
        ["1", "Mostrar todos los usuarios"],
        ["2", "Agregar un nuevo usuario"],
        ["3", "Buscar usuario por ID"],
        ["4", "Salir"]
    ]

    print("\n🔹 MENÚ PRINCIPAL 🔹")
    print(tabular(menu_opciones, headers=["Opción", "Acción"]))

def ejecutar_opcion(opcion):
    """Ejecuta la función seleccionada por el usuario."""
    if opcion == "1":
        usuarios = obtener_usuarios()
        if usuarios:
            print("\n📋 Lista de Usuarios:")
            print(tabular(usuarios, headers=["ID", "Nombre", "Email"]))
        else:
            print("\n⚠️ No hay usuarios registrados.")

    elif opcion == "2":
        nombre = input("\nIngrese el nombre del usuario: ")
        email = input("Ingrese el email del usuario: ")
        nuevo_id = crear_usuario(nombre, email)
        if nuevo_id:
            print(f"✅ Usuario creado con éxito. ID: {nuevo_id}")
        else:
            print("❌ Error al crear usuario.")

    elif opcion == "3":
        try:
            user_id = int(input("\nIngrese el ID del usuario a buscar: "))
            usuario = buscar_usuario_por_id(user_id)
            if usuario:
                print("\n🔍 Usuario encontrado:")
                print(tabular([usuario], headers=["ID", "Nombre", "Email"]))
            else:
                print("⚠️ Usuario no encontrado.")
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")

    elif opcion == "4":
        print("\n👋 Saliendo del programa... ¡Hasta luego!")
        exit()

    else:
        print("⚠️ Opción inválida. Inténtalo de nuevo.")

# AQUI SE UTILIZA UN LOOP PARA QUE EL PROGRAMA CORRA HASTA QUE SE INDIQUE SU SALIDA
if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        ejecutar_opcion(opcion)
