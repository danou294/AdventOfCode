def compare_hands(hand1, hand2):
    """
    Compare two hands based on their type and individual card strengths.
    """
    card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    
    def get_hand_type(hand):
        """
        Determine the type of the hand.
        """
        counts = {label: hand.count(label) for label in set(hand)}
        count_values = sorted(counts.values(), reverse=True)

        if count_values == [5]:
            return "Cinq d'une sorte"
        elif count_values == [4, 1]:
            return "Carré"
        elif count_values == [3, 2]:
            return "Full house"
        elif count_values == [3, 1, 1]:
            return "Brelan"
        elif count_values == [2, 2, 1]:
            return "Deux paires"
        elif count_values == [2, 1, 1, 1]:
            return "Une paire"
        else:
            return "Carte haute"
    
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)
    types = ["Cinq d'une sorte", "Carré", "Full house", "Brelan", "Deux paires", "Une paire", "Carte haute"]

    # Compare types
    if types.index(hand1_type) < types.index(hand2_type):
        return -1  # hand1 est plus faible
    elif types.index(hand1_type) > types.index(hand2_type):
        return 1  # hand1 est plus fort
    else:
        # If types are the same, compare individual cards
        for card1, card2 in zip(hand1, hand2):
            if card_values[card1] > card_values[card2]:
                return 1  # hand1 est plus fort
            elif card_values[card1] < card_values[card2]:
                return -1  # hand1 est plus faible
        # Si toutes les cartes sont égales, c'est une égalité
        return 0

def rank_hands(entries):
    """
    Rank the hands based on their strength.
    """
    hands_and_bids = [(entry.split()[0], int(entry.split()[1])) for entry in entries]

    # Sort hands by their strength (first by type, then by individual card strength)
    sorted_hands = sorted(hands_and_bids, key=lambda hand_bid: (
        compare_hands(hand_bid[0], ""),
        compare_hands(hand_bid[0], hand_bid[0])
    ), reverse=True)

    # Assign ranks to the sorted hands
    ranked_hands = [(hand_bid[0], rank, hand_bid[1]) for rank, hand_bid in enumerate(sorted_hands, start=1)]
    return ranked_hands

# Exemple d'entrée
example_entries = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483"
]

# Obtenir la liste combinée
combined_list = rank_hands(example_entries)
print(combined_list)
