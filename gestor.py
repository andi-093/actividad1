from abc import ABC, abstractmethod

# === CLASE ABSTRACTA (INTERFAZ) ===
class Producto(ABC):
    def __init__(self, nombre, precio_base, stock):
        self.nombre = nombre
        self.precio_base = precio_base
        self.stock = stock

    @abstractmethod
    def calcular_precio_final(self):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass

    def verificar_stock(self):
        return self.stock > 0


# === SUBCLASES CONCRETAS ===

class Electronico(Producto):
    def __init__(self, nombre, precio_base, stock, garantia):
        super().__init__(nombre, precio_base, stock)
        self.garantia = garantia

    def calcular_precio_final(self):
        return self.precio_base * 1.15

    def mostrar_info(self):
        print(f"[Electrónico] {self.nombre} - ${self.calcular_precio_final():.2f} - Garantía: {self.garantia} años")

class Alimento(Producto):
    def __init__(self, nombre, precio_base, stock, caducidad):
        super().__init__(nombre, precio_base, stock)
        self.caducidad = caducidad

    def calcular_precio_final(self):
        return self.precio_base * 1.08

    def mostrar_info(self):
        print(f"[Alimento] {self.nombre} - ${self.calcular_precio_final():.2f} - Vence: {self.caducidad}")

class Ropa(Producto):
    def __init__(self, nombre, precio_base, stock, talla):
        super().__init__(nombre, precio_base, stock)
        self.talla = talla

    def calcular_precio_final(self):
        return self.precio_base * 1.12

    def mostrar_info(self):
        print(f"[Ropa] {self.nombre} - ${self.calcular_precio_final():.2f} - Talla: {self.talla}")


# === FUNCIONES DEL SISTEMA ===

def registrar_producto():
    print("\nRegistrar nuevo producto")
    print("1. Electrónico\n2. Alimento\n3. Ropa")
    tipo = input("Seleccione el tipo de producto (1-3): ")

    nombre = input("Nombre del producto: ")
    precio_base = float(input("Precio base: "))
    stock = int(input("Cantidad en stock: "))

    if tipo == "1":
        garantia = int(input("Años de garantía: "))
        return Electronico(nombre, precio_base, stock, garantia)
    elif tipo == "2":
        caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")
        return Alimento(nombre, precio_base, stock, caducidad)
    elif tipo == "3":
        talla = input("Talla: ")
        return Ropa(nombre, precio_base, stock, talla)
    else:
        print("Tipo no válido. Producto no registrado.")
        return None


def mostrar_inventario(productos):
    print("\n=== INVENTARIO ===")
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        producto.mostrar_info()
        print("Disponible:", "Sí" if producto.verificar_stock() else "No")
        print("-" * 40)


# === PROGRAMA PRINCIPAL ===

def main():
    inventario = []

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar producto")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = registrar_producto()
            if producto:
                inventario.append(producto)
                print("✅ Producto registrado correctamente.")
        elif opcion == "2":
            mostrar_inventario(inventario)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
