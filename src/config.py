Settings = {
    "camera": {
        "index": 0 # Index de la camera (0 pour la caméra par défaut)
    },

    "bindings": {
        #"toggle_settings": "s",
        "toggle_YOLO": "y", # Permet d'activer ou désactiver l'analyse de YOLO
        "toggle_fps": "f", # Permet d'afficher ou de masquer le compteur de FPS
        "pause_frame": "p", # Permet de mettre en pause ou de reprendre l'affichage des frames
        "shutdown": "q" # Permet de fermer l'application
    },

    "YOLO": {
        "model_path": "../model/best.pt", # Chemin vers le modèle YOLO
        "confidence_threshold": 0.4 # Seuil de confiance pour les détections (entre 0 et 1)
    },

    "display": {
        "window_name": "Detection",
        "show_settings": True,
        "show_fps": True
    }
}