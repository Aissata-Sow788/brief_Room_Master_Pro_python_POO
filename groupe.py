from basedonnee import BaseDonnee
class Groupes:
    def __init__(self):
        self.db = BaseDonnee()

    def groupes(self, nom_groupe, responsable):
        try: 

            cursor = self.db.connection.cursor()

            query = "insert into groupes (nom_groupe, responsable) values (%s,%s)"
            cursor.execute(query, (nom_groupe, responsable))
            self.db.connection.commit()
            print("Groupe ajouter avec succes")
        
        except Exception as e:
            print("Erreur :", e)

            cursor.close()


    def lister_groupe(self):
        try: 

            cursor = self.db.connection.cursor()

            query = "select * from groupes"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"id groupe : {row[0]}, nom groupe : {row[1]}, responsable : {row[2]}")

        except Exception as e:
            print("Erreur :", e)

            cursor.close()


    

