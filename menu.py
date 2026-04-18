from datetime import datetime
from admin import PlanningJournaliere
from groupe import Groupes
from creneaux import Creneaux
from reservation import Reservation
from exportplanning import ExportPlanning


class Menu:
    def __init__(self):
        self.planning = PlanningJournaliere()
        self.groupe = Groupes()
        self.creneau = Creneaux()
        self.reservation = Reservation()
        self.export = ExportPlanning()
      
    

    def executer(self):

        while True:
            print("\n", "-" * 10, "PLANNING", "-" * 10)
            print("1: Ajouter creneaux")
            print("2: Ajouter groupe")
            print("3: Ajouter reservation")
            print("4: Lister creneaux occuper")
            print("5: Lister creneaux libre")
            print("6: Lister creneaux")
            print("7: Lister groupes")
            print("8: Lister reservations")
            print("9: Export planning complet CSV")
            print("10: Annuler reservation")
            print("0: Deconnexion")

            choix = input("Entrez votre choix :")

            match choix:
                case "1":
                    
                    try:
                        heure_debut = input("Entrer l'heure de début (HH:MM) : ")
                        heure_debut = datetime.strptime(heure_debut, "%H:%M").time()

                        heure_fin = input("Entrer l'heure de fin (HH:MM) : ")
                        heure_fin = datetime.strptime(heure_fin, "%H:%M").time()

                        if heure_fin <= heure_debut:
                            raise ValueError("L'heure de fin doit être après l'heure de début.")

                        self.creneau.creneaux(heure_debut, heure_fin)
                    except ValueError:
                        print("Format invalide. Utilisez le format HH:MM (ex: 09:00)")

                case "2":
                    try:
                        nom_groupe = input("nom groupe:").strip().lower()
                        if not nom_groupe.replace(" ","").replace("'","").isalpha():
                            raise ValueError("nom groupe doit etre une chaine caractere")
                        
                        responsable = input("responsable:").strip().lower()
                        if not responsable.replace(" ","").replace("'","").isalpha():
                            raise ValueError("responsable doit etre une chaine caractere")
                        
                        self.groupe.groupes(nom_groupe, responsable)
                    except Exception as e:
                        print("Erreur :", e)

                case "3":
                    try:
                        date_str = input("Entrer la date reservation (YYYY-MM-DD) : ").strip()
                        try:
                            date_reservation = datetime.strptime(date_str, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                        
                        motif = input("motif:").strip().lower()
                        if not motif.replace(" ","").replace("'","").isalpha():
                            raise ValueError("Motif doit etre une chaine caractere")
                        print('------------------Liste des CRENEAUX-------------------')
                        self.creneau.lister_creneau()
                        id_creneau=input("id_creneau: ").strip()

                        if not id_creneau.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                        id_creneau = int(id_creneau)
                        print('------------------Liste des GROUPEs-------------------')
                        self.groupe.lister_groupe()
                        id_groupe=input("id_groupe: ").strip()

                        if not id_groupe.replace(" ", "").isnumeric():

                            raise ValueError("Vous devez saisir un numero")
                        id_groupe = int(id_groupe)
                        self.reservation.reservation(date_reservation, motif, id_creneau, id_groupe)
                    except Exception as e:
                        print("Erreur :", e)

                case "4":
                        print('------------------Liste des reservations-------------------')
                        self.reservation.lister_reservation()
                        try:
                            date_str = input("Entrer la date reservation (YYYY-MM-DD) : ").strip()
                            date = datetime.strptime(date_str, "%Y-%m-%d").date()

                            self.planning.lister_creneaux_occupe(date)
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                case "5": 
                        print('------------------Liste des reservations-------------------')
                        self.reservation.lister_reservation()
                        try:
                            date_str = input("Entrer la date reservation (YYYY-MM-DD) : ").strip()
                            date = datetime.strptime(date_str, "%Y-%m-%d").date()

                            self.planning.lister_creneaux_libre(date)
                        except ValueError:
                            raise ValueError("Format invalide ! Utilise YYYY-MM-DD")
                        
                case "6":
                    self.creneau.lister_creneau()
                case "7":
                    self.groupe.lister_groupe()
                case "8":
                    self.reservation.lister_reservation()
                case "9":
                    self.export.export_planning()
                    self.export.lister_planing()
                case "10":
                        print('------------------Liste des reservations-------------------')
                        self.reservation.lister_reservation()
                        try:
                            id_reservation=input("id_reservation: ").strip()

                            if not id_reservation.replace(" ", "").isnumeric():

                                raise ValueError("Vous devez saisir un numero")
                            id_reservation = int(id_reservation)
                            self.planning.annuler_reservation(id_reservation)
                        except Exception as e:
                            print("Erreur :", e)
                case "0":
                    print("Au revoir 👋")
                    break

                case _:
                    print("erreur saisie")
