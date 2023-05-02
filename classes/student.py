# importe la class Person
from classes.person import Person

# importe la List depuis le module typing 
from typing import List

# Création de la class Studenrt, qui est étendu à la class Person
class Student (Person) :
    
    # Initialise un bonus_point a 0
    bonus_point = 0

    # Création du constructeur Student, qui prend 6 paramètres
    def __init__ (self, 
                  first_name : str, 
                  last_name : str, 
                  notes : List [int] = None, 
                  average_student : int = 0, 
                  user_name : str = "", 
                  password : str = "") -> None :
        
        # Appel le constructeur parent de la class Person avec la méthode super, qui initialise les 4 attributs
        super ().__init__ (first_name, 
                           last_name, 
                           user_name, 
                           password)
        
        # Si _notes n'existent pas 
        if (notes is None) :
            
            # Initialise les notes dans un tableau 
            self._notes = []
        
        # Sinon on retourne les notes
        else :
            
            # Notes
            self._notes = notes
        
        # Average_student
        self._average_student = average_student
    
    # Acceseur notes sans paramètres, qui retourne les notes
    @property
    def notes (self) -> List [int] :
        
        # Retourne les notes
        return (self._notes)
    
    # Modificateur notes avec un paramètre new_note, qui modifie la note
    @notes.setter
    def notes (self, 
               new_note : int) -> None :
        
        # Gère l'erreur de la nouvelle note
        try :
        
            # New_note est une nouvelle note entière
            new_note = int (new_note)
            
            # Si new_note est comprise entre 0 et 20 
            if (0 <= new_note <= 20) :
                
                # Ajoute une nouvelle note dans _notes
                self._notes.append (new_note)
        
        # Message d'erreur
        except ValueError:
        
            # Affiche la saisie n'est pas valide
            print ("la saisie n'est pas valide")
        
        # Retourne la nouvelle note
        return (new_note)

    # Création d'une méthode average sans paramètres, qui calcul la moyenne de l'étudiant
    @classmethod
    def average (self) -> None :
        
        # Average_student est la somme des notes en plus du bonus_point
        self._average_student = (sum (self._notes) / len (self._notes) + self.bonus_point)

    # Création d'une méthode bonus_point_average sans paramètres, qui donne un point bonus à l'étudiant
    @classmethod
    def bonus_point_average (cls) -> None :
        
        # Tant que c'est vrai, on continue
        while (True) :
            
            # Entrer le nombre de bonus point a donner
            bonus_point = input ("\n entrez le nombre de points bonus a donner : ")
            
            # # Gère l'erreur du point bonus
            try :
                
                # Bonus_point est une nouveau point bonus entier
                bonus_point = int (bonus_point)
                
                # Si bonus_point est supérieur ou égal à 0
                if (bonus_point >= 0) :
                    
                    # Bonus_point
                    cls.bonus_point = bonus_point
                    
                    # Arrete
                    break
                
                # Sinon on retourne le nombre de points bonus doit-etre un entier positif ou nul
                else :
                    
                    # Affiche le nombre de points bonus doit-etre un entier positif ou nul
                    print ("\n le nombre de points bonus doit-etre un entier positif ou nul")
            
            # Message d'erreur        
            except ValueError :
                
                # Affiche le nombre de points bonus doit-etre un entier positif ou nul
                print ("\n le nombre de points bonus doit-etre un entier positif ou nul")

    # Création d'une méthode work sans paramètres, qui donne la moyenne de l'étudiant
    @classmethod
    def work (self) -> str :
        
        # Retourne j'ai une moyenne generale
        return ("j'ai une moyenne generale : {}".format ("".join (str (self._average_student))))

    # Création d'une méthode connect_student avec 2 paramètres, qui dit si un étudiant est connecté ou pas via un booléen
    @classmethod
    def connect_student (self,
                         user_name : str,
                         password: str) -> bool :
        
        # Si la méthode connect de la class parent Person contient un user-name et un password
        if (super ().connect (user_name, 
                              password)) :
            
            # Affiche etudiant connecte
            print ("etudiant connecte")
            
            # Retourne vrai
            return (True)
        
        # Sinon on retourne étudiant non connecte
        else :    
            
            # Affiche etudiant non connecte
            print ("etudiant non connecte")
        
            # Retourne faux
            return (False)
        
    # Création d'une méthode disconnect_student sans paramètres, qui dit que l'étudiant est déconnecté
    @classmethod
    def disconnect_student (self) -> None :
        
        # Appel la méthode disconnect de la class Person
        super ().disconnect ()
        
        # Affiche etudiant deconnecte
        print ("etudiant deconnecte")