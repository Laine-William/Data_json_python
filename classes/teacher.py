# importe la class Person
from classes.person import Person

# importe la List depuis le module typing 
from typing import List

# Création de la class Teacher, qui est étendu à la class Person
class Teacher (Person) :

    # Initialise la liste les leçons à l'aide de la List, que l'on stock dans un tableau
    list_lessons : List [str] =  ["HTML", "CSS", "Javascript", "PHP", "Symfony", "Python", "Design UX/UI", "Marketing", "PAO"]

    # Création du constructeur Teacher, qui prend 5 paramètres
    def __init__ (self, 
                  first_name : str, 
                  last_name : str, 
                  list_lessons : List [str] = [], 
                  user_name: str = "", 
                  password: str = "") -> None : 
        
        # Appel le constructeur parent de la class Person avec la méthode super, qui initialise les 4 attributs
        super ().__init__ (first_name, 
                           last_name, 
                           user_name, 
                           password)
        
        # List_lessons
        self._list_lessons : List [str] = list_lessons

    # Acceseur list_lessons sans paramètres, qui retourne la liste des leçons
    @property
    def list_lessons (self) -> List [str] :
        
        # Retourne la liste des leçons
        return (self._list_lessons)
    
    # Modificateur list_lessons avec un paramètre new_list_lesson, qui modifie la liste des leçons
    @list_lessons.setter
    def list_lessons (self, 
                      new_list_lesson : str) -> None : 
        
        # Si new_list_lesson est dans la list_lesson
        if (new_list_lesson in self._list_lessons) :
            
            # Ajoute une nouvelle leçon dans _list_lessons 
            self._list_lessons.append (new_list_lesson)
        
        # Sinon on retourne, matiere inconnue
        else :
            
            # affiche matiere inconnue
            print ("matiere inconnue")
    
    # Création d'une méthode update_lessons avec 1 paramètres new_listlesson, qui met à jour la liste des leçons
    @classmethod
    def update_lessons (cls, 
                        new_list_lesson : str) -> None :
        
        cls._list_lessons = new_list_lesson

    # Création d'une méthode work sans paramètres, qui donne la leçon enseignée
    @classmethod
    def work (self) -> str :
        
        # Retourne j'enseigne les matières suivantes 
        return ("j'enseigne les matières suivantes : {}" .format (", " .join (self._list_lessons)))

    # Création d'une méthode connect_teacher avec 2 paramètres, qui dit si un enseignant est connecté ou pas via un booléen
    @classmethod
    def connect_teacher (self, 
                         user_name : str,
                         password : str) -> bool :
        
        # Si la méthode connect de la class parent Person contient un user-name et un password
        if (super ().connect (user_name, 
                              password)) :
            
            # Affiche enseignant connecte
            print ("enseignant connecte")
            
            # Retourne vrai
            return (True)
        
        # Sinon on retourne enseignant non connecte
        else :    
            
             # Affiche enseignant non connecte
            print ("enseignant non connecte")
        
            # Retourne faux
            return (False)   
    
    # Création d'une méthode disconnect_teacher sans paramètres, qui dit que l'enseignant est déconnecté
    @classmethod
    def disconnect_teacher (self) -> None :
        
        # Appel la méthode disconnect de la class Person
        super ().disconnect ()
        
        # Affiche enseignant deconnecte
        print ("enseignant deconnecte")