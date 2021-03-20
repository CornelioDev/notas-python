import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def login(self):
        print("Ok. Vamos a identificarte en el sistema...")
        
        try:
            email = input("\nIntroduce tu e-mail: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"\nBienvenido {login[1]} {login[2]}\nFecha de registro: {login[5]}")
                self.ProximasAcciones(login)
        
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Login incorrecto")
        
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
    
    def ProximasAcciones(self, usuario):
        
        print("""
        Acciones disponibles:
            -Crear nota (crear)
            -Mostrar tus notas (mostrar)
            -Eliminar nota (eliminar)
            -Salir (salir)
        """)

        accion = input("¿Qué quieres hacer? -> ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            print("Vamos a crear")
            self.ProximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.ProximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar una nota")
            self.ProximasAcciones(usuario)
        elif accion == "salir":
            exit()
