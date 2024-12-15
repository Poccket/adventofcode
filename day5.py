from copy import copy
import common
manual_updates = common.load_day(5, False)
time = common.Timer()
for i in range(len(manual_updates)):
    manual_updates[i] = manual_updates[i].rstrip()

# day 1
rules = {}
for line in manual_updates:
    if "|" in line:
        if not (line[:line.index("|")] in rules.keys()):
            rules[line[:line.index("|")]] = []
        rules[line[:line.index("|")]] += [line[line.index("|")+1:]]
middles = 0
valid = []
for z, line in enumerate(manual_updates):
    valid += [True]
    if "," in line:
        pages = line.split(",")
        for i, page in enumerate(pages):
            if page in rules:
                for page2 in pages[:i]:
                    if page2 == page:
                        continue
                    if page2 in rules[page]:
                        valid[z] = False
        if valid[z]:
            middles += int(pages[int((len(pages) - 1)/2)])
common.print_result(middles)
time.stop()
time.restart()                  
# day 2
rules = {}
for line in manual_updates:
    if "|" in line:
        if not (line[:line.index("|")] in rules.keys()):
            rules[line[:line.index("|")]] = []
        rules[line[:line.index("|")]] += [line[line.index("|")+1:]]
middles = 0
for z, line in enumerate(manual_updates):
    if valid[z]:
        continue
    if "," in line:
        pages = line.split(",")
        for x, page in enumerate(pages):
            lower = 0
            higher = 0
            for y, page2 in enumerate(pages):
                if page == page2:
                    continue
                if page2 in rules[page]:
                    lower += 1
                else:
                    higher += 1
            if lower == higher:
                middles += int(page)
common.print_result(middles)
time.stop()