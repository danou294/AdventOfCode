def extract_game_data(line):
    line = line.split(':', 1)[1].strip() if ':' in line else line.strip()
    segments = line.split(';')
    color_counts = {}
    for segment in segments:
        color_number_pairs = segment.strip().split(',')
        for pair in color_number_pairs:
            parts = pair.strip().split()
            if len(parts) == 2:
                number, color = parts
                try:
                    number = int(number)
                except ValueError:
                    continue
                if color in color_counts:
                    color_counts[color] = max(color_counts[color], number)
                else:
                    color_counts[color] = number
    return color_counts

def compare_games(bag_contents, game_data):
    playable_games = []
    total_line_numbers = 0
    for game_number, color_counts in game_data.items():
        if all(bag_contents.get(color, 0) >= count for color, count in color_counts.items()):
            playable_games.append(game_number)
            total_line_numbers += game_number
    return playable_games, total_line_numbers

def main():
    bag_contents = {'red': 12, 'green': 13, 'blue': 14}
    game_data = {}
    with open('input.txt', 'r') as file:
        game_number = 1
        for line in file:
            color_counts = extract_game_data(line)
            game_data[game_number] = color_counts
            game_number += 1

    playable_games, total_line_numbers = compare_games(bag_contents, game_data)
    
    if playable_games:
        print("The following games are playable with the given bag contents: ", ", ".join(map(str, playable_games)))
        print("The total of the IDs of all playable games is: ", total_line_numbers)
    else:
        print("No games are playable with the given bag contents.")

if __name__ == "__main__":
    main()
