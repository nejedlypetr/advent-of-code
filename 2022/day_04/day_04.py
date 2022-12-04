DATA = "puzzle_input.txt"


def get_data(file):
    with open(file, "r") as data:
        return data.read().splitlines()


def get_totals(data):
    total_fully_contained_pairs = 0
    total_ovelaps = 0
    for value in data:
        pair = value.split(",")
        range_one, range_two = pair[0].split("-"), pair[1].split("-")
        numbers_1 = range(int(range_one[0]), int(range_one[1])+1)
        numbers_2 = range(int(range_two[0]), int(range_two[1])+1)
        if (int(range_one[0]) in numbers_2 and int(range_one[1]) in numbers_2) or (int(range_two[0]) in numbers_1 and int(range_two[1]) in numbers_1):
            total_fully_contained_pairs += 1
        if int(range_one[0]) in numbers_2 or int(range_one[1]) in numbers_2 or int(range_two[0]) in numbers_1 or int(range_two[1]) in numbers_1:
            total_ovelaps += 1
    return total_fully_contained_pairs, total_ovelaps


print(get_totals(get_data(DATA)))