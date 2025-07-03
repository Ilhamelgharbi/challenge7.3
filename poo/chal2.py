from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    @abstractmethod
    def afficher_info(self):
        print(f"le nom est {self.nom}, le prénom est {self.prenom} et l'âge est {self.age} ans.")
class Etudiant(Person):
    def __init__ (self ,nom, prenom, age, matricule, notes=None):
        super().__init__(nom, prenom, age)
        self.matricule = matricule
        self.notes = notes if notes is not None else []
    def ajouter_note(self, note):
        self.notes.append(note)
    def moyenne(self):
        if self.notes:
            return sum(self.notes) / len(self.notes)
        return 0
    def afficher_info(self):
        super().afficher_info()
        print(f"Le matricule est {self.matricule} et les notes sont {self.notes}.")
class Enseignant(Person):
    def __init__(self, nom, prenom, age, specialite, salaire):
        super().__init__(nom, prenom, age)
        self.specialite = specialite
        self._salaire = salaire
    def afficher_info (self):
        super().afficher_info()
        print(f"La spécialité est {self.specialite} et le salaire est {self.salaire}€.")
    @property
    def getsalaire(self):
        return self._salaire

    @salaire.setter
    def setsalaire(self, valeur):
        if valeur >= 0:
            self._salaire = valeur
        else:
            print("Erreur : salaire ne peut pas être négatif")
class Ecole:
        def __init__(self, nom, liste_etudiants=None, liste_enseignants=None):
            self.nom = nom
            self.liste_etudiants = liste_etudiants if liste_etudiants is not None else []
            self.liste_enseignants = liste_enseignants if liste_enseignants is not None else []
        def ajouter_etudiant(self , etudiant: Etudiant):
            self.liste_etudiants.append(etudiant)

        def ajouter_enseignant(self , enseignant: Enseignant):
            self.liste_enseignants.append(enseignant)
        def afficher_tous_les_membres(self):
            print(f"École: {self.nom}")
            print("\nListe des étudiants:")
            for etudiant in self.liste_etudiants:
                etudiant.afficher_info()
            print("\nListe des enseignants:")
            for enseignant in self.liste_enseignants:
                enseignant.afficher_info()
def main():
     ecole = Ecole ("École de Programmation")
     etudiant = Etudiant("ilham", "elgharbi", 24 , "12345" , [15, 18, 20]) 
     etudiant.ajouter_note(17)
     etudiant.afficher_info()
     ecole.ajouter_etudiant(etudiant)
     enseignant = Enseignant("Dr. Smith", "John", 40, "Informatique", 3000)
     enseignant.setsalaire = 3500  
     enseignant.afficher_info()
     ecole.ajouter_enseignant(enseignant)
     ecole.afficher_tous_les_membres()
if __name__ == "__main__":
    main()
