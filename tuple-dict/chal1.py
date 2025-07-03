First_dict = { "Appareil": "Laptop",
               "Marque": "IBM",
               "Carte mère": "MSI Z490",
               "Carte Graphique":"GeForce RTX 3070",
               "RAM": "16G",
               "Processeur": "Intel core i7-G11",
               "SSD": "1 To" } 
First_dict["RAM"] = "32G"
a = First_dict.keys()      
b = First_dict.values()   
c = First_dict.items() 
print(a)
print(b)
print(c)
#swap keys and values
item = First_dict["Carte Graphique"]                   
First_dict[item] = "Carte Graphique" 
item = First_dict["Processeur"] 
First_dict[item] = "Processeur"
del First_dict["Processeur"]
del First_dict["Carte Graphique"]
# Adding a new key-value pair
First_dict["Système dexploitation"]= "Windows 10"
print(First_dict.items())
notes_eleves = { "Amine": 15.5,
                 "Yassine": 19.0,
                  "Reda": 14.2,
                  "Malak": 8.7,
                  "Manal": 20.0,
                  "Ahmed": 7.5,
                  "Saad": 11.3,
                  "Hannae": 9.8 }
etudiantAdmis = {}
etudiantNonAdmis =  {}
for clé, valeur in notes_eleves.items():
    if notes_eleves[clé] >= 10:
       etudiantAdmis[clé] = valeur
    else :
       etudiantNonAdmis[clé] = valeur
print("Etudiants admis:", etudiantAdmis)
print("Etudiants non admis:", etudiantNonAdmis)
