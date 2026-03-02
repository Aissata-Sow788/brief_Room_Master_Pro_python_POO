from basedonnee import BaseDonnee

class Reservation:
    def __init__(self):
        self.db = BaseDonnee()



    def reservation(self, date_reservation, motif, id_creneau, id_groupe):
        try:

            cursor = self.db.connection.cursor()

            query = "select * from creneaux where id = %s"
            cursor.execute(query, (id_creneau,))
            result1 = cursor.fetchone()

            if not result1:
                print("cette creneaux n'exite pas")
                return
            
            query = "select * from groupes where id = %s"
            cursor.execute(query, (id_groupe,))
            result2 = cursor.fetchone()

            if not result2:
                print("cette groupe n'exite pas")
                return

            query = "select id from reservations where date_reservation = %s and id_creneau = %s"
            cursor.execute(query, (date_reservation, id_creneau))
            result = cursor.fetchone()

            if result:
                print("Ce creneau est deja occuper pour cette date")
                return
        
            query = "insert into reservations (date_reservation, motif, id_creneau, id_groupe) values (%s,%s,%s,%s)"
            cursor.execute(query, (date_reservation, motif, id_creneau, id_groupe))
            self.db.connection.commit()
            print("Reservation ajouter avec succes")

        except Exception as e:
            print("Erreur :", e)

            cursor.close()


    def lister_reservation(self):
        try:

            cursor = self.db.connection.cursor()

            query = "select * from reservations"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"id reservation : {row[0]}, date reservation : {row[1]}, motif : {row[2]}, id_groupe : {row[3]}")
        except Exception as e:
            print("Erreur :", e)

            cursor.close()
