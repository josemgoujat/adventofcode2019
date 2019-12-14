"""
https://adventofcode.com/2019/day/3

Alternative approach using dictionaries as data structure for path coordinates:
{
    x1: {y1: True, y2: True},
    x2: {y1: True, y3: True, y4: True}
}
Slightly faster, probably because of doing an extra intersection that discards non shared x values
between the two paths.
"""
with open('day-3.input', 'r') as input_f:
    path_steps_1, path_steps_2 = [line.split(',') for line in input_f.read().splitlines()]


# Star 1
def parse_step(step):
    return step[0], int(step[1:])


def move_horizontally(path_coordinates, x, y, length):
    _range = range(x, x + length, 1 if length > 0 else -1)
    for i in _range:
        if path_coordinates.get(i):
            path_coordinates[i].update({y: True})
        else:
            path_coordinates[i] = {y: True}

    return path_coordinates, x + length


def move_vertically(path_coordinates, x, y, length):
    _range = range(y, y + length, 1 if length > 0 else -1)
    if path_coordinates.get(x):
        path_coordinates[x].update({j: True for j in _range})
    else:
        path_coordinates[x] = {j: True for j in _range}

    return path_coordinates, y + length


def build_path_coordinates(path_steps):
    x, y = 0, 0
    path_coordinates = {}
    for step in path_steps:
        direction, length = parse_step(step)
        if direction in 'RL':
            path_coordinates, x = move_horizontally(path_coordinates, x, y, length if direction == 'R' else -length)
        elif direction in 'UD':
            path_coordinates, y = move_vertically(path_coordinates, x, y, length if direction == 'U' else -length)

    return path_coordinates


def get_intersections(path_coordinates_1, path_coordinates_2):
    intersections = []
    for x in set(path_coordinates_1.keys()) & set(path_coordinates_2.keys()):
        for y in set(path_coordinates_1[x].keys()) & set(path_coordinates_2[x].keys()):
            if not (x == 0 and y == 0):
                intersections.append((x, y))

    return intersections


def get_manhattan_distance_to_origin(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


path_coordinates_1 = build_path_coordinates(path_steps_1)
path_coordinates_2 = build_path_coordinates(path_steps_2)
answer_1 = min(map(get_manhattan_distance_to_origin, get_intersections(path_coordinates_1, path_coordinates_2)))
print(f'Answer 1: {answer_1}')
