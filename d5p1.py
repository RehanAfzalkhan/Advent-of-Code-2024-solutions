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
    # Extract subgraph for the pages in this update
    subgraph = defaultdict(list)
    for x in update:
        subgraph[x] = [y for y in graph[x] if y in update]

    # Calculate in-degrees for topological sort
    in_degree = {x: 0 for x in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    # Perform topological sort
    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if sorted_order matches the update
    return sorted_order == update


def find_middle_pages(updates, graph):
    valid_updates = []
    for update in updates:
        if is_valid_update(update, graph):
            valid_updates.append(update)

    # Find and sum the middle pages of valid updates
    middle_sum = 0
    for update in valid_updates:
        middle_page = update[len(update) // 2]
        middle_sum += middle_page

    return middle_sum


def main():
    file_path = "inputs/d5p1_input.txt"  # Replace with the actual path
    rules, updates = parse_input(file_path)
    graph = build_graph(rules)
    result = find_middle_pages(updates, graph)
    print(f"Sum of middle pages of valid updates: {result}")


if __name__ == "__main__":
    main()
