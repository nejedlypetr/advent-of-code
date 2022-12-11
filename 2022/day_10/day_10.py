import copy
DATA = 'puzzle_input.txt'

class CRT():
    def __init__(self, file):
        self.data = self.get_data(file)
        self.screen = ""
        self.cycle = 0
        self.register = 1
        self.saved_signal_strengths = []

    def get_data(self, file):
        with open(file, "r") as data: return data.read().splitlines()

    def save_signal_strength(self):
        if self.cycle in [20, 60, 100, 140, 180, 220]:
            self.saved_signal_strengths.append(self.cycle * self.register)

    def get_sum_of_saved_register_values(self):
        return sum(self.saved_signal_strengths)

    def run(self):
        for line in self.data:
            if line == "noop": 
                self.new_cycle()
            else:
                self.new_cycle()
                self.new_cycle()
                self.register += int(line.split()[1])
        self.format_screen()
        
    def new_cycle(self):
        self.draw()
        self.cycle += 1
        self.save_signal_strength()
    
    def draw(self):
        if abs(self.register - (self.cycle % 40)) <= 1: self.screen += "#"
        else: self.screen += "."
        
    def split_str_by_fixed_lenght(self, str, n):
        return [str[i:i+n] for i in range(0, len(str), n)]

    def format_screen(self):
        chunks = self.split_str_by_fixed_lenght(self.screen, 40)
        self.screen = "\n".join(chunks)


crt = CRT(DATA)
crt.run()
print(f"Task #1: {crt.get_sum_of_saved_register_values()}")
print(f"Task #2:\n{crt.screen}")