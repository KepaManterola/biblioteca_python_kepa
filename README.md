# biblioteca_python_kepa

Programa de consola para gestionar los libros y socios de una biblioteca.

## Cómo ejecutar

Desde la carpeta del proyecto:

```
python3 main.py
```

Los datos se guardan en la carpeta `datos/` (`libros.txt`, `socios.txt` y `log.txt`).

## Estructura

```
main.py                               → Inicio del programa
vista/menu.py                         → Interacción con el usuario
controlador/gestor_biblioteca.py      → Conecta la lógica con el almacenamiento
modelo/libro.py, modelo/socio.py      → Clases Libro y Socio
modelo/biblioteca.py                  → Lógica de la biblioteca
persistencia/gestor_almacenamiento.py → Lectura y escritura de ficheros
errores/excepciones.py                → Excepciones propias
datos/                                → Ficheros de datos
```

## Qué hace cada módulo

- **main.py**: crea los objetos (almacenamiento, biblioteca, gestor y menú), los conecta entre sí y arranca el menú.

- **vista/menu.py (Menu)**: muestra el menú, pide los datos con `input()`, pide las operaciones al gestor y muestra los resultados o los errores con `print()`.

- **controlador/gestor_biblioteca.py (GestorBiblioteca)**: recibe las peticiones del menú, le pide a la biblioteca que haga la operación y, si sale bien, le pide al almacenamiento que escriba el log y guarde los datos.

- **modelo/biblioteca.py (Biblioteca)**: guarda las listas de libros y socios, y contiene las reglas: buscar, añadir, prestar y devolver. Si algo no se puede hacer, lanza una excepción. No usa `print`, ni `input`, ni ficheros.

- **persistencia/gestor_almacenamiento.py (GestorAlmacenamiento)**: lee y guarda los ficheros `.txt` y escribe el log. Si hay un problema con los ficheros, lanza `AlmacenamientoError`.

- **errores/excepciones.py**: `PrestamoError`, `DatosInvalidosError` y `AlmacenamientoError`.

## Cómo colaboran los módulos

Ejemplo: **prestar un libro**

1. **Menu** pide el código del libro y del socio.
2. **Menu** llama a `gestor.prestar(id_libro, id_socio)`.
3. **GestorBiblioteca** llama a `biblioteca.prestar(...)`.
4. **Biblioteca** comprueba que existen el libro y el socio, que el socio no tiene ya un libro y que el libro está disponible. Si algo falla, lanza `PrestamoError`. Si todo está bien, marca el préstamo.
5. **GestorBiblioteca** pide a **GestorAlmacenamiento** que escriba el log y guarde los ficheros.
6. **Menu** muestra "Libro ... prestado a ...", o el error si se lanzó una excepción.

Los datos se guardan después de cada cambio y también al salir con la opción 8.

## Posibles mejoras

- Que un socio pueda tener mas de un libro a la vez.
- Guardar la fecha de prestamo y avisar si un libro lleva mucho tiempo prestado.
- Buscar tambien por autor o por genero.
- Poder borrar o modificar libros y socios.
- Mostrar los libros por paginas porque son muchos.
- Hacer una interfaz grafica.