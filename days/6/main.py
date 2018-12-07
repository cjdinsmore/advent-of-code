def manhattan_distance(location_a, location_b):
    return abs(location_a[0] - location_b[0]) + abs(location_a[1] - location_b[1])


def get_dimensions(points_list):
    max_x = max(points_list, key=lambda x: x[0])
    max_y = max(points_list, key=lambda x: x[1])
    return max_x[0] + 1, max_y[1] + 1


def get_closest_point_key(location, points_dict):
    distance_array = []  # array of tuples of form (point_key, distance)
    for point_key in points_dict:
        distance_array.append((point_key, manhattan_distance(location, points_dict[point_key])))
    shortest = min(distance_array, key=lambda x: x[1])
    sum_to_all_distances = sum(x[1] for x in distance_array)
    if sum(x[1] == shortest[1] for x in distance_array) > 1:
        return None, sum_to_all_distances
    return shortest[0], sum_to_all_distances


def create_and_fill_grids(points_list, points_dict):
    max_x, max_y = get_dimensions(points_list)
    point_key_grid = [[-1 for _ in range(max_x)] for _ in range(max_y)]
    total_distance_grid = [[-1 for _ in range(max_x)] for _ in range(max_y)]
    for y in range(len(point_key_grid)):
        for x in range(len(point_key_grid[y])):
            point_key, sum_to_all_distances = get_closest_point_key([x, y], points_dict)
            point_key_grid[y][x] = point_key
            total_distance_grid[y][x] = sum_to_all_distances
    return point_key_grid, total_distance_grid


def part_one(grid, points_dict):
    # eliminate infinite points
    for point_key in grid[0]:
        if point_key in points_dict:
            del points_dict[point_key]
    for point_key in grid[-1]:
        if point_key in points_dict:
            del points_dict[point_key]
    for row in grid:
        if row[0] in points_dict:
            del points_dict[row[0]]
        if row[-1] in points_dict:
            del points_dict[row[-1]]
    totals = []
    for point_key in points_dict:
        total = 0
        for row in grid:
            total += sum(pk == point_key for pk in row)
        totals.append((point_key, total))
    return max(totals, key=lambda x: x[1])


def part_two(distances_grid):
    total = 0
    for row in distances_grid:
        total += sum(x < 10000 for x in row)
    return total


def main(input_filename):
    with open(input_filename) as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]
        points_dict = {}
        points_list = []
        for line in lines:
            str_points = line.split(',')
            point = (int(str_points[0]), int(str_points[1]))
            points_list.append(point)
            points_dict[str(point)] = point
        point_key_grid, distances_grid = create_and_fill_grids(points_list, points_dict)
        print(part_one(point_key_grid, points_dict))
        print(part_two(distances_grid))


main('input.txt')
