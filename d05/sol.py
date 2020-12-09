def parse_data(filename: str) -> list:
    with open(filename) as f:
        passes = [line.strip() for line in f.readlines()]
    return passes

def decode(code: str) -> tuple:
    vertical = [1 if i == 'B' else 0 for i in code[:7]]
    horizontal = [1 if i == 'R' else 0 for i in code[7:]]
    vertical = int(''.join(map(str, vertical)), 2)
    horizontal = int(''.join(map(str, horizontal)), 2)
    return (vertical, horizontal)

def get_seats(passes: list) -> list:
    pass_nums = []
    for p in passes:
        row, col = decode(p)
        pass_nums.append((row << 3) + col)
    return pass_nums

def get_part1(passes: list) -> int:
    seats = get_seats(passes)
    return max(seats)

def get_missing(seats_taken: list) -> set:
    all_possible = {(row << 3) + col for row in range(128) for col in range(8)}
    return all_possible - set(seats_taken)

def get_part2(passes: list) -> int:
    seats_taken = set(get_seats(passes))
    missing = get_missing(seats_taken)
    for miss in missing:
        if miss + 1 in seats_taken and miss - 1 in seats_taken:
            return miss
    return -1

if __name__ == "__main__":
    passes = parse_data("data.txt")
    print(get_part1(passes))
    print(get_part2(passes))
