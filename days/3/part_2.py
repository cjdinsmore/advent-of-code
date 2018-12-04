from .common import parse_line


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
        if line_col_width_range.intersection(other_line_col_width_range) and line_row_height_range.intersection(
                other_line_row_width_range):
            return False
    return True


def main(input_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            if check_for_no_overlaps(line, lines):
                return line


if __name__ == '__main__':
    print(main('input.txt'))
