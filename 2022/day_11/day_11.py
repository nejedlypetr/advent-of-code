import copy
DATA = 'puzzle_input.txt'

class Monkey():
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation # data format -> [sign, value]
        self.test = test # data format -> [divisible_by, if_true, if_false]
        self.counter = 0

class MonkeyBusiness():
    def __init__(self):
        self.monkeys = []

    def calculate_modulo(self):
        modulo = 1
        for monkey in self.monkeys: modulo *= monkey.test[0]
        return modulo

    def get_monkey_blocks(self, file):
        with open(file, "r") as data: return data.read().split("\n\n")
    
    def map_data(self, file):
        for m in self.get_monkey_blocks(file):
            monkey_data = m.replace('  ', '').splitlines()

            items = monkey_data[1].replace("Starting items: ", '').split(", ")
            operation = monkey_data[2].replace("Operation: new = old ", '').split()
            divisible_by = int(monkey_data[3].replace("Test: divisible by ", ''))
            if_true = int(monkey_data[4].replace("If true: throw to monkey ", ''))
            if_false = int(monkey_data[5].replace("If false: throw to monkey ", ''))

            monkey = Monkey(items, operation, [divisible_by, if_true, if_false])
            self.monkeys.append(monkey)

    def pass_to_monkey(self, id, worry_level):
        self.monkeys[id].items.append(worry_level)

    def throw(self, worry_level, test):
        if worry_level % test[0] == 0: self.pass_to_monkey(test[1], worry_level)
        else: self.pass_to_monkey(test[2], worry_level)

    def get_new_worry_level(self, operation, value):
        value %= self.calculate_modulo()
        if operation[0] == "+":
            if operation[1] == "old": return value * 2
            else: return value + int(operation[1])
        if operation[1] == "old": return value * value
        else: return value * int(operation[1])

    def run_rounds(self, n, is_worry_lvl_divided_by_3):
        for _ in range(n):
            for monkey in self.monkeys:
                for i, value in enumerate(copy.deepcopy(monkey.items)):
                    worry_level = self.get_new_worry_level(monkey.operation, int(value))
                    if is_worry_lvl_divided_by_3:
                        worry_level = int(worry_level / 3)
                    self.throw(worry_level, monkey.test)
                    monkey.counter += 1
                monkey.items = []

    def get_monkey_business(self):
        values = []
        for m in self.monkeys: values.append(m.counter)
        max_1 = values.pop(values.index(max(values)))
        max_2 = values.pop(values.index(max(values)))
        return max_1 * max_2


mb_1, mb_2 = MonkeyBusiness(), MonkeyBusiness()
mb_1.map_data(DATA), mb_1.run_rounds(20, True)
mb_2.map_data(DATA), mb_2.run_rounds(10000, False)
print(f"Task #1: {mb_1.get_monkey_business()}")
print(f"Task #2: {mb_2.get_monkey_business()}")