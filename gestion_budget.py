import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
with sqlite3.connect("budget.db") as connection:
    cursor = connection.cursor()
    
cursor.execute(
    "CREATE TABLE IF NOT EXISTS budget (id INTEGER PRIMARY KEY AUTOINCREMENT,Loyer TEXT, Manger TEXT, Transport TEXT, Loisir TEXT, Tontine TEXT, Factures_courant TEXT, Salaire TEXT, Business TEXT, tontine TEXT)")

class GestionBudget:
    
    
    def __init__(self):
        print("l'application de gestion de budget")


    def Depense_Total(self):
        print("Remplissez la liste de vos dépense:")
        Type_de_depense = ("Loyer, Manger, Transport, Loisir, Tontine, Factures_courant")
        print("que voulez-vous ajouter:"+str(Type_de_depense))
        Loyer = int(input("Donnez le montant du loyer:"))
        Manger = int(input("Le bilan du mangé:"))
        Transport = int(input("Donnez la somme des tarifs du transprt:"))
        Loisir = int(input("Donnez la somme effectuée du Loisir:"))
        Tontine = int(input("La somme versée de la Tontine:"))
        Factures_courant = int(input("Donnez la somme des factures:"))
        requette = "CREATE TABLE Depense_Total (id INTEGER PRIMARY KEY AUTOINCREMENT, Loyer TEXT, Manger TEXT, Transport TEXT, Loisir TEXT, Tontine TEXT, Factures_courant TEXT)"
        requette = "INSERT INTO Depense_Total('loyer', 'Manger', 'Transport', 'Loisir', 'Tontine', 'Factures_courant') VALUES (?,?,?,?,?,?)"
        cursor.execute(requette, (Loyer, Manger, Transport, Loisir, Tontine, Factures_courant))
        connection.commit()
        print("les dépenses sont ajoutées")
        Depense_Totale = Loyer+Manger+Transport+Loisir+Tontine+Factures_courant
        print("la somme dépensé" +str(Depense_Totale)+ "Franc(CFA)")
        if Depense_Totale > 1000000:
            print("Votre dépense est hyper élevé")
        else:
            print("vous avez bien géré vos dépense")
            
    def Revenu_Total(self):
        print("Remplissez la liste de vos dépense:")
        Type_de_Revenu = ("Salaire, Business, tontine")
        print("que voulez-vous savoir:"+str(Type_de_Revenu))
        Salaire = int(input("La somme de votre salaire:"))
        Business = int(input("la somme gagnée du business:"))
        Tontinee = int(input("La somme gagnée à la tontine:"))
        requette = "CREATE TABLE Revenu_Total (id INTEGER PRIMARY KEY AUTOINCREMENT, Salaire TEXT, Business TEXT, Tontinee TEXT)"
        requette = "INSERT INTO Revenu_Total('Salaire', 'Business', 'tontine') VALUES(?,?,?)"
        cursor.execute(requette, (Salaire, Business, Tontinee))
        connection.commit()
        print("vos revenus ont été consulté")
        Revenu_Totale = Salaire+Business+Tontinee
        print("La somme des revenus" +str(Revenu_Totale)+ "Franc(CFA)")
        if Revenu_Totale > 500000:
            print("Vous pouvez souffler")
        else:
            print("vous avez pratiquement rien gagner")
            
    def difference(self):
        Depense_Totale = ("loyer+Manger+Transport+Loisir+Tontine+Factures_courant")
        Revenu_Totale = ("Salaire+Business+tontine")
        self.La_difference = Revenu_Totale - Depense_Totale
        print("Donnez la difference effectuée:")
        if Revenu_Totale > Depense_Totale:
            print("Vous avez bien géré vos transactions")
        elif Revenu_Totale < Depense_Totale:
            print("vous n'avez pas bien géré vos transactions")
        else:
            print("On a un égalité de somme entre les deux")
            
    def Le_tarif_des_budgets(self):
        choix =""
        print("       Bonjour comment vous allez ?      ")
        print("                                         ")
        print("   A) Remplissez vos dépenses")
        print("   B) Consultez vos revenus")
        print("   C) Vérifier la difference entre la dépense et le revenu")
        print("   0) quitter l'application")
        choix = input("quel est votre désire:\n")
        if choix == "A":
            self.Depense_Total()
            self.Le_tarif_des_budgets()
        elif choix == "B":
            self.Revenu_Total()
            self.Le_tarif_des_budgets()
        elif choix == "C":
            self.La_difference()
            self.Le_tarif_des_budgets()
        elif choix == "0":
            print("Quitter")
            exit()
        else:
            print("votre choix n'est pas reconnu" )
            

geestion_budget = GestionBudget()
geestion_budget.Le_tarif_des_budgets()