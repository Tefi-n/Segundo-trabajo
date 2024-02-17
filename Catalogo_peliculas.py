import os

class Pelicula:
    def __init__(self, titulo, director, genero):
        self.titulo = titulo
        self.director = director
        self.__genero = genero

    def __str__(self):
        return f"{self.titulo}, director {self.director} pertenece al género {self.__genero}"

    @property
    def genero(self):
        return self.__genero

class CatalogoPelicula():
    def __init__(self, genero_pelicula, ruta_archivo):
        self.peliculas = []
        self.genero_pelicula = genero_pelicula
        self.ruta_archivo = ruta_archivo

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"La película '{pelicula.titulo}' ha sido agregada al catálogo correctamente")
        self.guardar_en_archivo()

    def listar(self):
        if self.peliculas:
            for pelicula in self.peliculas:
                print(pelicula)
        else:
            print("El catálogo está vacío")

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"El catálogo '{self.genero_pelicula}' ha sido eliminado")
        else:
            print("No se encuentran existencias")

    def guardar_en_archivo(self):
        try:
            with open(self.ruta_archivo, 'w') as file:
                for pelicula in self.peliculas:
                    file.write(f"{pelicula.titulo},{pelicula.director},{pelicula.genero}\n")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")

def menu():
  
    c_peliculas = CatalogoPelicula("Catalogo", "catalogo_peliculas.txt")

    while True:
        print("\n ::: CATÁLOGO DE PELÍCULAS::: "
            "\n"
            "\n Menú de opciones: "
            "\n"
            "\n 1. Agregar películas al catálogo"
            "\n 2. Listar películas existentes"
            "\n 3. Eliminar catálogo"
            "\n 4. Salir")
        

        try:
            opcion = int(input("Seleccione la opción deseada: "))

            if opcion == 1:
                titulo = input("Ingrese el nombre de la película: ")
                director = input("Ingrese el nombre del director: ")
                genero = input("Ingrese el género de la película: ")
                pelicula = Pelicula(titulo, director, genero)
                c_peliculas.agregar(pelicula)

            elif opcion == 2:
                c_peliculas.listar()

            elif opcion == 3:
                c_peliculas.eliminar()
                break

            elif opcion == 4:
                print("¡Hasta pronto!")
                break

        except ValueError:
            print("Ingrese una opción válida")

menu()
