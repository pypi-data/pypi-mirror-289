import os

def streamsysLoad(filename):
    if not filename.endswith('.strS'):
        raise ValueError("El archivo debe tener la extensión .strS")

    if not os.path.isfile(filename):
        raise FileNotFoundError(f"No se encuentra el archivo: {filename}")

    with open(filename, 'r') as file:
        content = file.read()

    # Aquí deberías agregar la lógica para interpretar y ejecutar el contenido del archivo .strS
    # Por ejemplo:
    print(f"Contenido de {filename}:")
    print(content)
