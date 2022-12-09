DATA = 'puzzle_input.txt'

def get_data(file):
    with open(file, "r") as data: return data.read().splitlines()

def is_cd_command(line):
    if line.split()[0] == "$" and line.split()[1] == "cd":
        return True
    return False

def is_ls_command(line):
    if line.split()[0] == "$" and line.split()[1] == "ls":
        return True
    return False

def run_commands(data, directories):
    path = ["$"]
    value = 0
    was_prev_go_back_cmd = False
    for line in data:
        l = line.split()
        if is_cd_command(line):
            if l[2] == "/": pass
            elif l[2] == "..": 
                set_value_to_directory_by_path(directories, path, value)
                path.pop()
                relative_path = "/".join(path)
                value += directories[relative_path]
                directories[relative_path] = value
                was_prev_go_back_cmd = True
            else: 
                if not was_prev_go_back_cmd:
                    set_value_to_directory_by_path(directories, path, value) 
                value = 0
                path.append(l[2])
                was_prev_go_back_cmd = False
        elif l[0].isnumeric():
            value += int(l[0])
    
    add_value_to_remaining_directories(directories, path, value)

def set_value_to_directory_by_path(directories, path, value):
    relative_path = "/".join(path)
    directories[relative_path] = value

def add_value_to_remaining_directories(directories, path, value):
    for directory in path.copy():
        relative_path = "/".join(path)
        try: directories[relative_path] += value
        except: directories[relative_path] = value
        value = directories[relative_path]
        path.pop()

def get_total(directories):
    total = 0
    for key in directories:
        if directories[key] <= 100000: total += directories[key]
    return total

def calculate_needed_space(directories, update_size):
    return update_size - (70_000_000 - directories["$"])

def get_dir_for_delete(directories, update_size):
    needed_space = calculate_needed_space(directories, update_size)
    dir_value = directories["$"]
    for key in directories:
        if directories[key] >= needed_space and directories[key] < dir_value:
            dir_value = directories[key]
    return dir_value


directories = {}
run_commands(get_data(DATA), directories)

print(f"Task #1: {get_total(directories)}")
print(f"Task #2: {get_dir_for_delete(directories, 30_000_000)}")