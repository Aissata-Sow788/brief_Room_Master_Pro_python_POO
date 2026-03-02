from basedonnee import BaseDonnee
class Creneaux:
    def __init__(self):
        self.db = BaseDonnee()
     

    def creneaux(self, heure_debut, heure_fin):
        try:

            cursor = self.db.connection.cursor()

            query = "insert into creneaux (heure_debut, heure_fin) values (%s,%s)"
            cursor.execute(query, (heure_debut, heure_fin))
            self.db.connection.commit()
            print("Creneux ajouter avec succes")

        except Exception as e:
            print("Erreur :", e)

            cursor.close()

    def lister_creneau(self):
        try:

            cursor = self.db.connection.cursor()

            query = "select * from creneaux"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"id creneau : {row[0]}, heure debut : {row[1]}, heure fin : {row[2]}")

        except Exception as e:
            print("Erreur :", e)

            cursor.close()