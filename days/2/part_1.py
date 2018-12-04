def get_occurrences(line: str):
    occurs_twice = False
    occurs_thrice = False
    for ch in line:
        if line.count(ch) == 2:
            occurs_twice = True
        elif line.count(ch) == 3:
            occurs_thrice = True
    return occurs_twice, occurs_thrice


def main(input_filename):
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


if __name__ == '__main__':
    print(main('input.txt'))
