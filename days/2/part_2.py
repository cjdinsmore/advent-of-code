import Levenshtein


def compare_against_all_lines(line, lines):
    for other_line in lines:
        if Levenshtein.distance(line, other_line) == 1:
            return other_line
    return False


def main(input_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            match = compare_against_all_lines(line, lines)
            if match:
                return line, match


if __name__ == '__main__':
    print(main('input.txt'))
