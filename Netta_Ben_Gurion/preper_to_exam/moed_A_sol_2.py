class Pokemon:
    def __init__(self, name, a, d):
        self.name = name
        self.a = a
        self.d = d

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name

    def cross_breeding(self, other, name):
        return Pokemon(name, (self.a + other.a)/2, (self.d + self.d)/2)


class PokemonLineageGraph:
    def __init__(self):
        self.pokemon_nodes = [Pokemon('Pikachu', 5, 5),
                              Pokemon('Charmander', 5, 5),
                              Pokemon('Squirtle', 5, 5),
                              Pokemon('Bulbasaur', 5, 5),
                              Pokemon('Mew', 5, 5)]
        self.pedigree = []

    def __repr__(self):
        return f"nodes={self.pokemon_nodes}\nedges={self.pedigree}"

    def add_pokemon(self, poke_name, ancestors):
        p = ancestors[0].cross_breeding(ancestors[1], poke_name)
        self.pokemon_nodes.append(p)
        self.pedigree.append((p, ancestors[0]))
        self.pedigree.append((p, ancestors[1]))
        self.pedigree.append((ancestors[0], p))
        self.pedigree.append((ancestors[1], p))

    def get_pokemon_families(self):
        visited = {i: False for i in self.pokemon_nodes}

        families = []
        for poke in self.pokemon_nodes:
            if not visited[poke]:
                visited[poke] = True
                family = self.get_all_family_members(poke, visited)
                families.append(family)

        return families

    def get_all_family_members(self, poke, visited):
        family = []
        family.append(poke)

        for edge in self.pedigree:
            new_member = edge[1]

            if edge[0] == poke and new_member not in visited.values():
                visited[new_member] = True
                family.append(new_member)

                new_family = self.get_all_family_members(new_member, visited)

                family += new_family

        return set(family)

    def sort_families_by_max_kinship(self):
        families = self.get_pokemon_families()

        families_strength = []

        for family in families:
            family_strength = self.get_family_strength(family)
            families_strength.append((family_strength, family))

        sorted_families_strength = sorted(families_strength, key=lambda x: x[0])
        new_families = []
        for f in sorted_families_strength:
            new_families.append(f[1])

        return new_families

    # def get_family_strength(self, family):
    #     max = 0
    #     for member in family:
    #         ms = self.get_relative...()
    #         if ms > max:
    #             max = ms
    #     return max


if __name__ == '__main__':
    poke_lineage = PokemonLineageGraph()
    poke_lineage.add_pokemon('Zubat', (poke_lineage.pokemon_nodes[1], poke_lineage.pokemon_nodes[2]))
    print(poke_lineage)
