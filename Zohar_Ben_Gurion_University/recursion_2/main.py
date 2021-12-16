def dict_depth_helper(d, level):
    if not isinstance(d, dict) or not d:
        return level

    return max(dict_depth_helper(d[key], level + 1) for key in d)


def dict_depth(d):
    if not isinstance(d, dict):
        raise TypeError(f"{d} id not a dict!")

    if not d:
        return 0

    return dict_depth_helper(d, -1)


def nested_get(d, key):
    res = []

    if not isinstance(d, dict):
        return res

    for k in d:
        current_value = d[k]
        if key == k and not isinstance(current_value, dict):
            res.append(d[key])

        if isinstance(current_value, dict):
            res = res + nested_get(current_value, key)

    return res


def is_valid_integer_csv(file_name):
    line_len = None

    try:
        with open(file_name) as file:
            lines = file.readlines()

            for line in lines:
                vals = line.split(",")

                if line_len is None:
                    line_len = len(vals)
                elif line_len != len(vals):
                    return False

                try:
                    vals = [int(v) for v in vals]
                except ValueError:
                    return False
    except FileNotFoundError:
        return False

    return True


def connected_nodes_helper(graph, node, visited):
    visited.append(node)
    next_nodes = graph[node]

    for next_node in next_nodes:
        if next_node not in visited:
            visited = connected_nodes_helper(graph, next_node, visited)

    return visited


def connected_nodes(graph, node):
    return connected_nodes_helper(graph, node, [])
