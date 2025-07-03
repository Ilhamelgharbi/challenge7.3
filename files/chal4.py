import os

principal = "repertoire_principale"
sous_repertoires = ["docs", "images", "logs"]

os.mkdir(principal)

for nom in sous_repertoires:
    os.mkdir(os.path.join(principal, nom))
