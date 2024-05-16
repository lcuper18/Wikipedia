from googlesearch import search

def buscar_Bibliografia(consulta):
    try:
        # Realizar la búsqueda en Google
        resultados = search(consulta, num_results=8, lang='es')
        
        # Imprimir los resultados
        print(f"Resultados para '{consulta}':")
        for i, resultado in enumerate(resultados, start=1):
            print(f"{i}. {resultado}")
        
    except Exception as e:
        # Manejar errores
        print(f"Error: {e}")

# Ejemplo de uso
