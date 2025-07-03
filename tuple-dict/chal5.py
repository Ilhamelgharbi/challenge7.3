etudiant_info = ("Prénom : \"Yasmine\"", "Âge : 22", "Filière : \"Informatique\"", "Moyenne générale : 17.4")
for element in etudiant_info:
    print(element)
slice = etudiant_info[0:2]
for element in slice:
    print(element)
print(10*"*" , "\n tuple final : ")
tuple_info = "Mention : \"tres bien \"", "Année d'obtention du diplôme : 2024"
tuple_finl = etudiant_info + tuple_info
for element in tuple_finl:
    print(element)
