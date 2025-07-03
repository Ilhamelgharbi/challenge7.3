class CompteBancaire:

    def __init__ (self, nom_proprietaire, solde=0):
        self.nom_proprietaire= nom_proprietaire
        self.solde = solde
    
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Montant déposé: {montant}€")
        else:
            print("Le montant doit être positif.")
        return self.solde

    def retirer(self, montant):
        if montant >0 and montant <self.solde:
            self.solde-=montant
            print(f"Montant retiré: {montant}€")
        else :
            print("Le montant doit être positif et inférieur au solde.")
        return self.solde
    def afficher_solde(self):
        print(f"Solde actuel de {self.nom_proprietaire}: {self.solde}€")
def main():
   compte = CompteBancaire("ilham el gharbi ", 10000)
   compte.afficher_solde()
   compte.deposer(500)
   compte.retirer(200)
   compte.afficher_solde()
   compte.retirer(20000) 
if __name__ == "__main__":
    main()
   