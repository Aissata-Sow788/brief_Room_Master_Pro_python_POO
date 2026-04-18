from connexion import Connexion

class Authentification:
    def __init__(self):
        self.connect = Connexion()
       

    def connexion(self):

        print("=================Connexion===============")
        print("1: Inscription")
        print("2: Se connecter")

        choix = input("Entrez votre choix :")

        match choix:
            case "1":
                    try:
                        prenom = input("prenom:").strip().lower()
                        if not prenom.replace(" ","").replace("'","").isalpha():
                            raise ValueError("prenom doit etre une chaine caractere")
                        
                        nom = input("nom:").strip().lower()
                        if not nom.replace(" ","").replace("'","").isalpha():
                            raise ValueError("nom doit etre une chaine caractere")
                        
                        email = input("email:").strip().lower()
                        if not email.replace(" ","").replace("'",""):
                            raise ValueError("email doit etre une chaine caractere")
                        
                        mdp = input("mdp:").strip().lower()
                        if not mdp.replace(" ","").replace("'","").isalpha():
                            raise ValueError("mdp doit etre une chaine caractere")
                        
                        self.connect.inscription(prenom, nom, email, mdp)
                    except Exception as e:
                        print("Erreur :", e)

            case "2":
                    try:
                        email = input("email:").strip().lower()
                        if not email.replace(" ","").replace("'",""):
                            raise ValueError("email doit etre une chaine caractere")
                        
                        
                        mdp = input("mdp:").strip().lower()
                        if not mdp.replace(" ","").replace("'","").isalnum():
                            raise ValueError("mdp doit etre une chaine caractere")
                        else:
                            self.connect.se_connecter(email, mdp)
                    except Exception as e:
                        print("Erreur :", e)       

auth = Authentification()
auth.connexion()

        
    
        