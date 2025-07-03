chemin = "fichier.txt"
lignes = ["Bonjour", "Voici un exemple", "Fin du fichier"]

with open(chemin, "w", encoding="utf-8") as f:
    for ligne in lignes:
        f.write(ligne + "\n")
