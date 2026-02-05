# Projet de détection avec YOLO

Ce programme permet l’analyse d’un flux vidéo afin de détecter des étiquettes sur un plateau à l’aide d’un modèle YOLO entrainé sur 100 images.

Il en calcule ensuite le centre et affiche les résultats en temps réel via OpenCV.

Le programme est configurable via un fichier config.py.

## Prérequis

* Version Python ≥ 3.9
* Ultranalytics `pip install ultralytics`
* OpenCV `pip install opencv-python`
* numpy `pip install numpy`

## Utilisation

Lancer le programme sur la racine avec `python src/main.py`.

La caméra utilisée, les touches ainsi que le seuil de confiance sont modifiables en accédant au fichier "config.py".
