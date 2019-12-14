"""
https://adventofcode.com/2019/day/3
"""
with open('day-3.input', 'r') as input_f:
    path_steps_1, path_steps_2 = [line.split(',') for line in input_f.read().splitlines()]


def parse_step(step):
    return step[0], int(step[1:])


def build_path_coordinates(path_steps):
    x, y = 0, 0
    path_coordinates = {}
    for step in path_steps:
        direction, length = parse_step(step)

        if direction == 'R':
            for k in range(x, x + length):
                if path_coordinates.get(k):
                    path_coordinates[k].update({y: True})
                else:
                    path_coordinates[k] = {y: True}
            x += length
        elif direction == 'L':
            for k in range(x, x - length, -1):
                if path_coordinates.get(k):
                    path_coordinates[k].update({y: True})
                else:
                    path_coordinates[k] = {y: True}
            x -= length
        elif direction == 'U':
            if path_coordinates.get(x):
                path_coordinates[x].update({k: True for k in range(y, y + length)})
            else:
                path_coordinates[x] = {k: True for k in range(y, y + length)}
            y += length
        elif direction == 'D':
            if path_coordinates.get(x):
                path_coordinates[x].update({k: True for k in range(y, y - length, -1)})
            else:
                path_coordinates[x] = {k: True for k in range(y, y - length, -1)}
            y -= length

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