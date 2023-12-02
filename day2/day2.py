import aoc_lube
from functools import reduce


def preprocess_data(raw_data):
    processed_data = []
    for line in raw_data:
        games = line.split(':')[1].split(';')
        game_data = [[int(count), color]
                     for game in games
                     for count, color in (color_data.split() for color_data in game.split(','))]
        processed_data.append(game_data)
    return processed_data


DATA = preprocess_data(aoc_lube.fetch(year=2023, day=2).splitlines())
THRESHOLDS = {'red': 12, 'green': 13, 'blue': 14}


def part1():
    total_score = 0
    for game_index, game_data in enumerate(DATA):
        if all(count <= THRESHOLDS[color] for count, color in game_data):
            total_score += game_index + 1
    return total_score


def part2():
    total = 0
    for game_data in DATA:
        max_values = {'red': 0, 'green': 0, 'blue': 0}
        for count, color in game_data:
            max_values[color] = max(max_values[color], count)
        total += reduce(lambda x, y: x * y, max_values.values(), 1)
    return total


if __name__ == "__main__":
    print('Day 2 Part 1 result:', part1())
    print('Day 2 Part 2 result:', part2())
