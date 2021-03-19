import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"De acuerdo {usuario[1]}. Vamos a crear una nueva nota...")
        titulo = input("Escribe el título de la nota:\n")
        descripcion = input("Escribe el contenido de la nota:")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[1] >= 1:
            print(f'\nPrefecto {usuario[1]}. Se ha guardado tu nota "{nota.titulo}"')
        else:
            print("No se ha guardado la nota, lo siento")