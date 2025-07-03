import os

chemin = "mon_dossier/config.yaml"

if os.path.exists(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print("Le fichier config.yaml n'existe pas.")
