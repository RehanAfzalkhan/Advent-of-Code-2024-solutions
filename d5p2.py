from collections import defaultdict, deque


def parse_input(file_path):
    with open(file_path, "r") as f:
        sections = f.read().strip().split("\n\n")
        rules = [line.strip() for line in sections[0].splitlines()]
        updates = [
            list(map(int, line.strip().split(","))) for line in sections[1].splitlines()
        ]
    return rules, updates


def build_graph(rules):
    graph = defaultdict(list)
    for rule in rules:
        x, y = map(int, rule.split("|"))
        graph[x].append(y)
    return graph


def is_valid_update(update, graph):
    subgraph = defaultdict(list)
    for x in update:
        subgraph[x] = [y for y in graph[x] if y in update]

    in_degree = {x: 0 for x in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order == update


def reorder_update(update, graph):
    subgraph = defaultdict(list)
    for x in update:
        subgraph[x] = [y for y in graph[x] if y in update]

    in_degree = {x: 0 for x in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


def find_middle_pages(updates, graph):
    middle_sum = 0
    for update in updates:
        reordered = reorder_update(update, graph)
        middle_page = reordered[len(reordered) // 2]
        middle_sum += middle_page
    return middle_sum


def main():
    file_path = "inputs/d5p2_input.txt"  # Replace with your actual file path
    rules, updates = parse_input(file_path)
    graph = build_graph(rules)

    # Separate valid and invalid updates
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if is_valid_update(update, graph):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    # Process invalid updates
    result = find_middle_pages(invalid_updates, graph)
    print(f"Sum of middle pages of corrected updates: {result}")


if __name__ == "__main__":
    main()
