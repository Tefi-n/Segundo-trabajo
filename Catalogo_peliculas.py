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

        # Cargar películas desde el archivo al inicio
        self.cargar_desde_archivo()

    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        print(f"La película '{pelicula.titulo}' ha sido agregada al catálogo correctamente.")
        self.guardar_en_archivo()

    def listar(self):
        if self.peliculas:
            for pelicula in self.peliculas:
                print(pelicula)
        else:
            print("El catálogo está vacío.")

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"El catálogo '{self.genero_pelicula}' ha sido eliminado.")
        else:
            print("No se encuentran existencias.")

    def guardar_en_archivo(self):
        try:
            with open(self.ruta_archivo, 'w') as file:
                for pelicula in self.peliculas:
                    file.write(f"{pelicula.titulo},{pelicula.director},{pelicula.genero}\n")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")

    def cargar_desde_archivo(self):
        try:
            if os.path.exists(self.ruta_archivo):
                with open(self.ruta_archivo, 'r') as file:
                    for line in file:
                        datos = line.strip().split(',')
                        if len(datos) == 3:
                            pelicula = Pelicula(datos[0], datos[1], datos[2])
                            self.peliculas.append(pelicula)
        except Exception as e:
            print(f"Error al cargar desde el archivo: {e}")

def menu_principal():
    nombre_catalogo = input("Ingrese el nombre del género de película buscado: ")
    catalogo = CatalogoPelicula(nombre_catalogo, "C:\\Users\\teefi\\OneDrive\\Documentos\\Python\\catalo_pelicula.txt")

    while True:
        print("\n¿Qué desea hacer?:")
        print("1. Agregar películas al catálogo")
        print("2. Listar películas existentes")
        print("3. Eliminar catálogo")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione la opción deseada: "))

            if opcion == 1:
                titulo = input("Ingrese el nombre de la película: ")
                director = input("Ingrese el nombre del director: ")
                genero = input("Ingrese el género de la película: ")
                pelicula = Pelicula(titulo, director, genero)
                catalogo.agregar(pelicula)

            elif opcion == 2:
                catalogo.listar()

            elif opcion == 3:
                catalogo.eliminar()
                break

            elif opcion == 4:
                print("¡Hasta pronto!")
                break

            else:
                print("Opción inválida. Por favor, elija una opción correcta.")
        except ValueError:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    menu_principal()
