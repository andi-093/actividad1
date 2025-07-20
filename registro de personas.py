def main():
    registros = []
    contador_eliminados = 0
    
    print("Bienvenido al sistema de registro de personas")
    
    while True:
        try:
            nombre = input("Ingresa el nombre de la persona: ")
            email = input("Ingresa el email de la persona: ")
            edad = int(input("Por favor, ingresa la edad de la persona: "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue
        
        genero = input("Ingresa el género de la persona (H/M/Otro): ").strip().lower()
        
        registros.append({
            "nombre": nombre,
            "email": email,
            "edad": edad,
            "genero": genero
        })
        
        continuar = input("¿Deseas registrar otra persona? (S/N): ").strip().lower()
        if continuar not in ["s", "s"]:
            break
    
    while True:
        eliminar = input("¿Deseas eliminar algún registro? (S/N): ").strip().lower()
        if eliminar not in ["s", "s"]:
            break
        
        nombre_eliminar = input("Ingresa el nombre de la persona que deseas eliminar: ")
        registros_filtrados = [r for r in registros if r["nombre"] != nombre_eliminar]
        if len(registros) > len(registros_filtrados):
            contador_eliminados += 1
            print(f"Registro de {nombre_eliminar} eliminado.")
        else:
            print(f"No se encontró un registro con el nombre {nombre_eliminar}.")
        registros = registros_filtrados
    
    print("=========================================")
    print("Registro Finalizado")
    print(f"Total de personas registradas: {len(registros)}")
    print(f"Total de personas eliminadas: {contador_eliminados}")
    
    mayores = sum(1 for r in registros if r["edad"] >= 18)
    menores = len(registros) - mayores
    hombres = sum(1 for r in registros if r["genero"] == "h")
    mujeres = sum(1 for r in registros if r["genero"] == "m")
    otro = len(registros) - (hombres + mujeres)
    
    print(f"Número de personas mayores de edad: {mayores}")
    print(f"Número de personas menores de edad: {menores}")
    print(f"Número de hombres registrados: {hombres}")
    print(f"Número de mujeres registradas: {mujeres}")
    print(f"Número de personas con otro género registrado: {otro}")
    print("=========================================")
    print("Gracias por usar el sistema.")

if __name__ == "__main__":
    main()