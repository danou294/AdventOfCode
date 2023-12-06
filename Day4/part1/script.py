def read_scratchcards(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    cards = []
    for line in lines:
        # Retirer le préfixe "Card X:" et séparer les parties de la ligne
        parts = line.strip().split(': ')[1].split(' | ')
        if len(parts) < 2:
            continue  # Ignorer les lignes mal formatées
        winning_numbers, your_numbers = parts
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = list(map(int, your_numbers.split()))
        cards.append((winning_numbers, your_numbers))

    return cards

def calculate_points(cards):
    total_points = 0

    for winning_numbers, your_numbers in cards:
        matches = winning_numbers.intersection(your_numbers)
        if matches:
            points = 1
            for _ in range(1, len(matches)):
                points *= 2
            total_points += points

    return total_points

def main():
    path = 'input.txt'
    cards = read_scratchcards(path)
    total_points = calculate_points(cards)
    print(f"The total points of the scratchcards are: {total_points}")

if __name__ == "__main__":
    main()
