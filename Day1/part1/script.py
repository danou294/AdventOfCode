def extract_calibration_value(line):
    # Utilise strip() pour supprimer les espaces et les caractères de fin de ligne
    line = line.strip()
    
    # Vérifie que la ligne a au moins deux caractères
    if len(line) >= 2:
        # Extrait le premier chiffre en partant du début de la ligne
        first_digit = None
        for char in line:
            if char.isdigit():
                first_digit = int(char)
                break
        
        # Extrait le dernier chiffre en partant de la fin de la ligne
        last_digit = None
        for char in reversed(line):
            if char.isdigit():
                last_digit = int(char)
                break
        
        # Si les deux chiffres ont été trouvés, combine-les pour former la valeur de calibration
        if first_digit is not None and last_digit is not None:
            calibration_value = first_digit * 10 + last_digit
            return calibration_value
    
    # Si la ligne ne correspond pas au format attendu, retourne 0
    return 0

def main():
    total_calibration = 0

    # Ouvre le fichier d'entrée en mode lecture
    with open('input.txt', 'r') as file:
        for line in file:
            # Appelle la fonction pour extraire la valeur de calibration de chaque ligne
            calibration = extract_calibration_value(line)
            # Ajoute la valeur de calibration à la somme totale
            total_calibration += calibration

    # Affiche la somme totale des valeurs de calibration
    print("La somme totale des valeurs de calibration est :", total_calibration)

if __name__ == "__main__":
    main()
