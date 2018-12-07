def do_full_reactions(polymer):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    polymer_length = -1
    new_polymer_length = 0
    while polymer_length != new_polymer_length:
        polymer_length = len(polymer)
        for ch in alphabet:
            polymer = polymer.replace(f'{ch}{ch.upper()}', '')
            polymer = polymer.replace(f'{ch.upper()}{ch}', '')
        new_polymer_length = len(polymer)
    return polymer


def part_one(input_filename):
    with open(input_filename) as input_file:
        polymer = input_file.read()
        polymer = polymer.rstrip()
        polymer = do_full_reactions(polymer)
    return len(polymer)


def get_length_from_letter(polymer, letter):
    test_polymer = polymer
    test_polymer = test_polymer.replace(letter, '')
    test_polymer = test_polymer.replace(letter.upper(), '')
    test_polymer = do_full_reactions(test_polymer)
    return len(test_polymer)


def part_two(input_filename):
    lowest_length = 50000
    lowest_length_letter = None
    with open(input_filename) as input_file:
        polymer = input_file.read()
        polymer = polymer.rstrip()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            length_from_letter = get_length_from_letter(polymer, letter)
            if length_from_letter < lowest_length:
                lowest_length = length_from_letter
                lowest_length_letter = letter
    return lowest_length_letter, lowest_length


if __name__ == '__main__':
    print(part_one('input.txt'))
    print(part_two('input.txt'))
