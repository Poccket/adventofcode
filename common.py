def load_day(num, example=True, lines=True):
    if example:
        example = input("Enter for example, anything else for non-example >") == ""
    with open(f'inputs/day{num}{"example" if example else ""}.txt', 'r') as f:
        if lines:
            return f.readlines()
        else:
            return f.read()