def parse_data(filename: str) -> list:
    data = []
    with open(filename) as f:
        for line in f:
            splitted = line.split(":")
            data
            data.append([splitted[1].strip(), splitted[0]])
    return data

def get_part1(data: list) -> int:
    count = 0
    for line in data:
        paswd, policy = line
        occurances, letter = policy.split(" ")
        lower, upper = map(int, occurances.split("-"))
        letter_count = paswd.count(letter)
        if letter_count >= lower and letter_count <= upper:
            count += 1
    return count

def get_part2(data: list) -> int:
    count = 0
    for line in data:
        paswd, policy = line
        occurances, letter = policy.split(" ")
        pos1, pos2 = map(int, occurances.split("-"))
        if (paswd[pos1 - 1] == letter) ^ (paswd[pos2 - 1] == letter):
            count += 1
    return count


if __name__ == "__main__":
    data = parse_data("data.txt")
    print(get_part1(data))
    print(get_part2(data))

