import os

dossier = "mon_dossier"
contenu_total = ""

for fichier in os.listdir(dossier):
    if fichier.endswith(".txt"):
        chemin = os.path.join(dossier, fichier)
        with open(chemin, "r", encoding="utf-8") as f:
            contenu_total += f.read() + "\n"

print(contenu_total)
