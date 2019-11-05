
def earliest_ancestor(ancestors, starting_node):
    graph = {}

    for pair in ancestors:
        if f"{pair[1]}" in graph:
            graph[f"{pair[1]}"].add(f"{pair[0]}")
        else:
            graph[f"{pair[1]}"] = set()
            graph[f"{pair[1]}"].add(f"{pair[0]}")

    stack = []
    path = []
    level = 1
    stack.append({"number": f"{starting_node}", "length": level})
    while len(stack) > 0:
        v = stack.pop()
        path.append(v)
        if v["number"] in graph:
            level += 1
            for neighbor in graph[v["number"]]:
                stack.insert(0, {"number": neighbor, "length": level})


    if len(path) == 1:
        return -1
    else:
        lowest = 1
        lowest_numbers = []
        for i in range(len(path)):
            if path[i]["length"] > lowest:
                lowest = path[i]["length"]
                lowest_numbers = [int(path[i]["number"])]
            else:
                lowest_numbers.append(int(path[i]["number"]))
        return min(lowest_numbers)