def extract_minimum_cubes(line):
    line = line.split(':', 1)[1].strip() if ':' in line else line.strip()
    segments = line.split(';')
    min_cubes = {}
    for segment in segments:
        color_number_pairs = segment.strip().split(',')
        for pair in color_number_pairs:
            parts = pair.strip().split()
            if len(parts) == 2:
                number, color = parts
                number = int(number)
                if color in min_cubes:
                    min_cubes[color] = max(min_cubes[color], number)
                else:
                    min_cubes[color] = number
    return min_cubes

def calculate_power(cubes):
    return cubes.get('red', 0) * cubes.get('green', 0) * cubes.get('blue', 0)

def main():
    total_power = 0
    with open('input.txt', 'r') as file:
        for line in file:
            min_cubes = extract_minimum_cubes(line)
            power = calculate_power(min_cubes)
            total_power += power
            print(f"Game: {line.split(':')[0]}, Minimum Cubes: {min_cubes}, Power: {power}")

    print(f"The total power of all games is: {total_power}")

if __name__ == "__main__":
    main()
