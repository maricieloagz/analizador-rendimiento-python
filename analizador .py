import time
def tarea_pesada():
    """Simula un proceso que consume tiempo"""
    resultado = 0
    for i in range(1_000_000):
        resultado += i
    return resultado

def ejecutar_prueba():
    print("--- Iniciando Análisis de Rendimiento ---")
    
    inicio = time.time()
    tarea_pesada()
    fin = time.time()
    
    tiempo_total = fin - inicio
    print(f"La tarea tardó: {tiempo_total:.4f} segundos")
    print("--- Análisis Finalizado con éxito ---")

if __name__ == "__main__":
    ejecutar_prueba()