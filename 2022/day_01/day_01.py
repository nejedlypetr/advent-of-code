DATA = "puzzle_input.txt"


def get_max_value(file):
  with open(file, "r") as data:
    max_value = 0
    current_value = 0

    for line in data:
      if line == "\n":
        if current_value > max_value:
          max_value = current_value
        current_value = 0
      else:
        current_value += int(line.removesuffix("\n"))

  return max_value


def get_sum_of_n_max_values(file, n):
  with open(file, "r") as data:
    max_values = [0] * n
    current_value = 0

    for line in data:
      if line == "\n":
        for i in range(len(max_values)):
          if current_value > max_values[i]:
            max_values[i] = current_value
            break
        current_value = 0
      else:
        current_value += int(line.removesuffix("\n"))

  return sum(max_values)


print(get_max_value(DATA))
print(get_sum_of_n_max_values(DATA, 3)) 