# Clase Estudiante para gestionar la información de un estudiante
class Estudiante:
    def __init__(self, nombre, edad, matricula):
        """Constructor que inicializa los atributos del estudiante"""
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula
        self.materias = []

    def agregar_materia(self, materia):
        """Agrega una materia a la lista de materias del estudiante"""
        self.materias.append(materia)

    def mostrar_info(self):
        """Muestra la información del estudiante"""
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")
        print(f"Materias inscritas: {', '.join(self.materias)}")

# Programa principal
if __name__ == "__main__":
    print("=== Registro de Estudainte===")
    nombre = input("Ingrese el nombre del estudainte: ")
    edad = int(input("Ingrese la edad: "))
    matricula = input("Ingrese la matricula: ")

    estudiante = Estudiante(nombre, edad, matricula)

    print("\nIngrese las materias (escriba 'fin' para terminar):")
    while True:
        materia = input("Materia: ")
        if materia.lower() == 'fin':
            break
        estudiante.agregar_materia(materia)

        # Mostrar la informacion del estudiante
        estudiante.mostrar_info()
        