import json

from random import randint

from classes.encoder import Encoder
from classes.student import Student
from classes.teacher import Teacher
from classes.user import User

# Exercice 1
# number_students = int (input ("\n Quel est le nombre d'eleves dans votre promotion : "))

# students = []

# for i in range (number_students) :
    
#     first_name = input ("\n Donner le prenom de l'eleve {} : " .format (i + 1))
#     last_name = input (" Donner le nom de l'eleve {} : " .format (i + 1))
    
#     student = Student (first_name, 
#                        last_name)
    
#     notes = []
    
#     for j in range (5) :
        
#         student.notes.append (randint (0, 20))

#     student.bonus_point_average ()

#     student.average ()

#     students.append (student)

# with open ("./data/students.json", "w") as file_student :
    
#     json.dump ([{'Pseudo': student.user_name,
#                  'Mot_de_passe': student.password,
#                  'Prenom': student.first_name, 
#                  'Nom': student.last_name, 
#                  'Notes': student.notes, 
#                  'Point_bonus': student.bonus_point, 
#                  'Moyenne_des_notes': student.average_student} 
#                 for student in students], 
#                file_student, 
#                indent = 4)

# Exercice 2
# teachers = []

# number_teacher = int (input ("Combien d'enseignants pour la classe ? "))

# for i in range (number_teacher) :
    
#     first_name = input ("Prénom de l'enseignant {} : " .format (i + 1))
#     last_name = input ("Nom de l'enseignant {} : " .format (i + 1))
    
#     teacher = Teacher (first_name, 
#                        last_name)
    
#     list_lessons = [] 
    
#     lesson = ""
    
#     while (True) :
        
#         input_lesson = input (f"Enseignement à ajouter : ")
        
#         if (input_lesson == "stop") :
            
#             break
        
#         teacher.list_lessons.append (input_lesson)
        
#     teachers.append (teacher)

# with open ("./data/teachers.json", "w") as file_teacher :
    
#     json.dump ([{'Pseudo': teacher.user_name,
#                  'Mot_de_passe': teacher.password,
#                  'Prenom': teacher.first_name, 
#                  'Nom': teacher.last_name, 
#                  'Lecons': teacher.list_lessons}  
#                 for teacher in teachers], 
#                file_teacher, 
#                indent = 4)

# Exercice 3
# persons = []

# # Ajout des étudiants dans la liste "persons"
# with open ('./data/students.json', 'r') as file_student :
    
#     json_file = json.load (file_student)

# for json_data in json_file :
    
#     string_data_file = json.dumps (json_data, 
#                                    cls = Encoder)

#     # conversion en objet Python
#     dictionnary_object_student = json.loads (string_data_file)
    
#     # conversion en instance de classe
#     student = Student (
#         user_name = dictionnary_object_student ["Pseudo"],
#         password = dictionnary_object_student ["Mot_de_passe"],
#         first_name = dictionnary_object_student ["Prenom"], 
#         last_name = dictionnary_object_student ["Nom"],
#         notes = dictionnary_object_student ["Notes"],
#         average_student = dictionnary_object_student ["Moyenne_des_notes"]
#     )

#     persons.append (student)

# with open ('./data/teachers.json', 'r') as file_teacher :
    
#     json_file = json.load (file_teacher)

# for json_data in json_file :
    
#     string_data_file = json.dumps (json_data, 
#                                    cls = Encoder)

#     # conversion en objet Python
#     dictionnary_object_teacher = json.loads (string_data_file)
    
#     # conversion en instance de classe
#     teacher = Teacher (
#         user_name = dictionnary_object_teacher ["Pseudo"],
#         password = dictionnary_object_teacher ["Mot_de_passe"],
#         first_name = dictionnary_object_teacher ["Prenom"], 
#         last_name = dictionnary_object_teacher ["Nom"],
#         list_lessons = dictionnary_object_teacher ["Lecons"]
#     )

#     persons.append (teacher)

# for person in persons :
    
#     print (f"Bonjour, je m'appelle {person.first_name} {person.last_name} et {person.work()}")

# Exercice 4
persons = []

with open ("./data/students.json", "r") as file_student :
    
    data_student = json.load (file_student)
    
    for item_student in data_student :
        
        student = Student (item_student ["Prenom"], 
                           item_student ["Nom"], 
                           item_student ["Pseudo"], 
                           item_student ["Mot_de_passe"])
        
        student.user_name = item_student ["Pseudo"]
        student.password = item_student ["Mot_de_passe"]
        
        persons.append (student)

with open ("./data/teachers.json", "r") as file_teacher :
    
    data_teacher = json.load (file_teacher)
    
    for item_teacher in data_teacher :
        
        teacher = Teacher (item_teacher ["Prenom"], 
                           item_teacher ["Nom"], 
                           item_teacher ["Pseudo"], 
                           item_teacher ["Mot_de_passe"])
        
        teacher.user_name = item_teacher ["Pseudo"]
        teacher.password = item_teacher ["Mot_de_passe"]
    
        persons.append (teacher)

while (True) :
    
    first_name = input ("Prenom de l'utilisateur : ")
    last_name = input ("Nom de l'utilisateur : ")

    if (first_name == "stop" or last_name == "stop") :
        
        break

    user = next ((person for person in persons 
                  if (person.first_name == first_name and person.last_name == last_name)), 
                 None)

    if (not user) :
        
        print (f"Utilisateur {first_name} {last_name} introuvable \n")
        
        continue

    user_name = input ("Nouveau pseudo d'utilisateur : ")
    password = input ("Nouveau mot de passe : ")
    
    user = User (user_name, 
                 password)
    
    user.connect (user_name, 
                  password)

    if (isinstance (user, Student)) :
        
        student = Student (user_name, 
                           password)
        
        student.connect_student (user_name, 
                                 password)
        
        with open ("./data/students.json", "r") as file_student :
            
            data_student = json.load (file_student)
            
            for item_student in data_student :
                
                if (item_student ["Prenom"] == user.first_name and item_student ["Nom"] == user.last_name) :
                    
                    item_student ["Pseudo"] = user_name
                    item_student ["Mot_de_passe"] = password
                    
        with open ("./data/students.json", "w") as file_student :
            
            json.dump (data_student, 
                       file_student, 
                       indent = 4)
            
        student.disconnect_student ()
            
    elif (isinstance (user, Teacher)) :
        
        teacher = Teacher (user_name, 
                           password)
        
        teacher.connect_teacher (user_name, 
                                 password)
        
        with open ("./data/teachers.json", "r") as file_teacher :
            
            data_teacher = json.load (file_teacher)
            
            for item_teacher in data_teacher :
                
                if (item_teacher ["Prenom"] == user.first_name and item_teacher ["Nom"] == user.last_name) :
                    
                    item_teacher ["Pseudo"] = user_name
                    item_teacher ["Mot_de_passe"] = password
        
        with open ("./data/teachers.json", "w") as file_teacher :
            
            json.dump (data_teacher, 
                       file_teacher, 
                       indent = 4)
            
        teacher.disconnect_teacher () 

    print (f"informations mises à jour pour {first_name} {last_name}\n")