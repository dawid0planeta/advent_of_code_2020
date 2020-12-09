import numpy as np
from functools import reduce

def convert_to_int(char: str) -> int:
    if char == ".":
        return 0
    return 1


def parse_data(filename: str) -> np.array:
    vect_convert = np.vectorize(convert_to_int)
    python_array = []
    with open(filename, "r") as f:
        for line in f:
            python_array.append(list(line.strip()))

    return np.array(list(map(vect_convert, np.array(python_array)))) #awful

def prepare_data(raw_data: np.array,) -> np.array:
    stacked = np.hstack((raw_data, raw_data))

    while stacked.shape[1] // 7 < stacked.shape[0]:
        stacked = np.hstack((stacked, raw_data))

    return stacked

def get_new_coor(di: int, dj: int):
    (i, j) = (0, 0)
    while 1:
        (i, j) = (i + di, j + dj)
        yield (i, j)

def get_slope_count(raw_data: np.array, di: int, dj: int) -> int:
    stacked = prepare_data(raw_data)
    count = 0
    coors_gen = get_new_coor(di, dj)
    new_coors = next(coors_gen)

    while new_coors[0] < stacked.shape[0]:
        count += stacked[new_coors]
        new_coors = next(coors_gen)

    return count

def get_part1(raw_data: np.array) -> int:
    return get_slope_count(raw_data, 1, 3)

def get_part2(raw_data: np.array) -> int:
    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
    slopes_count = [get_slope_count(raw_data, *slope) for slope in slopes]
    print(slopes_count)
    return reduce(lambda a, b: a*b, slopes_count)



if __name__ == "__main__":
    raw_data = parse_data("data.txt")
    print(get_part1(raw_data))
    print(get_part2(raw_data))