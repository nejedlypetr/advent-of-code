DATA = "puzzle_input.txt"


def get_data(file):
    with open(file, "r") as data:
        return data.read().splitlines()


def letter_value(letter):
    if letter.isupper():
        return ord(letter) - ord("A") + 27
    return ord(letter) - ord("a") + 1


def get_sum_of_priorities(file):
    total = 0
    rucksacks = get_data(file)
    for rucksack in rucksacks:
        split = len(rucksack) // 2
        left, right = rucksack[:split], rucksack[split:]
        common_char = (set(left) & set(right)).pop()
        total += letter_value(common_char)
    return total


def get_sum_of_badge_priorities(file):
    total = 0
    rucksacks = get_data(file)
    for i in range(0, len(rucksacks), 3):
        common_char = ( set(rucksacks[i]) & set(rucksacks[i+1]) & set(rucksacks[i+2]) ).pop()
        total += letter_value(common_char)
    return total


print(get_sum_of_priorities(DATA))
print(get_sum_of_badge_priorities(DATA))