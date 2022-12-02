DATA = "puzzle_input.txt"

def get_total_score(file):
    points = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
    }
    total = 0
    with open(file, "r") as data:
        for line in data:
            total += points[line.removesuffix("\n")]
    return total

def get_total_score_elf_plan(file):
    points = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
    }
    total = 0
    with open(file, "r") as data:
        for line in data:
            total += points[line.removesuffix("\n")]
    return total


print(get_total_score(DATA))
print(get_total_score_elf_plan(DATA))