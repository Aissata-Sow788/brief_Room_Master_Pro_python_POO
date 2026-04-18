from basedonnee import BaseDonnee
import bcrypt
from menu import Menu

class Connexion:
    def __init__(self):
        self.db = BaseDonnee()
        self.menu = Menu()
       

    def inscription(self, prenom, nom, email, mdp):
        cursor = None
        try:
            cursor = self.db.connection.cursor(dictionary=True)

            mdp_byte = mdp.encode("utf-8")
            hashed = bcrypt.hashpw(mdp_byte, bcrypt.gensalt())
            query = "insert into utilisateurs (prenom, nom, email, mdp, role) values (%s,%s,%s,%s,%s)"
            cursor.execute(query, (prenom, nom, email, hashed, 'Admin'))
            self.db.connection.commit()
            print(f"Bienvenue {prenom}")

        except Exception as e:
            print("Erreur :", e)

        finally:
            if cursor:
                cursor.close()

    def se_connecter(self, email, mdp):
        cursor = None
        try:
            cursor = self.db.connection.cursor(dictionary=True)

            query = "select * from utilisateurs where email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()

            if not result :
                print("email incorrect")
                return False
            
            hash_pw = result["mdp"]
            if bcrypt.checkpw(mdp.encode("utf-8"),hash_pw.encode("utf-8")):
                self.menu.executer()
                return True
            else:
                print("mot de passe incorrect")
                return False

        except Exception as e:
            print("Erreur :", e)

        finally:
            if cursor:
                cursor.close()