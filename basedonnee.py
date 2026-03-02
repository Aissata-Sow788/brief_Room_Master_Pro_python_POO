import mysql.connector

class BaseDonnee:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="MotDePasseFort",
                database="Room_Master_Pro"

            )
        except Exception as e:
            print("Erreur connexion BD :", e)

  

