import wikipedia

wikipedia.set_lang("es")  # Establecer el idioma a español

def buscar_informacion(consulta):
    try:
        # Realizar la búsqueda en Wikipedia
        pagina = wikipedia.page(consulta)
        
        longitud = int(input("Digite el numero maximo de palabras:\n"))

        # Obtener el resumen de la página
        resumen = pagina.content[:longitud] + "..."
        
        # Imprimir el resumen
        print(f"Resumen de '{consulta}':")
        print(resumen)
        
    except wikipedia.exceptions.DisambiguationError as e:
        # Manejar la ambigüedad de la consulta
        print(f"La consulta '{consulta}' es ambigua. Por favor, selecciona una de las siguientes opciones:")
        opciones = e.options
        for i, opcion in enumerate(opciones):
            print(f"{i+1}. {opcion}")
        
        # Solicitar al usuario que seleccione una opción
        seleccion = int(input("Ingresa el número de la opción deseada: "))
        pagina = wikipedia.page(opciones[seleccion-1])
        resumen = pagina.content[:500] + "..."
        print(f"Resumen de '{opciones[seleccion-1]}':")
        print(resumen)
        
    except Exception as e:
        # Manejar otros errores
        print(f"Error: {e}")

