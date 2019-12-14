"""
https://adventofcode.com/2019/day/3

Simple approach, using a list of tuples (x, y) as path coordinates representation.
More clear but slightly slower than alternative using dictionaries (see day-3-alternative.py).
"""
with open('day-3.input', 'r') as input_f:
    path_steps_1, path_steps_2 = [line.split(',') for line in input_f.read().splitlines()]


def parse_step(step):
    return step[0], int(step[1:])


def move_horizontally(path_coordinates, x, y, length):
    for i in range(x, x + length, 1 if length > 0 else -1):
        path_coordinates.append((i, y))

    return path_coordinates, x + length


def move_vertically(path_coordinates, x, y, length):
    for j in range(y, y + length, 1 if length > 0 else -1):
        path_coordinates.append((x, j))

    return path_coordinates, y + length


def build_path_coordinates(path_steps):
    x, y = 0, 0
    path_coordinates = []
    for step in path_steps:
        direction, length = parse_step(step)
        if direction in 'RL':
            path_coordinates, x = move_horizontally(path_coordinates, x, y, length if direction == 'R' else -length)
        elif direction in 'UD':
            path_coordinates, y = move_vertically(path_coordinates, x, y, length if direction == 'U' else -length)

    return path_coordinates


def get_intersections(path_coordinates_1, path_coordinates_2):
    intersections = set(path_coordinates_1) & set(path_coordinates_2)
    intersections.remove((0, 0))
    return intersections


def get_manhattan_distance_to_origin(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


path_coordinates_1 = build_path_coordinates(path_steps_1)
path_coordinates_2 = build_path_coordinates(path_steps_2)
answer_1 = min(map(get_manhattan_distance_to_origin, get_intersections(path_coordinates_1, path_coordinates_2)))
print(f'Answer 1: {answer_1}')
