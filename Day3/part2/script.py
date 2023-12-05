import itertools

def Point(y, x):
    return (y, x)

def PointSpan(y, x_start, x_end):
    return {"y": y, "x": {"start": x_start, "end": x_end}}

def Number(index, value):
    return {"index": index, "value": value}

def parse(path):
    numbers = []
    symbols = set()

    with open(path, 'r') as file:
        input_data = file.readlines()

    for y, line in enumerate(input_data):
        row = list(line.strip())
        is_parsing_number = False
        digits, start = None, None

        for x, char in enumerate(row):
            if char.isdigit():
                digit = int(char)
                if is_parsing_number:
                    digits = digits * 10 + digit
                else:
                    is_parsing_number = True
                    digits, start = digit, x
            else:
                if is_parsing_number:
                    numbers.append(Number(PointSpan(y, start, x), digits))
                is_parsing_number = False
                if char != '.':
                    symbols.add(Point(y, x))

        if is_parsing_number:
            numbers.append(Number(PointSpan(y, start, len(row)), digits))

    return numbers, symbols

def neighbors(point_span):
    y, span = point_span["y"], point_span["x"]
    return [
        Point(y, x) for x in itertools.chain(range(span["start"] - 1, span["start"]),
                                             range(span["end"], span["end"] + 1))
    ] + [
        Point(yn, x) for yn in [y - 1, y + 1]
        for x in range(span["start"] - 1, span["end"] + 1)
    ]

def part2(path):
    numbers, symbols = parse(path)
    adjacency = {symbol: [] for symbol in symbols}

    for number in numbers:
        for symbol in set(neighbors(number["index"])).intersection(symbols):
            adjacency[symbol].append(number["value"])
    
    sum_gear_ratios = 0
    for adjacent_numbers in adjacency.values():
        if len(adjacent_numbers) == 2:
            gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
            sum_gear_ratios += gear_ratio
    
    print(sum_gear_ratios)

def main():
    path = 'input.txt'
    part2(path)

if __name__ == "__main__":
    main()
