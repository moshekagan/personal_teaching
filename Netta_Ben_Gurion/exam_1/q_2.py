class Football_Player:
    def __init__(self, name, salary, performance_func=None):
        self.name = name
        self.salary = salary
        self.performance_func = performance_func

    def set_new_performance_func(self, a, b, c):
        self.performance_func = lambda x: a*(x**2) + b*x + c

    def get_performance(self, x):
        return self.performance_func(x)

    def __repr__(self):
        return f"({self.name}, {self.salary}, {self.performance_func(2)})"


class Defense_Player(Football_Player):
    def __init__(self, name, salary, performance_func=None):
        super().__init__(name, salary, performance_func)
        self.total_tackles = 0

    def tackle(self):
        self.total_tackles += 1


class Offense_Player(Football_Player):
    def __init__(self, name, salary, performance_func=None):
        super().__init__(name, salary, performance_func)
        self.total_yards_gained = 0

    def run_yards(self, yards):
        self.total_yards_gained += yards


def choose_players(players, team_motivation, num_def, num_off, max_salary):
    return choose_players_helper(players, team_motivation, num_def, num_off, max_salary, 0)


def choose_players_helper(players, team_motivation, num_def, num_off, max_salary, sum_performance):
    if len(players) == 0:
        # We found a good solution
        if num_def == 0 and num_off == 0 and max_salary >=0:
            return sum_performance
        else:
            return 0

    sum_without_current = choose_players_helper(players[1:], team_motivation, num_def, num_off, max_salary, sum_performance)

    current_player = players[0]
    new_max_salary = max_salary - current_player.salary
    new_sum_performance = sum_performance + current_player.performance_func(team_motivation)

    if isinstance(current_player, Offense_Player):
        sum_with_current = choose_players_helper(players[1:], team_motivation, num_def, num_off-1, new_max_salary, new_sum_performance)
    else:  # is Defense_Player
        sum_with_current = choose_players_helper(players[1:], team_motivation, num_def-1, num_off, new_max_salary, new_sum_performance)

    return max(sum_with_current, sum_without_current)


if __name__ == '__main__':
    p1 = Defense_Player("P1", 10, lambda x: 5)
    p2 = Defense_Player("P2", 20, lambda x: 6)
    p3 = Offense_Player("P3", 10, lambda x: 4)
    p4 = Offense_Player("P4", 20, lambda x: 9)

    print(choose_players(players=[], team_motivation=2, num_def=1, num_off=0, max_salary=10))  # 0

    print(choose_players(players=[p1], team_motivation=2, num_def=1, num_off=0, max_salary=10))  # 5
    print(choose_players(players=[p1, p2], team_motivation=2, num_def=1, num_off=0, max_salary=10))  # 5
    print(choose_players(players=[p1, p2], team_motivation=2, num_def=1, num_off=0, max_salary=20))  # 6

    print(choose_players([p1, p2, p3, p4], 2, 1, 1, 20))  # 9
    print(choose_players([p1, p2, p3, p4], 2, 1, 1, 40))  # 15

    d1 = Defense_Player("D1", 10, lambda x: -1)
    o1 = Offense_Player("O1", 9, lambda x: 4)
    d2 = Defense_Player("D1", 12, lambda x: 13)
    o2 = Offense_Player("O1", 7, lambda x: 18)
    d3 = Defense_Player("D1", 14, lambda x: 27)
    o3 = Offense_Player("O1", 5, lambda x: 32)
    d4 = Defense_Player("D1", 16, lambda x: 41)
    o4 = Offense_Player("O1", 3, lambda x: 46)
    d5 = Defense_Player("D1", 18, lambda x: 55)
    o5 = Offense_Player("O1", 80, lambda x: 60)

    players_list = [d1, o1, d2, o2, d3, o3, d4, o4, d5, o5]
    print(choose_players(players=players_list, team_motivation=2, num_def=4, num_off=4, max_salary=100))  # 236


# def choose_players(players, team_motivation, num_def, num_off, max_salary):
#     mot_level = 2
#     return choose_players_helper(players, num_def, num_off, max_salary, 0, mot_level)
#
# def choose_players_helper(players, num_def, num_off, max_salary, sum_qual, mot_level):
#     if len(players) == 0:
#         if num_def == 0 and num_off == 0 and max_salary >= 0:
#             return sum_qual
#         else:
#             return 0
#     if num_def < 0 or num_off < 0 or max_salary < 0:
#         return 0
#
#     dont_choose_curr = choose_players_helper(players[1:], num_def, num_off, max_salary, sum_qual, mot_level)
#
#     new_sum_qual = sum_qual + players[0].get_performance(mot_level)
#     new_max_sal = max_salary - players[0].salary
#     if isinstance(players[0], Offense_Player):
#         choose_curr = choose_players_helper(players[1:], num_def, num_off - 1, new_max_sal, new_sum_qual, mot_level)
#     else:
#         choose_curr = choose_players_helper(players[1:], num_def - 1, num_off, new_max_sal, new_sum_qual, mot_level)
#
#     return max(choose_curr, dont_choose_curr)