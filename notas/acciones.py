import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"De acuerdo {usuario[1]}. Vamos a crear una nueva nota...")
        titulo = input("Escribe el título de la nota: ")
        descripcion = input("Escribe el contenido de la nota:\n")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\nPrefecto {usuario[1]}. Se ha guardado tu nota "{nota.titulo}"')
        else:
            print("No se ha guardado la nota, lo siento")
    
    def mostrar(self, usuario):
        print(f"\nOkay {usuario[1]}. Estas son todas tus notas:\n")
        
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for nota in notas:
            print("\n**********************************")
            print(nota[2])
            print(nota[3])