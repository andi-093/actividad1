class Empresa:
    def __init__ (self, nombre, servicio, telefono, direccion, detalles):
        self.nombre = nombre
        self.servicio = servicio
        self.telefono = telefono
        self.direccion = direccion
        self.detalles = detalles
    
    def mostrar_info(self):
        print("=== Informacion de la empresa ===")
        print(f"Nombre:{self.nombre}")
        print(f"Servicio:{self.servicio}")
        print(f"Telefono{self.telefono}")
        print(f"Direccion{self.direccion}")
        print(f"Detalles{self.detalles}")

def registrar_empresa():
    print("=== Registro de la empresa ===")
    nombre = input("Ingrese su nombre:")
    servicio = input("Ingrese el servicio que ofrece:")
    telefono = input("Ingrese telefono:")
    direccion = input("ingrese la direccion:")
    detalles = input("Ingrese los detalles que ofrece su servicio:")
    return Empresa(nombre, servicio, telefono, direccion, detalles)

def mostrar_inventario(inventario):
    if not inventario:
        print("No hay empresas registradas.")
    else:
        for i, empresa in enumerate(inventario, start=1):
            print(f"\nEmpresa #{i}")
            empresa.mostrar_info()

def main ():
    inventario = []

    while True:
        print("\n--- Menu ---")
        print("1. Registrar empresa")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            empresa = registrar_empresa()
            if empresa:
                inventario.append(empresa)
                print("✅ Empresa registrada correctamente.")
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()