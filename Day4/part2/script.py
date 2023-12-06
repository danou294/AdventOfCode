def read_scratchcards(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    cards = []
    for line in lines:
        parts = line.strip().split(': ')[1].split(' | ')
        if len(parts) < 2:
            continue
        winning_numbers, your_numbers = parts
        winning_numbers = set(map(int, winning_numbers.split()))
        your_numbers = set(map(int, your_numbers.split()))
        cards.append((winning_numbers, your_numbers))

    return cards

def calculate_total_cards(cards):
    total_cards = 0
    num_cards = len(cards)
    copies = [0] * num_cards  # Initialiser un compteur pour les copies de chaque carte

    for index in range(num_cards):
        winning_numbers, your_numbers = cards[index]
        matches = winning_numbers.intersection(your_numbers)
        num_matches = len(matches)

        # Ajouter la carte originale et ses copies
        total_cards += 1 + copies[index]

        # Calculer les copies supplémentaires gagnées
        for i in range(1, num_matches + 1):
            next_card_index = index + i
            if next_card_index < num_cards:
                copies[next_card_index] += 1 + copies[index]  # Ajouter les copies gagnées

    return total_cards

def main():
    path = 'input.txt'
    cards = read_scratchcards(path)
    total_cards = calculate_total_cards(cards)
    print(f"Total scratchcards including copies: {total_cards}")

if __name__ == "__main__":
    main()
