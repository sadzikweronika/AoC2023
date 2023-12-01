import aoc_lube
from num2words import num2words

DATA = aoc_lube.fetch(year=2023, day=1).splitlines()
TEXT_TO_NUM = {num2words(num): str(num) for num in range(1, 10)}


def part1(data):
    total = 0
    for line in data:
        digits = [s for s in line if s.isdigit()]
        total += int(digits[0] + digits[-1])

    return total


def part1_oneliner(data):
    # it's trash regarding readabilty tbh
    total = sum(int(digits[0] + digits[-1]) for line in data for digits in [[s for s in line if s.isdigit()]])
    return total


def part1_generator(data):
    total = 0
    for line in data:
        first_digit = next(s for s in line if s.isdigit())
        last_digit = next(s for s in reversed(line) if s.isdigit())
        total += int(first_digit + last_digit)

    return total


def replace_in_string(s):
    for text, num in TEXT_TO_NUM.items():
        s = s.replace(text, text[0] + num + text[-1])
    return s


def part2():
    replaced_data = map(replace_in_string, DATA)
    return part1(replaced_data)


if __name__ == '__main__':
    print('Day 1 Part 1 result:', part1(DATA))
    print('Day 1 Part 2 result:', part2())
