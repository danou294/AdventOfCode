# Créez un dictionnaire qui associe les noms en anglais aux chiffres
name_to_digit = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_first_number(line):
    number = ""
    position = -1
    
    for i, char in enumerate(line):
        if char.isdigit():
            number = char
            position = i
            break
    
    return number, position
def find_last_number(line):
    number = ""
    position = -1
    
    for i, char in enumerate(reversed(line)):
        if char.isdigit():
            number = char
            position = len(line) - 1 - i
            break
    
    return number, position
def find_name_positions(line):
    name_positions = {}
    
    for name in name_to_digit.keys():
        position = line.find(name)
        if position != -1:
            name_positions[name] = position
    
    return name_positions

    smallest_position = len(line)

    # Recherche le chiffre numérique ayant la plus petite position
    first_number, first_position = find_first_number(line)
    if first_number is not None and first_position < smallest_position:
        smallest_digit = first_number
        smallest_position = first_position

    # Recherche le chiffre littéral ayant la plus petite position
    for name, position in find_name_positions(line).items():
        if position < smallest_position:
            if smallest_digit is None or isinstance(smallest_digit, str):
                # Si smallest_digit est une chaîne de caractères, faites la correspondance avec name_to_digit
                if name in name_to_digit:
                    smallest_digit = name_to_digit[name]
                else:
                    smallest_digit = name
            else:
                smallest_digit = name
            smallest_position = position

    return smallest_digit
def find_and_map_smallest_number(line, mapping_dict):
    smallest_position = len(line)
    smallest_number = None

    for name, position in mapping_dict.items():
        if name in line and position < smallest_position:
            smallest_position = position
            smallest_number = name
        elif str(position) in line and position < smallest_position:
            smallest_position = position
            smallest_number = str(position)

    if smallest_number is not None:
        return smallest_number
    else:
        return None





def main():
    # Ouvre le fichier d'entrée en mode lecture
    with open('input.txt', 'r') as file:
        for line in file:
            print(find_name_positions(line))
            print(find_and_map_smallest_number(find_name_positions(line),name_to_digit))

if __name__ == "__main__":
    main()
