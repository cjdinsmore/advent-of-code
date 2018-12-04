def parse_line(line: str):
    split = line.split()
    col_row = split[2]
    col_start = int(col_row.split(',')[0])
    row_start = int(col_row.split(',')[1].replace(':', ''))
    width, height = split[3].split('x')
    return col_start, row_start, int(width), int(height)


def make_claim(matrix, col_start, row_start, width, height):
    for row in range(row_start, row_start + height):
        for col in range(col_start, col_start + width):
            matrix[row][col] += 1


def check_for_no_overlaps(line, lines):
    line = line.rstrip()
    col_start, row_start, width, height = parse_line(line)
    line_col_width_range = range(col_start, col_start + width)
    line_col_width_range = set(line_col_width_range)
    line_row_height_range = range(row_start, row_start + height)
    line_row_height_range = set(line_row_height_range)
    for other_line in lines:
        other_line = other_line.rstrip()
        if line == other_line:
            continue
        col_start, row_start, width, height = parse_line(other_line)
        other_line_col_width_range = range(col_start, col_start + width)
        other_line_row_width_range = range(row_start, row_start + height)
        if line_col_width_range.intersection(other_line_col_width_range) and line_row_height_range.intersection(other_line_row_width_range):
            return False
    return True


def part_two(input_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            if check_for_no_overlaps(line, lines):
                return line


def main(input_filename):
    fabric_matrix = [[0 for col in range(2000)] for row in range(2000)]
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            line = line.rstrip()
            col_start, row_start, width, height = parse_line(line)
            make_claim(fabric_matrix, col_start, row_start, width, height)
    double_claimed_squares = 0
    for row in range(len(fabric_matrix)):
        for col in range(len(fabric_matrix[row])):
            if fabric_matrix[row][col] >= 2:
                double_claimed_squares += 1
    return double_claimed_squares


if __name__ == '__main__':
    import os
    this_dir = os.path.abspath(os.path.dirname(__file__))
    input_dir = os.path.join(this_dir, 'inputs')
    print(main(os.path.join(input_dir, 'three.txt')))
    print(part_two(os.path.join(input_dir, 'three.txt')))
