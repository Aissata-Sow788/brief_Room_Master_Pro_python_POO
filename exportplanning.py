from basedonnee import BaseDonnee
import csv

class ExportPlanning:
    def __init__(self):
        self.db = BaseDonnee()


    def export_planning(self):
        try:

            cursor = self.db.connection.cursor()

            query = "select c.heure_debut, c.heure_fin, r.motif, g.nom_groupe, g.responsable from reservations r inner join creneaux c on r.id_creneau = c.id inner join groupes g on r.id_groupe = g.id"
            cursor.execute(query)
            resultats = cursor.fetchall()
            

            with open("planing_journalier.csv.", "w", newline="") as fichier_csv:
                writer = csv.writer(fichier_csv) 
                writer.writerow(["heure_debut | heure_fin | nom_groupe | motif | responsable |"])
                writer.writerows(resultats)

        except Exception as e :
            print("Erreur :", e)

        finally:
            cursor.close()
        


    def lister_planing(self):
        with open("planing_journalier.csv.", "r") as fichier_csv:
            ligne = fichier_csv.readline()
            while ligne:
                print(ligne.strip())
                ligne = fichier_csv.readline()




