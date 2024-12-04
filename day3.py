import re
with open('inputs/day3.txt', 'r') as f:
    program = f.read()

# part 1
matches = re.findall(r"mul\([0-9]+\,[0-9]+\)", program)
result = 0
for match in matches:
    result += (int(match[4:match.find(",")]) * int(match[match.find(",")+1:-1]))
print(result)

# part 2
matches = re.findall(r"(?:\A|(?:do\(\)))(?:[\s\S]*?)(?:(?:don't\(\))|\Z)", program) # Regex Hell
result = 0
for match in matches:
    submatches = re.findall(r"mul\([0-9]+\,[0-9]+\)", match)
    for submatch in submatches:
        result += (int(submatch[4:submatch.find(",")]) * int(submatch[submatch.find(",")+1:-1]))
print(result)