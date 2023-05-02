# importe ABC (abstractClass) depuis le module abc 
from abc import ABC

# Création de la class User, qui est étendu à la class ABC
class User (ABC):
    
    # Création du constructeur User, qui prend 2 paramètres
    def __init__ (self,
                  user_name : str, 
                  password : str) -> None: 
        
        # User_name
        self._user_name = user_name
        
        # Password
        self._password = password
        
         # Person_is_connected est faux
        self._person_is_connected = False
    
    # Création d'une méthode connect avec 2 paramètres, qui dit si un utilisaeur est connecté ou pas via un booléen
    @classmethod
    def connect (self, 
                 user_name : str, 
                 password : str) -> bool :
        
        # Si user_name et password correspondent
        if (self._user_name == user_name and self._password == password) :
            
            # Affiche bonjour user_name ! utilisateur connecte
            print (f"bonjour {self._user_name} ! utilisateur connecte")
            
            # Person_is_connected est vrai
            self._person_is_connected = True
            
            # Retourne Person_is_connected
            return (self._person_is_connected)
        
        # Sinon on retourne, une erreur de nom utilisateur ou de mot de passe
        else :
            
            # Affiche erreur de nom utilisateur ou de mot de passe
            print ("erreur de nom utilisateur ou de mot de passe")

            # Retourne faux
            return (False)
        
    # Création d'une méthode disconnect sans paramètres, qui dit que l'utilisateur est déconnecté
    @classmethod        
    def disconnect (self) -> None : 
        
        # Person_is_connected est faux
        self._person_is_connected = False
        
        # Affiche deconnexion de user_name
        print (f"deconnexion de {self._user_name}")