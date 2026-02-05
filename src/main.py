from ultralytics import YOLO
import cv2
from DetectionEtiquette import Detection
from Overlay import AfficheFPS, DrawSettings
import time
from config import Settings

# Selectionne la camera dans config.py
camera = cv2.VideoCapture(Settings["camera"]["index"])

# Selectionne le model dans config.py
model = YOLO(Settings["YOLO"]["model_path"])

# Variable temps pour calculer les fps
prev_time = 0

# Créer les variables nécessaire à la pause
paused = False
frame_pause = None

# Créer des booleans pour activer ou désactiver les interfaces
detecte = True
aff_fps = True

# Creation de la fenetre
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)

# Fait défiler les frames
while True:
    if not camera.isOpened():
        print("Erreur : caméra non accessible")

    if paused:
        if detecte:
            Detection(model, frame_pause)
            detecte = not detecte
            DrawSettings(frame_pause)
            cv2.imshow("Webcam", frame_pause)
    else:
        ret, frame = camera.read() # ret = boolean frame valide/invalide
        if not ret:
            break
        frame_pause = frame.copy()
        
        # Dessine l'interface
        DrawSettings(frame)
        
        # Utilise YOLO pour analyser et dessiner les etiquettes sur les frames
        if detecte:
            Detection(model, frame)

        # Temps actuel
        current_time = time.time()

        # Calcul FPS
        fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
        prev_time = current_time

        # Affichage des FPS sur l'image
        if aff_fps:
            AfficheFPS(fps, frame)

        # Affichage de la webcam dans une fenetre ajustable
        cv2.imshow("Webcam", frame)

    # Attente d'une touche
    key = cv2.waitKey(1) & 0xFF 

    """    
    # Active ou désactive l'affichage des settings
    if key == ord(Settings["bindings"]["toggle_settings"]):
        interface = not interface
    """

    # Active ou désactive l'analyse de YOLO sur les frames
    if key == ord(Settings["bindings"]["toggle_YOLO"]):
        detecte = not detecte

    # Affiche les FPS
    if key == ord(Settings["bindings"]["toggle_fps"]):
        aff_fps = not aff_fps
        
    # Met l'affichage en pause
    if key == ord(Settings["bindings"]["pause_frame"]):
        paused = not paused
        detecte = True
        
    # Met fin au programme
    if key == ord(Settings["bindings"]["shutdown"]):
        break

# Mettre fin au programme
camera.release()
cv2.destroyAllWindows()