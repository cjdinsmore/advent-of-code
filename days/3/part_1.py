from .common import make_claim, parse_line


def main(input_filename):
    fabric_matrix = [[0 for col in range(1000)] for row in range(1000)]
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
    print(main('input.txt'))
