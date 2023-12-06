def read_and_process_input(file_path):
    with open(file_path, 'r') as file:
        sections = file.read().split("\n\n")

    seeds = list(map(int, sections[0].split(":")[1].split()))

    # Préparation des plages de mappage pour chaque catégorie
    maps_ranges = [list() for _ in sections[1:]]
    for index, section in enumerate(sections[1:], start=1):
        for line in section.strip().split('\n')[1:]:
            dest_start, src_start, length = map(int, line.split())
            maps_ranges[index - 1].append((src_start, dest_start, length))

    # Processus de transformation
    min_location = float('inf')
    for seed in seeds:
        num = seed
        for ranges in maps_ranges:
            for src_start, dest_start, length in ranges:
                if src_start <= num < src_start + length:
                    num = dest_start + (num - src_start)
                    break
        min_location = min(min_location, num)

    return min_location

def main():
    path = 'input.txt'
    lowest_location = read_and_process_input(path)
    return lowest_location

print(main())
