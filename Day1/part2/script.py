# Dictionnaire pour convertir les noms en chiffres
name_to_digit = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

def convert_name_to_digit(name):
    return name_to_digit.get(name, None)

def find_first_number_or_name(line):
    smallest_position = len(line)
    result = None, -1

    # Recherche de chiffres numériques
    for i, char in enumerate(line):
        if char.isdigit() and i < smallest_position:
            smallest_position = i
            result = int(char), i

    # Recherche de noms de chiffres
    for name, digit in name_to_digit.items():
        position = line.find(name)
        if 0 <= position < smallest_position:
            smallest_position = position
            result = digit, position

    return result

def find_last_number_or_name(line):
    highest_position = -1
    result = None, -1

    # Recherche de chiffres numériques
    for i, char in enumerate(reversed(line)):
        pos = len(line) - 1 - i
        if char.isdigit() and pos > highest_position:
            highest_position = pos
            result = int(char), pos

    # Recherche de noms de chiffres
    for name, digit in name_to_digit.items():
        position = line.rfind(name)
        if position > highest_position:
            highest_position = position
            result = digit, position

    return result

def main():
    cumul = 0

    with open('input.txt', 'r') as file:
        for line in file:
            first_digit, _ = find_first_number_or_name(line)
            last_digit, _ = find_last_number_or_name(line)

            if first_digit is not None and last_digit is not None:
                nombre = int(f"{first_digit}{last_digit}")
                cumul += nombre

    print('Cumul total :', cumul)

if __name__ == "__main__":
    main()
