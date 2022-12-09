DATA = "puzzle_input.txt"

def get_data(file):
    with open(file, "r") as data: return data.read().splitlines()

def count_outside_trees(grid):
    top_bottom = 2 * len(grid[0])
    left_right = 2 * len(grid)
    return top_bottom + left_right

def map_columns_to_lines(grid):
    new_grid = []
    for num in range(len(grid[0])):
        column = ""
        for row in range(len(grid)):
            column += grid[row][num]
        new_grid.append(column)
    return new_grid

def count_trees(rows, columns):
    visible_trees = 0
    for i in range(0, len(rows)):
        for j in range(0, len(columns)):
            left, right = rows[i][:j], rows[i][(j+1):]
            top, bottom = columns[j][:i], columns[j][(i+1):]
            tree_height = rows[i][j]

            if is_tree_visible([left, right, top, bottom], tree_height):
                visible_trees += 1
    return visible_trees
    
def is_tree_visible(list_of_trees_around, tree_height):
    is_visible = 0
    for trees in list_of_trees_around:
        for height in trees:
            if height >= tree_height:
                is_visible += 1
                break
    if is_visible == 4: return False
    return True

def get_best_spot(rows, columns):
    best_score = 0
    for i in range(0, len(rows)):
        for j in range(0, len(columns)):
            left, right = rows[i][:j], rows[i][(j+1):]
            top, bottom = columns[j][:i], columns[j][(i+1):]
            left, top = left[::-1], top[::-1]
            tree_height = rows[i][j]

            current_tree_score = get_tree_score([left, right, top, bottom], tree_height)
            if current_tree_score > best_score:
                best_score = current_tree_score
    return best_score

def number_of_smaller_trees(trees, tree_height):
    trees_count = 0
    for height in trees:
        trees_count += 1
        if height >= tree_height: return trees_count
    return trees_count

def get_tree_score(list_of_trees_around, tree_height):
    score = 1
    for trees in list_of_trees_around:
        score *= number_of_smaller_trees(trees, tree_height)
    return score


rows = get_data(DATA)
columns = map_columns_to_lines(get_data(DATA))

print(f"Task #1: {count_trees(rows, columns)}")
print(f"Task #2: {get_best_spot(rows, columns)}")