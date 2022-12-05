import copy

DATA = "puzzle_input.txt"
original_stacks = [
    [],
    ['B', 'S', 'V', 'Z', 'G', 'P', 'W'],
    ['J', 'V', 'B', 'C', 'Z', 'F'],
    ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
    ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
    ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
    ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
    ['L', 'G', 'C', 'Z', 'V'],
    ['N', 'L', 'G'],
    ['J', 'F', 'H', 'C']
]


def get_data(file):
    with open(file, "r") as data: return data.read().splitlines()


def move_crates(stacks, num_of_crates, from_stack, to_stack):
    for i in range(num_of_crates):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)


def move_crates_keeping_order(stacks, num_of_crates, from_stack, to_stack):
    crates = stacks[from_stack][-num_of_crates:]
    del stacks[from_stack][-num_of_crates:]
    stacks[to_stack] += crates


def get_rearrangement(stacks, instructions, keep_order):
    new_stacks = copy.deepcopy(stacks)
    for move in instructions:
        move = move.replace('move', '').replace('from ', '').replace('to ', '').split()
        if keep_order: 
            move_crates_keeping_order(new_stacks, int(move[0]), int(move[1]), int(move[2]))
        else:
            move_crates(new_stacks, int(move[0]), int(move[1]), int(move[2]))
    return new_stacks


def get_top_crates(stacks):
    result = ""
    for stack in copy.deepcopy(stacks):
        if stack: result += stack.pop()
    return result


new_stacks_1 = get_rearrangement(original_stacks, get_data(DATA), False)
new_stacks_2 = get_rearrangement(original_stacks, get_data(DATA), True)

print(f"Original (top crates): {get_top_crates(original_stacks)}")
print(f"Task #1 (top crates): {get_top_crates(new_stacks_1)}")
print(f"Task #2 (top crates): {get_top_crates(new_stacks_2)}")