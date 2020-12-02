def parse_data(filename: str) -> set:
    with open(filename) as f:
        data = [int(line) for line in f]
    return set(data)

def get_part1(data_set: set) -> int:
    for num in data_set:
        diff = 2020 - num
        if diff in data_set:
            return num * diff
    return 0

def get_part2(data_set: set) -> int:
    partials = {}
    for i in data_set:
        for j in data_set:
            partials[i+j] = [i, j]
    for num in partials.keys():
        diff = 2020 - num
        if diff in data_set:
            return diff * partials[num][0] * partials[num][1]
    return 0




if __name__ == '__main__':
    data_set = parse_data("data.txt")
    print(get_part1(data_set))
    print(get_part2(data_set))

