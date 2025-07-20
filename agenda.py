def mostrar_menu():
	print("\n--- Agenda de Contactos ---")
	print("1. Agregar contacto")
	print("2. Mostrar contactos")
	print("3. Modificar contacto")
	print("4. Eliminar contacto")
	print("5. Salir")
	
def agregar_contacto(agenda):
	nombre = input("Ingrese el nombre:")
	teléfono = input("Ingrese el teléfono:")
	email = input("Ingrese el email:")
	contacto = {
		'nombre': nombre,
		'telefono': teléfono,
		'email': email
	}
	agenda.append(contacto)
	print(f"Contacto '{nombre}' agregado esxitosamente.")

def mostrar_contacto(agenda):
	if not agenda:
		print("La agenda está vacía")
	else:
		print("\nLista de contactos:")
		for idx, contacto in enumerate(agenda):
			print(f"\nContacto #{idx + 1}")
			print(f"Nombre: {contacto['nombre']}")
			print(f"Teléfono: {contacto['telefono']}")
			print(f"Email: {contacto['email']}")

def modificar_contacto(agenda):
	nombre = input("Ingrese el nombre del contacto a modificar:")
	for contacto in agenda:
		if contacto['nombre'] == nombre:
			print("Contacto encontrado. Ingrese los nuevos datos:")
			contacto['telefono'] = input("Nuevo teléfono:")
			contacto['email'] = input("Nuevo email:")
			print(f"Contacto '{nombre}' modificado exitosamente.")
			return
	print(f"No se encontró un contacto con el nombre '{nombre}'.")

def eliminar_contacto(agenda):
	nombre = input("Ingrese el nombre del contacto a eliminar:")
	for contacto in agenda:
		if contacto['nombre'] == nombre:
			agenda.remove(contacto)
			print(f"Contacto'{nombre}' eliminado exitosamente.")
			return
	print(f"No se encontró un contacto con el nombre'{nombre}'.")

def main():
	agenda = []
	while True:
		mostrar_menu()
		opción = input("Seleccionar una opción:")
		if opción == '1':
			agregar_contacto(agenda)
		elif opción == '2':
			mostrar_contacto(agenda)
		elif opción == '3':
			modificar_contacto(agenda)
		elif opción == '4':
			eliminar_contacto(agenda)
		elif opción == '5':
			print("Saliendo de la agenda. ¡Hasta luego!")
			break
		else:
			print("Opción no valida. Por favor, seleccione una opción del 1 al 5.")