# src/api_customer.py
import time

def enviar_incidencia(tipo_evento, detalle):
    """
    Función simulada (Mock) para probar el sistema sin backend.
    """
    print(f"\n--- [SIMULACIÓN API] ---")
    print(f"Tipo: {tipo_evento}")
    print(f"Detalle: {detalle}")
    print(f"Timestamp: {time.ctime()}")
    print(f"------------------------\n")
    
    # Retornamos True para que el main.py crea que todo salió bien
    return True