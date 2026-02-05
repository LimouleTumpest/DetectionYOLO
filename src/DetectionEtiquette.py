from ultralytics import YOLO
import cv2

# model = modèle YOLO utilisé, image = frame exploitée
def Detection(model, image):
    
    results = model(image)
    detections = []
    result = results[0]

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0]) #conf = confidence, entre 0 (pas fiable) et 1 (certain)
        cls  = int(box.cls[0]) #cls = class, identifiant correspondant à quelque chose dans un modèle. Ici il faudra définir l'identifiant pour les étiquettes plus tard
        if conf >= 0.40:
            detections.append((int(x1), int(y1), int(x2), int(y2), conf, cls))

    for (x1, y1, x2, y2, conf, cls) in detections:
        # Calcul du centre
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        # Dessiner le rectangle et les coordonnées
        if cls == 0 :
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

            cv2.putText(
                image,
                f"Face / Centre({cx},{cy})",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1
            )

        else :
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

            cv2.putText(
                image,
                f"Dos / Centre({cx},{cy})",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                1
            )

        # Dessiner le centre
        cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)