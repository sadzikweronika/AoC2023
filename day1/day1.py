import aoc_lube

DATA = aoc_lube.fetch(year=2023, day=1).splitlines()
TEXT_TO_NUM = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}


def part1(data):
    results = []
    for line in data:
        digits = [s for s in line if s.isdigit()]
        results.append(int(digits[0] + digits[-1]))
    return sum(results)


def replace_in_string(s):
    for text, num in TEXT_TO_NUM.items():
        s = s.replace(text, text[0] + num + text[-1])
    return s


def part2():
    replaced_data = map(replace_in_string, DATA)
    return part1(replaced_data)


if __name__ == '__main__':
    print("Day 1 Part 1 result:", part1(DATA))
    print("Day 1 Part 2 result:", part2())
