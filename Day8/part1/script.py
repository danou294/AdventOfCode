def parse_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    instructions = lines[0].strip()
    graph = {}

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        node_name, neighbors = line.split(' = ')
        graph[node_name] = tuple(neighbors[1:-1].split(', '))

    return instructions, graph

def find_steps_to_ZZZ(graph, start_node, instructions):
    current_node = start_node
    step_count = 0

    while current_node != 'ZZZ':
        instruction = instructions[step_count % len(instructions)]
        if instruction == 'L':
            current_node = graph[current_node][0]
        else:  # 'R'
            current_node = graph[current_node][1]
        step_count += 1

    return step_count

try:
    instructions, graph = parse_input('input.txt')
    start_node = 'AAA'
    steps = find_steps_to_ZZZ(graph, start_node, instructions)
    print(f"Nombre d'étapes pour atteindre ZZZ à partir de {start_node} : {steps}")
except Exception as e:
    print(f"Erreur : {e}")
