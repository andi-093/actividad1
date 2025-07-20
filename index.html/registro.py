def main():
    contador_total = 0
    contador_mayores = 0
    contador_menores = 0
    contador_hombres = 0
    contador_mujeres = 0
    contador_otro = 0
    
    print("Bienvenido al sistema de registro de personas")
    
    while True:
        try:
            edad = int(input("Por favor, ingresa la edad de la persona: "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue
        
        genero = input("Ingresa el género de la persona (H/M/Otro): ").strip().lower()
        if genero == "h":
            contador_hombres += 1
        elif genero == "m":
            contador_mujeres += 1
        else:
            contador_otro += 1
        
        if edad >= 18:
            print("La persona es mayor de edad.")
            contador_mayores += 1
        else:
            print("La persona es menor de edad.")
            contador_menores += 1
        
        contador_total += 1
        
        continuar = input("¿Deseas registrar otra persona? (Sí/No): ").strip().lower()
        if continuar not in ["sí", "si"]:
            break
    
    print("=========================================")
    print("Registro Finalizado")
    print(f"Total de personas registradas: {contador_total}")
    print(f"Número de personas mayores de edad: {contador_mayores}")
    print(f"Número de personas menores de edad: {contador_menores}")
    print(f"Número de hombres registrados: {contador_hombres}")
    print(f"Número de mujeres registradas: {contador_mujeres}")
    print(f"Número de personas con otro género registrado: {contador_otro}")
    print("=========================================")
    print("Gracias por usar el sistema.")

if __name__ == "__main__":
    main()
