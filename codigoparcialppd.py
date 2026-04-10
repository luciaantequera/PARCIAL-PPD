import threading
import queue
import time
import random

# 1. El Buffer (Cola de almacenamiento)
# Al instanciar Queue() sin un maxsize, la cola puede crecer indefinidamente.
# Esto cumple el requisito: "no se pierda ninguna imagen, incluso en carga máxima".
buffer_imagenes = queue.Queue()

def recepcion_satelite(nombre_satelite, total_imagenes):
    """
    Etapa 1: Productor. Simula un satélite que envía imágenes de forma impredecible.
    """
    for i in range(total_imagenes):
        imagen_id = f"IMG-{nombre_satelite}-0{i+1}"
        
        # Simular la tasa de llegada impredecible (rápido, lento o pausas)
        tiempo_llegada = random.uniform(0.1, 1.0)
        time.sleep(tiempo_llegada)
        
        # Almacenamiento temporal seguro
        buffer_imagenes.put(imagen_id)
        print(f"[ RECEPCIÓN] {nombre_satelite} recibió y almacenó: {imagen_id} (Cola: {buffer_imagenes.qsize()} en espera)")
        
    print(f"[ FIN TRANSMISIÓN] {nombre_satelite} ha terminado de enviar imágenes.")

def analista_automatico(nombre_analista):
    """
    Etapa 2: Consumidor. Simula un proceso que toma imágenes de la cola y realiza cálculos complejos.
    """
    while True:
        try:
            # Obtiene una imagen de la cola. 
            # Si no hay, el analista se queda "esperando" sin consumir CPU.
            # El timeout asegura que los hilos puedan cerrarse cuando ya no haya trabajo.
            imagen = buffer_imagenes.get(timeout=5)
            
            print(f"  [ PROCESANDO] {nombre_analista} comenzó a analizar: {imagen}...")
            
            # Simular cálculos muy complejos (tardan mucho más que la recepción)
            tiempo_procesamiento = random.uniform(2.0, 5.0)
            time.sleep(tiempo_procesamiento)
            
            print(f"  [ COMPLETADO] {nombre_analista} finalizó el análisis de: {imagen}")
            
            # Indica a la cola que la tarea extraída ya fue procesada totalmente
            buffer_imagenes.task_done()
            
        except queue.Empty:
            # Si pasan 5 segundos sin que llegue nada nuevo, el analista se desconecta
            print(f"[ DESCONEXIÓN] {nombre_analista} inactivo por falta de imágenes. Apagando.")
            break

# --- SIMULACIÓN DEL SISTEMA ---
if __name__ == "__main__":
    print("=== INICIANDO CENTRO DE PROCESAMIENTO SATELITAL ===\n")
    
    # Listas para guardar los hilos
    hilos_satelites = []
    hilos_analistas = []

    # Crear y arrancar hilos de recepción
    for i in range(2):
        hilo = threading.Thread(target=recepcion_satelite, args=(f"SATELITE-{i+1}", 4))
        hilos_satelites.append(hilo)
        hilo.start()

    # Crear y arrancar hilos de procesamiento 
    for i in range(3):
        hilo = threading.Thread(target=analista_automatico, args=(f"ANALISTA-{i+1}",))
        hilos_analistas.append(hilo)
        hilo.start()

    # Esperar a que los satélites terminen de emitir
    for hilo in hilos_satelites:
        hilo.join()
        
    print("\n[ℹ ESTADO] Recepción finalizada. Esperando a que los analistas limpien el acumulado...\n")

    # buffer_imagenes.join() bloquea el programa principal hasta que
    # por cada .put() haya habido un .task_done() exitoso.
    buffer_imagenes.join()
    
    print("\n=== TODAS LAS IMÁGENES HAN SIDO PROCESADAS CON ÉXITO ===")
