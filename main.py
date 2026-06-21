import cv2
import time
from src.object_detector import ObjectDetector
from src.gaze_detector import GazeTracker
from src.api_customer import enviar_incidencia

def main():
    # Inicialización de módulos
    detector_obj = ObjectDetector()
    gaze_tracker = GazeTracker()
    
    # Abrir cámara
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    # Variables de control
    tiempo_inicio_distraccion = None
    DURACION_MAXIMA = 10 

    print("Sistema de Proctoring Iniciado...")
    print("Presiona 'q' para salir.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: 
            break

        # 1. Detección de dispositivos (YOLO)
        devices = detector_obj.detect_devices(frame)
        if devices:
            enviar_incidencia("Uso de dispositivo", f"Detectado: {devices}")
            # Opcional: imprimir en consola para feedback inmediato
            print(f"Alerta: Dispositivo detectado {devices}")

        # 2. Detección de mirada (MediaPipe)
        # Si NO está mirando, empezamos a contar el tiempo
        if not gaze_tracker.esta_mirando(frame):
            if tiempo_inicio_distraccion is None:
                tiempo_inicio_distraccion = time.time()
            
            # Comprobar si ya pasaron los 10 segundos
            elif time.time() - tiempo_inicio_distraccion > DURACION_MAXIMA:
                enviar_incidencia("Distracción", "Más de 10s fuera de pantalla")
                print("Alerta: Distracción prolongada")
                tiempo_inicio_distraccion = None # Resetear contador
        else:
            # Si vuelve a mirar al frente, reseteamos el contador
            tiempo_inicio_distraccion = None

        # Visualización
        cv2.imshow('Proctoring - Monitor de seguridad', frame)
        
        # Salir con tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    # Limpieza
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()