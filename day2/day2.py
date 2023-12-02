import aoc_lube

DATA = aoc_lube.fetch(year=2023, day=2).splitlines()
THRESHOLDS = {'red': 12, 'green': 13, 'blue': 14}


def part1():
    total_score = 0
    for game_index, game_data in enumerate(DATA):
        games = game_data.split(':')[1].split(';')
        if all(int(count) <= THRESHOLDS[color]
               for game in games
               for count, color in (color_data.split() for color_data in game.split(','))):
            total_score += game_index + 1
    return total_score


def part2():
    total = 0
    for line in DATA:
        max_values = {'red': 0, 'green': 0, 'blue': 0}
        games = line.split(':')[1].split(';')
        for game in games:
            for color_info in game.split(','):
                count, color = map(str.strip, color_info.split())
                count = int(count)
                max_values[color] = max(max_values[color], count)
        total += max_values['red'] * max_values['green'] * max_values['blue']

    return total


if __name__ == "__main__":
    print('Day 2 Part 1 result:', part1())
    print('Day 2 Part 2 result:', part2())
