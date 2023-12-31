import itertools

# Définition d'une structure Point sous forme de tuple
def Point(y, x):
    return (y, x)

# Définition d'une structure PointSpan pour représenter un nombre dans le diagramme
def PointSpan(y, x_start, x_end):
    return {"y": y, "x": {"start": x_start, "end": x_end}}

# Définition d'une structure Number pour stocker un nombre et son emplacement
def Number(index, value):
    return {"index": index, "value": value}

# Fonction pour analyser le fichier et extraire les nombres et symboles
def parse(path):
    numbers = []
    symbols = set()

    with open(path, 'r') as file:
        input_data = file.readlines()

    # Parcourir chaque ligne et caractère pour identifier les nombres et symboles
    for y, line in enumerate(input_data):
        row = list(line.strip())
        is_parsing_number = False
        digits, start = None, None

        for x, char in enumerate(row):
            if char.isdigit():
                digit = int(char)
                if is_parsing_number:
                    # Si on est en train de lire un nombre, continuer à le construire
                    digits = digits * 10 + digit
                else:
                    # Sinon, commencer un nouveau nombre
                    is_parsing_number = True
                    digits, start = digit, x
            else:
                if is_parsing_number:
                    # Si on termine de lire un nombre, l'ajouter à la liste
                    numbers.append(Number(PointSpan(y, start, x), digits))
                is_parsing_number = False
                if char != '.':
                    # Si le caractère n'est pas un point, c'est un symbole
                    symbols.add(Point(y, x))

        if is_parsing_number:
            # Ajouter le dernier nombre de la ligne s'il y en a un
            numbers.append(Number(PointSpan(y, start, len(row)), digits))

    return numbers, symbols

# Fonction pour trouver les voisins d'un point donné
def neighbors(point_span):
    y, span = point_span["y"], point_span["x"]
    return [
        Point(y, x) for x in itertools.chain(range(span["start"] - 1, span["start"]),
                                             range(span["end"], span["end"] + 1))
    ] + [
        Point(yn, x) for yn in [y - 1, y + 1]
        for x in range(span["start"] - 1, span["end"] + 1)
    ]

# Partie 1 : Calcul de la somme des valeurs des nombres voisins des symboles
def part1(path):
    numbers, symbols = parse(path)
    sum = 0
    for number in numbers:
        if set(neighbors(number["index"])).intersection(symbols):
            sum += number["value"]
    print(sum)

# Partie 2 : Calcul basé sur une relation spécifique entre les nombres et les symboles
def part2(path):
    numbers, symbols = parse(path)
    adjacency = {symbol: [] for symbol in symbols}
    for number in numbers:
        for symbol in set(neighbors(number["index"])).intersection(symbols):
            adjacency[symbol].append(number["value"])
    
    sum = 0
    for adjacent_numbers in adjacency.values():
        if len(adjacent_numbers) == 2:
            sum += adjacent_numbers[0] * adjacent_numbers[1]
    
    print(sum)

def main():
    path = 'input.txt'
    part1(path)
    part2(path)

if __name__ == "__main__":
    main()
