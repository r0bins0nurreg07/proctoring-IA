import cv2
# Importamos específicamente el submódulo que contiene la lógica
from mediapipe.python.solutions import face_mesh as mp_face_mesh

class GazeTracker:
    def __init__(self):
        # Usamos el alias importado directamente
        self.face_mesh = mp_face_mesh.FaceMesh(
            static_image_mode=False,
            refine_landmarks=True,
            max_num_faces=1
        )

    def esta_mirando(self, frame):
        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # self.face_mesh ahora es la instancia correcta
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]
            nose = face_landmarks.landmark[1]
            nose_x = nose.x * w
            
            margin = w * 0.2
            centro = w / 2
            
            if abs(nose_x - centro) < margin:
                return True
        
        return False