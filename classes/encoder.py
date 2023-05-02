# importe le JSONEncoder depuis le module json
from json import JSONEncoder

# Création de la class Encoder, qui est étendu à la class JSONEncoder
class Encoder (JSONEncoder) :
    
    # Création d'une méthode default avec 1 paramètre, qui crée un dictionnaire avec l'object
    @classmethod
    def default (self, 
                 object : object) -> dict :
        
        # Retourne un dictionnaire
        return {
        
            # Kwargs.lstrip ('_'), enlève le tiret du bas de chaque clé (attribut)
            # var for kwargs, pour chaque clé et valeur 
            # Var in vars (object).items (), pairs de clé et valeur 
            kwargs.lstrip ('_') : var for kwargs, 
            var in vars (object).items ()
        }