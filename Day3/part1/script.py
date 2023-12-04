def read_diagram(file_path):
    """
    Lit les données d'entrée depuis un fichier et les stocke dans un tableau à deux dimensions.
    Chaque élément du tableau représente un caractère du schéma du moteur.
    """
    with open(file_path, 'r') as file:
        diagram = [list(line.strip()) for line in file.readlines()]
    return diagram
def find_special_symbols(diagram):
    """
    Trouve tous les symboles spéciaux (autre que '.' et chiffres) dans le diagramme.
    Retourne une liste de tuples contenant la position (ligne, colonne) de chaque symbole.
    """
    special_symbols = []
    for i in range(len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] not in "0123456789.":
                special_symbols.append((i, j))
    return special_symbols
def get_numbers_around_position(diagram, x, y):
    """
    Récupère tous les chiffres autour de la position spécifiée dans le diagramme.
    Retourne un ensemble de tous les chiffres trouvés.
    """
    numbers = set()

    # Check the surrounding positions
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i >= 0 and i < len(diagram) and j >= 0 and j < len(diagram[i]):
                if diagram[i][j].isdigit():
                    numbers.add(int(diagram[i][j]))

    return numbers

def get_all_numbers_around_symbols(diagram, symbols):
    """
    Récupère tous les chiffres autour de chaque symbole spécial dans le diagramme.
    Retourne un ensemble de tous les chiffres trouvés, sans se soucier du mapping.
    """
    all_numbers = set()

    for symbol_position in symbols:
        x, y = symbol_position
        numbers = get_numbers_around_position(diagram, x, y)
        all_numbers.update(numbers)

    return all_numbers
def get_all_numbers_around_symbols(diagram, symbols):
    """
    Récupère tous les chiffres autour de chaque symbole spécial dans le diagramme.
    Retourne une liste complète de tous les chiffres trouvés, sans se soucier du mapping ni des doublons.
    """
    all_numbers = []

    for symbol_position in symbols:
        x, y = symbol_position
        numbers = get_all_numbers_around_symbols(diagram, x, y)
        all_numbers.extend(numbers)

    return all_numbers
def sum_all_numbers(numbers_set):
    """
    Additionne tous les nombres dans l'ensemble.
    Retourne la somme totale.
    """
    return sum(numbers_set)

def main():
    # Chemin du fichier à lire
    file_path = 'input.txt'

    # Lire le schéma du moteur depuis le fichier
    motor_diagram = read_diagram(file_path)

    # Trouver tous les symboles spéciaux dans le diagramme
    special_symbols = find_special_symbols(motor_diagram)

    # Récupérer tous les chiffres autour de chaque symbole spécial
    all_numbers = get_all_numbers_around_symbols(motor_diagram, special_symbols)

    # Additionner tous les nombres
    total = sum_all_numbers(all_numbers)

    # Afficher la somme totale
    print(total)

if __name__ == "__main__":
    main()