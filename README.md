Procesador Digital de Imágenes Satelitales
Simulación de Concurrencia y Sincronización en Python

Este proyecto implementa un sistema de procesamiento de imágenes satelitales usando Programación Paralela y Distribuida. Se utiliza el patrón de diseño Productor-Consumidor para gestionar flujos de datos y cargas de trabajo intensivas mediante hilos (threads) y diferentes estructuras de datos.

1) Fundamentos Teóricos
El sistema demuestra tres conceptos clave de la computación paralela:

Desacoplamiento de Procesos: El uso de una queue.Queue actúa como un monitor que desacopla la velocidad de recepción (productores) de la velocidad de procesamiento (consumidores).

Sincronización: Implementa exclusión mutua implícita para el acceso a recursos compartidos, evitando condiciones de carrera.

Gestión de Carga: La cola permite manejar picos de tráfico sin pérdida de datos, garantizando un procesamiento FIFO (First In, First Out).

2) Especificaciones Técnicas
Librerías: threading, queue, time, random (Standard Library).

Concurrencia: Multithreading basado en el modelo de hilos de usuario gestionados por el intérprete.

Seguridad: Uso de colas bloqueantes con métodos .get() y .put() que garantizan la integridad de los datos entre hilos.

3) Guía de Ejecución
Entorno: Requiere Python 3.6+.

Comando:

Bash
python procesador_satelital.py
4) Análisis del Ciclo de Vida (Logs)
Al ejecutar el script, se puede observar el comportamiento dinámico del sistema:

[ RECEPCIÓN]: El hilo productor ha depositado un objeto en el buffer. Se muestra el tamaño actual de la cola (qsize).

[ PROCESANDO]: Un hilo consumidor ha tomado un recurso. Note que el procesamiento es concurrente (varios analistas trabajan a la vez).

[ COMPLETADO]: Finalización de la tarea intensiva en CPU/Tiempo.

[ DESCONEXIÓN]: Aplicación de un timeout de 5 segundos para el cierre controlado de hilos inactivos.

5) Configuración de Parámetros
Para realizar pruebas de estrés o análisis de escalabilidad, hay que modificar el bloque if __name__ == "__main__"::

Escalabilidad Horizontal: Es necesario aumentar el rango en el bucle de hilos_analistas para observar cómo disminuye el tiempo total de vaciado de la cola.

Carga de Trabajo: Hay que ajustar el parámetro total_imagenes en recepcion_satelite para variar el volumen de datos de entrada.
