"""
https://adventofcode.com/2019/day/3

Simple approach, using a list of tuples (x, y) as path coordinates representation.
"""
with open('day-3.input', 'r') as input_f:
    path_sections_1, path_sections_2 = [line.split(',') for line in input_f.read().splitlines()]


# Star 1
def parse_path_section(path_section):
    return path_section[0], int(path_section[1:])


def move_horizontally(path, length):
    x, y = path[-1][0]
    start_x = x + 1 if length > 0 else x - 1
    end_x = x + length + 1 if length > 0 else x + length - 1
    for i in range(start_x, end_x, 1 if length > 0 else -1):
        path.append(((i, y), path[-1][1] + 1))

    return path


def move_vertically(path, length):
    x, y = path[-1][0]
    start_y = y + 1 if length > 0 else y - 1
    end_y = y + length + 1 if length > 0 else y + length - 1
    for j in range(start_y, end_y, 1 if length > 0 else -1):
        path.append(((x, j), path[-1][1] + 1))

    return path


def build_path(path_sections):
    path = [((0, 0), 0)]  # ((x, y), steps)
    for path_section in path_sections:
        direction, length = parse_path_section(path_section)
        if direction in 'RL':
            path = move_horizontally(path, length if direction == 'R' else -length)
        elif direction in 'UD':
            path = move_vertically(path, length if direction == 'U' else -length)

    return path


def get_intersections(path_coordinates_1, path_coordinates_2):
    intersections = set(path_coordinates_1) & set(path_coordinates_2)
    intersections.remove((0, 0))
    return intersections


def get_manhattan_distance_to_origin(coordinates):
    return abs(coordinates[0]) + abs(coordinates[1])


path_1 = build_path(path_sections_1)
path_2 = build_path(path_sections_2)
intersections = get_intersections([coordinates for coordinates, steps in path_1],
                                  [coordinates for coordinates, steps in path_2])
answer_1 = min(map(get_manhattan_distance_to_origin, intersections))
print(f'Answer 1: {answer_1}')


# Star 2
def get_intersection_cost(path_1, path_2, intersection):
    coordinates_1 = [coordinates for coordinates, steps in path_1]
    coordinates_2 = [coordinates for coordinates, steps in path_2]
    return path_1[coordinates_1.index(intersection)][1] + path_2[coordinates_2.index(intersection)][1]


answer_2 = min(map(lambda intersection: get_intersection_cost(path_1, path_2, intersection),
                   intersections))
print(f'Answer 2: {answer_2}')
