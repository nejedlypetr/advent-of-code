DATA = 'puzzle_input.txt'


def get_data(file):
    with open(file, "r") as data: return data.read()


def is_unique(string):
    unique_chars = []
    for char in string:
        if char in unique_chars: return False
        unique_chars.append(char)
    return True


def get_starting_index(string, number_of_different_letters):
    for i in range(number_of_different_letters, len(string)+1):
        substring = string[:i]
        if is_unique(substring[-number_of_different_letters:]):
            return len(substring)
    return None


print(get_starting_index(get_data(DATA), 4))
print(get_starting_index(get_data(DATA), 14))