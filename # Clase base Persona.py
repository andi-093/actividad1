# Clase base Persona (clase Padre)
class Persona:
    def __init__(self, nombre, edad):
        """Inicializa nombre y edad de la persona"""
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        """Muestra nombre y edad de la persona"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")


# Clase derivada Estudiante que hereda de Persona (clase Hija)
class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        """Inicializa atributos de Persona y propios de Estudiante"""
        super().__init__(nombre, edad)
        self.matricula = matricula
        self.materias = []

    def agregar_materia(self, materia):
        """Agrega una materia a la lista del estudiante"""
        self.materias.append(materia)

    def mostrar_info(self):
        """Muestra la información completa del estudiante"""
        print("\n--- Información del Estudiante ---")
        super().mostrar_info()  # Reutiliza mostrar_info de Persona
        print(f"Matrícula: {self.matricula}")
        if self.materias:
            print(f"Materias inscritas: {', '.join(self.materias)}")
        else:
            print("No se inscribieron materias.")


# Programa principal con múltiples estudiantes
if __name__ == "__main__":
    estudiantes = []

    while True:
        print("\n=== Registro de Nuevo Estudiante ===")
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad: "))
        matricula = input("Ingrese la matrícula: ")

        estudiante = Estudiante(nombre, edad, matricula)

        print("\nIngrese las materias (escriba 'fin' para terminar):")
        while True:
            materia = input("Materia: ")
            if materia.lower() == 'fin':
                break
            estudiante.agregar_materia(materia)

        estudiantes.append(estudiante)

        continuar = input("¿Desea registrar otro estudiante? (s/n): ")
        if continuar.lower() != 's':
            break

    # Mostrar todos los estudiantes registrados
    print("\n======= Lista de Estudiantes Registrados =======")
    for est in estudiantes:
        est.mostrar_info()
