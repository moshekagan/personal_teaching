class IsraeliQueueItem:
    def __init__(self, value, priority, group_id):
        if not isinstance(priority, int) or not isinstance(group_id, int):
            raise TypeError("Invalid arguments types")

        if priority <= 0 or group_id <= 0:
            raise ValueError("Invalid arguments values")

        self.value = value
        self.priority = priority
        self.group_id = group_id

    def __repr__(self):
        return f"Value: {self.value}, Priority: {self.priority}, GroupID: {self.group_id}"


class IsraeliQueue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, val, priority, group_id):
        item = IsraeliQueueItem(val, priority, group_id)

        is_new = True
        for i in range(len(self)):
            group = self.queue[i]
            if group["group_id"] == item.group_id:
                is_new = False
                group["sum"] += item.priority
                group["items"].append(item)
                group["items"] = list(sorted(group["items"], key=lambda current_item: current_item.priority, reverse=True))

        if is_new:
            new_group = {
                "group_id": group_id,
                "items": [item],
                "sum": item.priority
            }
            self.queue.append(new_group)

        self.order_queue()

    def order_queue(self):
        self.queue = list(sorted(self.queue, key=lambda g: g["sum"], reverse=True))

    def dequeue_item(self):
        group = self.queue[0]

        item = group["items"][0]
        group["items"] = self.queue[0]["items"][1:]
        group["sum"] -= item.priority

        self.order_queue()

        return item

    def dequeue_group(self):
        group = self.queue[0]
        self.queue = self.queue[1:]

        return group["items"]

    def dequeue_item_2(self):
        max_sum = self.queue[0]["sum"]
        max_g = self.queue[0]

        for i in range(len(self)):
            if self.queue[i]["sum"] > max_sum:
                max_sum = self.queue[i]["sum"]
                max_g = self.queue[i]

        max_i = 0
        max_item = max_g["items"][0]

        for i in range(len(max_g["items"])):
            if max_g["items"][i].priority > max_item.priority:
                max_item = max_g["items"][i]
                max_i = i

        del max_g["items"][max_i]
        return max_item

    def dequeue_group_2(self):
        max_sum = self.queue[0]["sum"]
        max_g = self.queue[0]
        max_i = 0

        for i in range(len(self)):
            if self.queue[i]["sum"] > max_sum:
                max_sum = self.queue[i]["sum"]
                max_g = self.queue[i]

        del self.queue[max_i]
        return max_g["items"]


def sort_queue_by_priorities(queue):
    res = []
    for g in queue.queue:
        res += g["items"]
    return res


if __name__ == '__main__':
    q = IsraeliQueue()
    q.enqueue("F", 1, 1)
    q.enqueue("S", 2, 2)
    q.enqueue("F", 3, 3)
    q.enqueue("F", 4, 1)
    q.enqueue("F", 5, 1)
    q.enqueue("F", 6, 1)
    q.enqueue("F", 7, 1)

    i = q.dequeue_item()
    g = q.dequeue_group()

    q2 = IsraeliQueue()
    q2.enqueue("F", 1, 1)
    q2.enqueue("S", 2, 2)
    q2.enqueue("F", 3, 3)
    q2.enqueue("F", 4, 1)
    q2.enqueue("F", 5, 1)
    q2.enqueue("F", 6, 1)
    q2.enqueue("F", 7, 1)

    i2 = q2.dequeue_item_2()
    g2 = q2.dequeue_group_2()


    print(sort_queue_by_priorities(q2))

