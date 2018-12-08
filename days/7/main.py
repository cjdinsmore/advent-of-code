import re


def get_step_dict(lines):
    step_dict = {}
    for line in lines:
        match = re.match(r'Step\s(\w).*step\s(\w)', line)
        prereq_step, step = match.groups()
        if prereq_step not in step_dict:
            step_dict[prereq_step] = {
                'prereq': [],
                'time_left': abs(64 - ord(prereq_step)) + 60
            }
        if step not in step_dict:
            step_dict[step] = {
                'prereq': [],
                'time_left': abs(64 - ord(step)) + 60
            }
        if prereq_step not in step_dict[step]['prereq']:
            step_dict[step]['prereq'].append(prereq_step)
    return step_dict


def finish_step(step_dict, step):
    for step_key in step_dict:
        if step in step_dict[step_key]['prereq']:
            step_dict[step_key]['prereq'].remove(step)
    del step_dict[step]


def get_next_available(step_dict, being_worked_on=None):
    if being_worked_on is None:
        being_worked_on = []
    available = []
    for step_key in step_dict:
        if len(step_dict[step_key]['prereq']) == 0 and step_key not in being_worked_on:
            available.append(step_key)
    available.sort()
    if available:
        return available.pop(0)
    return False


def order_steps(step_dict):
    done = []
    next_step = get_next_available(step_dict)
    while next_step:
        finish_step(step_dict, next_step)
        done.append(next_step)
        next_step = get_next_available(step_dict)
    return done


def work_step(step_dict, step):
    step_dict[step]['time_left'] -= 1
    if step_dict[step]['time_left'] == 0:
        finish_step(step_dict, step)
        return True
    return False


def work_on_steps(step_dict):
    total_seconds = 0
    in_progress = []
    while step_dict:
        next_step = get_next_available(step_dict, being_worked_on=in_progress)
        while next_step and len(in_progress) < 5:
            in_progress.append(next_step)
            next_step = get_next_available(step_dict, in_progress)
        to_remove = []
        for step in in_progress:
            finished = work_step(step_dict, step)
            if finished:
                to_remove.append(step)
        for step in to_remove:
            in_progress.remove(step)
        total_seconds += 1
    return total_seconds


def main(input_filename):
    with open(input_filename) as input_file:
        lines = [line.rstrip() for line in input_file.readlines()]
        step_dict = get_step_dict(lines)
        print(''.join(order_steps(step_dict)))
        # part two
        step_dict = get_step_dict(lines)
        print(work_on_steps(step_dict))


main('input.txt')
