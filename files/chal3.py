import os
import shutil

source = "source_dossier"
destination = "destination_dossier"
os.makedirs(destination, exist_ok=True)

for fichier in os.listdir(source):
    if fichier.endswith(".csv"):
        shutil.copy(os.path.join(source, fichier), destination)
