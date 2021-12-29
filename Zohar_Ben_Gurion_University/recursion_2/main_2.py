# {} 0
# {1: "a", 2: "b"} 0
# {1: {1: "a", 2: "b"}, 2: "b"} 1
# {1: {1: "a", 2: "b"}, 2: {"b": 3}} 1
# {1: {1: "a", 2: "b"}, 2: {"b": {"3": 4}}} 2


def depth_d_helper(d, count):
    if not isinstance(d, dict):
        return count

    res_list = []
    for k, v in d.items():

        res = depth_d_helper(v, count + 1)
        res_list.append(res)

    return max(res_list)


def depth_d(d):
    if not isinstance(d, dict):
        raise TypeError("d is not dict")

    if not d:
        return 0

    return depth_d_helper(d, -1)


print(depth_d({}))