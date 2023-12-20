class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def get_total_part_one(input_data):
    instructions = input_data[0].strip()
    nodes = {}
    for line in input_data[1:]:
        parts = line.strip().split(' = ')
        if len(parts) != 2:
            continue
        value = parts[0]
        left, right = parts[1].strip('()').split(', ')
        nodes[value] = Node(value, left, right)

    cur_node = nodes["AAA"]
    cursor = 0
    count = 1
    while True:
        instruction = instructions[cursor]
        next_node = cur_node.right if instruction == 'R' else cur_node.left
        if next_node == "ZZZ":
            return count
        cur_node = nodes[next_node]
        count += 1
        cursor = (cursor + 1) % len(instructions)

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

def get_total_part_two(input_data):
    instructions = input_data[0].strip()
    nodes = {}
    for line in input_data[1:]:
        parts = line.strip().split(' = ')
        if len(parts) != 2:
            continue
        value = parts[0]
        left, right = parts[1].strip('()').split(', ')
        nodes[value] = Node(value, left, right)

    cursor = 0
    count = 0
    concurrent_paths = [nodes[key] for key in nodes if key.endswith('A')]
    loop_lengths = []

    while True:
        if len(loop_lengths) == len(concurrent_paths):
            result = lcm(loop_lengths[0], loop_lengths[1])
            for length in loop_lengths[2:]:
                result = lcm(result, length)
            return result

        instruction = instructions[cursor]
        for i, cur_node in enumerate(concurrent_paths):
            next_node = cur_node.right if instruction == 'R' else cur_node.left
            if next_node.endswith('Z'):
                loop_lengths.append(count + 1)
                concurrent_paths[i] = None
            else:
                concurrent_paths[i] = nodes[next_node]

        concurrent_paths = [node for node in concurrent_paths if node is not None]
        count += 1
        cursor = (cursor + 1) % len(instructions)


# Adapted usage
input_data = parse_input('input.txt')
print("Total Part One:", get_total_part_one(input_data))
print("Total Part Two:", get_total_part_two(input_data))
