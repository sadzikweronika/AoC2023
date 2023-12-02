import aoc_lube

DATA = aoc_lube.fetch(year=2023, day=2).splitlines()
THRESHOLDS = {'red': 12, 'green': 13, 'blue': 14}


def part1():
    total_score = 0
    for game_index, game_data in enumerate(DATA):
        field_of_views = game_data.split(':')[1].split(';')
        game_valid = True
        for fov in field_of_views:
            if not game_valid:
                break
            for color_data in fov.split(','):
                count, color = color_data.split()
                count = int(count)
                if count > THRESHOLDS[color]:
                    game_valid = False
                    break
        if game_valid:
            total_score += game_index + 1

    return total_score


def part2():
    total = 0
    for game in DATA:
        max_values = {'red': 0, 'green': 0, 'blue': 0}
        field_of_views = game.split(':')[1].split(';')
        for fov in field_of_views:
            for color_info in fov.split(','):
                count, color = map(str.strip, color_info.split())
                count = int(count)
                max_values[color] = max(max_values[color], count)
        total += max_values['red'] * max_values['green'] * max_values['blue']

    return total


if __name__ == "__main__":
    print('Day 2 Part 1 result:', part1())
    print('Day 2 Part 2 result:', part2())

