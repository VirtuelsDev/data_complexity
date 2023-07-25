def decrypter_code_secret(Xr, Xi, Br, Bi):
    #Convertir les réelles (Xr, Br) et imaginaires (Xi, Bi) en nombres complexes (X, B)
    X = complex(Xr, Xi)
    B = complex(Br, Bi)

    # Initialisation d'une liste vide pour stocker les chiffres du code
    digits = []

    #Déchiffrer le code en utilisant les chiffres du système avec la base B
    while abs(X) >= 1:
        
        digit = int(X.real % abs(B)) # Calcul du chiffre courant en prenant Xr/|B|
        digits.append(str(digit)) # Ajouter le chiffre courant à la liste 'digits'
        X = (X - digit) / B # Mettre à jour de X en soustrayant le chiffre courant / B

    #Vérifier si les contraintes st satisfaites (Si la valeur final de X est égale à 0)
    if X != 0:
        return "Le code ne peut pas être décrypté."
    
    #Formater la sortie en combinant les chiffres en une chaîne de caractères séparés
    return ",".join(reversed(digits))

#Précalculer les puissances de B jusqu'à n (nombre maximum d'entiers dans le code)
def precalculate_powers_of_B(B, n):
   
    powers = {0: complex(1, 0)}
    power = B
    for i in range(1, n + 1):
        powers[i] = power
        power *= B
    return powers


def main1():
    #Exécute le programme principal en lisant les données d'entrée 
    # et affichant les résultats du décryptage. 
    
    # Lecture du nombre total de cas de test T
    T = input("Entrez le nombre de cas de tests (T) : ")

    # Boucle pour chaque cas de test
    for k in range(T):
        print(f"\nCas de test {k + 1}:")
        # Lire les valeurs Xr, Xi, Br et Bi pour chaque cas de test
        Xr, Xi, Br, Bi = map(input("Entrez Xr, Xi, Br, Bi : ").split()) 

        # Appeler la fonction de décryptage 
        result = decrypter_code_secret(Xr, Xi, Br, Bi) 

        # Afficher le résultat du décryptage pour ce cas de test
        print(f"Résultat du décryptage : {result}") 

if __name__ == "__main__":
    main1()

