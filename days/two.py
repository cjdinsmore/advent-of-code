import Levenshtein


def get_occurrences(line: str):
    occurs_twice = False
    occurs_thrice = False
    for ch in line:
        if line.count(ch) == 2:
            occurs_twice = True
        elif line.count(ch) == 3:
            occurs_thrice = True
    return occurs_twice, occurs_thrice


def get_checksum(input_filename):
    with open(input_filename, 'r') as input_file:
        occurrence_dict = {
            2: [],
            3: []
        }
        for line in input_file:
            occurs_twice, occurs_thrice = get_occurrences(line)
            if occurs_twice:
                occurrence_dict[2].append(line)
            if occurs_thrice:
                occurrence_dict[3].append(line)
        return len(occurrence_dict[2]) * len(occurrence_dict[3])


def compare_against_all_lines(line, lines):
    for other_line in lines:
        if Levenshtein.distance(line, other_line) == 1:
            return other_line
    return False


def get_prototype_fabric(input_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            match = compare_against_all_lines(line, lines)
            if match:
                return line, match


if __name__ == '__main__':
    import os
    this_dir = os.path.abspath(os.path.dirname(__file__))
    input_dir = os.path.join(this_dir, 'inputs')
    print(get_checksum(os.path.join(input_dir, 'two.txt')))
    print(get_prototype_fabric(os.path.join(input_dir, 'two.txt')))
