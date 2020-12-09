def parse_data(filename: str) -> dict:
    def parse_passport(psp):
        fields = sum([line.split(" ") for line in psp.split("\n")], [])
        return {field[:3]: field[4:] for field in fields}

    with open(filename) as f:
        f = f.read().split("\n\n")
        return [parse_passport(psp) for psp in f]

def is_valid1(passport: dict) -> bool:
    return len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)

def get_part1(passports: dict) -> int:
    return len([1 for psp in passports if is_valid1(psp)])

def is_byr_valid(passport: dict) -> bool:
    byr = int(passport["byr"])
    return byr >= 1920 and byr <= 2002

def is_iyr_valid(passport: dict) -> bool:
    iyr = int(passport["iyr"])
    return iyr >= 2010 and iyr <= 2020

def is_eyr_valid(passport: dict) -> bool:
    eyr = int(passport["eyr"])
    return eyr >= 2020 and eyr <= 2030

import re
from functools import reduce

def is_hgt_valid(passport: dict) -> bool:
    hgt = passport["hgt"]
    m = re.match(r"^(\d+)(cm|in)$", hgt)
    if m:
        value, unit = m.group(1), m.group(2)
        if unit == 'cm':
            return int(value) >= 150 and int(value) <= 193
        elif unit == 'in':
            return int(value) >= 59 and int(value) <= 76
    else:
        return False

def is_hcl_valid(passport: dict) -> bool:
    hcl = passport["hcl"]
    m = re.match(r"^#([a-f]|[0-9]){6}$", hcl)
    if m:
        return True
    return False

def is_ecl_valid(passport: dict) -> bool:
    return passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def is_pid_valid(passport: dict) -> bool:
    pid = passport["pid"]
    m = re.match(r"^[0-9]{9}$", pid)
    if m:
        return True
    return False

def is_valid2(passport: dict) -> bool:
    validators = [
        is_valid1,
        is_byr_valid,
        is_ecl_valid,
        is_eyr_valid,
        is_hcl_valid,
        is_hgt_valid,
        is_iyr_valid,
        is_pid_valid
    ]

    return reduce(lambda so_far, next_validator: so_far and next_validator(passport), validators, True)

def get_part2(passports: dict) -> int:
    return len([1 for psp in passports if is_valid2(psp)])


if __name__ == "__main__":
    passports = parse_data("data.txt")
    print(get_part1(passports))
    print(get_part2(passports))