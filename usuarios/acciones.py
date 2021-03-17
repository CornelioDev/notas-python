import usuarios.usuario as modelo

class Acciones:

    def login(self):
        print("Ok. Vamos a identificarte en el sistema...")
        email = input("\nIntroduce tu e-mail: ")
        password = input("Introduce tu contraseña: ")
    
    def registro(self):
        print("Ok. Vamos a registrarte en el sistema...")

        nombre = input("\n¿Cual es tu nombre?: ")
        apellidos = input("¿Cual es tu apellido?: ")
        email = input("Introduce tu e-mail: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre}. Te has registrado correctamente y tu usario es {registro[1].email}")
        else:
            print("Lo siento, algo ha malido sal")