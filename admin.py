from basedonnee import BaseDonnee

class PlanningJournaliere:
    def __init__(self):
        self.db = BaseDonnee()
    



    def lister_creneaux_occupe(self, date):
        try:
            cursor = self.db.connection.cursor()

            query = "select c.heure_debut, c.heure_fin, g.nom_groupe from reservations r inner join creneaux c on r.id_creneau = c.id inner join groupes g on r.id_groupe = g.id where date_reservation = %s"
            cursor.execute(query, (date,))
            print("========================CRENEAUX OCCUPER===============================")

            result = cursor.fetchall()

            if not result:
                print("cette date reservation n'existe pas")
                return
            
            for row in result:
                print(f" heure_debut : {row[0]}, heure_fin : {row[1]}, nom_groupe : {row[2]} : OCCUPER")
        except Exception as e:
            print("Erreur :", e)

            cursor.close()



    def lister_creneaux_libre(self, date):
        try:
            cursor = self.db.connection.cursor()


            query = "select c.heure_debut, c.heure_fin from creneaux c left join reservations r on r.id_creneau = c.id  and r.date_reservation = %s where r.id_creneau is null"
            cursor.execute(query, (date,))
            print("========================CRENEAUX LIBRE===============================")
            
            for row in cursor.fetchall():
                print(f" heure_debut : {row[0]}, heure_fin : {row[1]} : LIBRE")

        except Exception as e:
            print("Erreur :", e)

            cursor.close()

    def annuler_reservation(self, id_reservation):
        curor = self.db.connection.cursor()

        query = "select * from reservations where id = %s"
        curor.execute(query, (id_reservation,))
        result = curor.fetchone()

        if not result:
            print("cette reservation n'existe pas")
            return

        query = "delete from reservations where id = %s"

        curor.execute(query, (id_reservation,))
        self.db.connection.commit()
        print("Reservation annuler avec succes")




