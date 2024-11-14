"""
Module pour vérifier si un nombre est premier et afficher les nombres premiers
jusqu'à 100.

Ce module contient deux fonctions :
1. `isprime(p)` : détermine si un nombre donné est premier.
2. `main()` : appelle `isprime` pour tester des nombres spécifiques et afficher
   tous les nombres premiers de 0 à 99.
"""

from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Vérifie si un nombre est un nombre premier.
    
    Args:
        p (int): Le nombre à vérifier.
        
    Returns:
        bool: Retourne True si le nombre est premier, sinon False.
        
    Description:
        Un nombre premier est un nombre qui est plus grand que 1 et qui ne peut 
        être divisé que par 1 et lui-même.
        
        La fonction commence par vérifier si le nombre est égal à 0 ou 1. Si c'est 
        le cas, elle retourne False, car ces nombres ne sont pas premiers.
        
        Ensuite, elle vérifie tous les nombres de 2 à la racine carrée du nombre 
        (ce qui permet de gagner du temps). Si un nombre trouve un diviseur (autre 
        que 1 et lui-même), le nombre n'est pas premier, donc la fonction retourne False.
        Si aucun diviseur n'est trouvé, cela veut dire que le nombre est premier et 
        la fonction retourne True.
    """
    if p in (1, 0):
        return False
    for i in range(2, int(sqrt(p)) + 1):  # On teste les diviseurs jusqu'à la racine carrée de p
        if p % i == 0:  # Si p est divisible par i, ce n'est pas un nombre premier
            return False
    return True  # Si aucun diviseur n'est trouvé, alors c'est un nombre premier

#### Fonction principale

def main():
    """
    Fonction principale qui teste si certains nombres sont premiers et affiche
    les nombres premiers de 0 à 99.
    
    Description:
        Cette fonction appelle plusieurs fois la fonction `isprime` pour tester 
        si certains nombres (comme 3, 53, et 14) sont premiers.
        
        Elle parcourt ensuite tous les nombres de 0 à 99, et pour chaque nombre, 
        elle vérifie s'il est premier avec `isprime`. Si c'est le cas, elle l'affiche.
    """
    isprime(3)
    isprime(53)
    isprime(14)

    # Affiche tous les nombres premiers entre 0 et 99
    for n in range(100):
        if isprime(n):
            print(n, end=", ")  # Affiche chaque nombre premier suivi d'une virgule

    print()  # Ajoute une nouvelle ligne à la fin

# Ce qui suit est exécuté si le fichier est lancé directement
if __name__ == "__main__":
    main()
