class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def remove_product(self, p_id, remove_count=1):
        for item, count in self.cart.items():
            if p_id == item:
                if count < remove_count:
                    raise ValueError()
                self.cart[p_id] -= remove_count

    def is_empty(self):
        s = 0

        for item, count in self.cart.items():
            s += count

        return s == 0

    def add_product(self, p_id, count=1):
        if not type(count) == int or count <= 0:
            raise ValueError()

        self.cart[p_id] = self.cart.get(p_id, 0) + count

    # def __repr__(self):
        return ",".join(f"{self.cart[p_id]}x{p_id}" for p_id in sorted(self.cart.keys()))


c = ShoppingCart()
print(c.is_empty())
c.add_product("12345")
c.add_product("66213", 3)
print(c)

c.remove_product("66213")
print(c)
print(c.is_empty())
c.remove_product("66213", 5)