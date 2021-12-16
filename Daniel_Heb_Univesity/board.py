from car import Car


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """
    SIZE = 7
    EMPTY_CALL = "-"

    def __init__(self):
        # implement your code and erase the "pass"
        # Note that this function is required in your Board implementation.
        # However, is not part of the API for general board types.
        self.cars = {}
        self.board = self.render_board()

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.

        res = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                res += self.board[i][j]
            res += "\n"

        return res

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        # In this board, returns a list containing the cells in the square
        # from (0,0) to (6,6) and the target cell (3,7)
        pass

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        # From the provided example car_config.json file, the return value could be
        # [('O','d',"some description"),('R','r',"some description"),('O','u',"some description")]
        pass

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        # In this board, returns (3,7)
        pass

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        # implement your code and erase the "pass"
        pass

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        # implement your code and erase the "pass"
        self.cars[car.name] = car
        self.board = self.render_board()


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        # implement your code and erase the "pass"
        pass

    def render_board(self):
        board = []

        for i in range(self.SIZE):
            row = []
            for j in range(self.SIZE):
                is_cell_fill = False

                for name, car in self.cars.items():
                    if (i, j) in car.car_coordinates():
                        row.append(name)
                        is_cell_fill = True
                        break

                if not is_cell_fill:
                    row.append(self.EMPTY_CALL)
            board.append(row)
        return board


if __name__ == '__main__':
    b = Board()
    c = Car("O", 2, (1,1), 1)

    print(b)
    b.add_car(c)

    print()
    print(b)