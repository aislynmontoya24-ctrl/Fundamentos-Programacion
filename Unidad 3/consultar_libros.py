def consultar_libros():
    try:
        with open("libros.txt", "r", encoding="utf-8") as f:
            libros = f.readlines()

        if libros:  # Si la lista NO está vacía
            print("\nLista de libros:")
            for linea in libros:
                linea = linea.strip()  # Elimina saltos de línea
                if linea:  # Evita líneas vacías
                    titulo, autor = linea.split(",", 1)
                    print(f"• {titulo} — {autor}")
        else:
            print("No hay libros registrados.")
            
    except FileNotFoundError:
        print("Aún no existe el archivo de libros.")

if __name__ == "__main__":
    consultar_libros()