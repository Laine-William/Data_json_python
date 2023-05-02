# importe la class User
from classes.user import User

# Création de la class Person, qui est étendu à la class User
class Person (User) :

    # Création du constructeur Person, qui prend 4 paramètres
    def __init__ (self, 
                  first_name : str, 
                  last_name : str, 
                  user_name : str, 
                  password: str) -> None : 
        
        # Appel le constructeur parent de la class User avec la méthode super, qui initialise les 2 attributs
        super ().__init__ (user_name, 
                           password)
        
        # First_name
        self._first_name = first_name
        
        # Last_name
        self._last_name = last_name
    
    # Acceseur first_name sans paramètres, qui retourne le prénom
    @property
    def first_name (self) -> str :
        
        # Retourne le first_name
        return (self._first_name)
    
    # Modificateur first_name avec un paramètre new_first_name, qui modifie la prénom
    @first_name.setter
    def first_name (self, 
                    new_first_name : str) -> str :
        
        # First_name est un nouveau prénom
        self._first_name = new_first_name

    # Acceseur last_name sans paramètres, qui retourne le nom
    @property
    def last_name (self) -> str :
        
        # Retourne le last_name
        return (self._last_name)
    
    # Modificateur last_name avec un paramètre new_last_name, qui modifie la nom
    @last_name.setter
    def last_name (self, 
                   new_last_name : str) -> str :
        
        # Last_name est un nouveau nom
        self._last_name = new_last_name

    # Création d'une méthode work sans paramètres, qui donne je travail
    @classmethod
    def work (self) -> str :
        
        # Retourne je travail
        return ("je travail")