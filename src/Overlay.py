import cv2
from config import Settings

def AfficheFPS(fps, frame):
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (5, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        1
    )

def DrawSettings(frame):
    espace = 70
    parametres = [f"[{Settings['bindings']['toggle_YOLO']}] YOLO",
                  f"[{Settings['bindings']['toggle_fps']}] fps",
                  f"[{Settings['bindings']['pause_frame']}] pause",
                  f"[{Settings['bindings']['shutdown']}] stopper"]
    for parametre in parametres:
        cv2.putText(
            frame,
            parametre,
            (5,espace),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4,
            (0,0,255),
            1
        )
        espace += 50