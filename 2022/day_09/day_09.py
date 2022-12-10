import copy
DATA = 'puzzle_input.txt'


class Cords():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rope():
    def __init__(self, number_of_nodes):
        self.visited = [Cords(0, 0)]
        self.nodes = []
        for _ in range(number_of_nodes):
            self.nodes.append(Cords(0, 0))

    def save_tail_cords(self):
        for cord in self.visited:
            if cord.x == self.nodes[-1].x and cord.y == self.nodes[-1].y: return
        self.visited.append(copy.copy(self.nodes[-1]))


class Board():
    def __init__(self, file, number_of_nodes):
        self.rope = Rope(number_of_nodes)
        self.moves = self.get_data(file)

    def get_data(self, file):
        with open(file, "r") as data: return data.read().splitlines()  

    def get_cords_of_direction(self, direction):
        if direction == "U": return Cords(0, 1)
        elif direction == "D": return Cords(0, -1)
        elif direction == "R": return Cords(1, 0)
        elif direction == "L": return Cords(-1, 0)

    def move_head(self, direction, steps):
        cords = self.get_cords_of_direction(direction)
        for _ in range(steps):
            self.rope.nodes[0].x += cords.x
            self.rope.nodes[0].y += cords.y
            self.move_body()

    def move_body(self):
        for i in range(0, len(self.rope.nodes)-1):
            if not self.is_touching(self.rope.nodes[i], self.rope.nodes[i+1]):
                self.move(self.rope.nodes[i], self.rope.nodes[i+1])
        self.rope.save_tail_cords()

    def move(self, first, second):
        if first.x > second.x: second.x += 1
        if first.x < second.x: second.x -= 1
        if first.y > second.y: second.y += 1
        if first.y < second.y: second.y -= 1
        
    def is_touching(self, first, second):
        return abs(first.x - second.x) <= 1 and abs(first.y - second.y) <= 1

    def run_moves(self):
        for move in self.moves:
            direction = move.split()[0]
            steps = int(move.split()[1])
            self.move_head(direction, steps)

    def count_visited(self):
        return len(self.rope.visited)


board_1, board_2 = Board(DATA, 2), Board(DATA, 10)
board_1.run_moves(), board_2.run_moves()
print(f"Part #1: {board_1.count_visited()}")
print(f"Part #2: {board_2.count_visited()}")