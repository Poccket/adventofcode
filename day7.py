import common
test_data = common.load_day(7, False)
time = common.Timer()
def rebase(n, b, pad=0):
    if n == 0:
        return '0'.rjust(pad, '0')
    nums = []
    while n:
        n, r = divmod(n, b)
        nums.append(str(r))
    return ''.join(reversed(nums)).rjust(pad, '0')

data = []
for datum in test_data:
    data += [[datum.split(":")[0], datum.split(": ")[1].split(" ")]]

operators = ("+","*")
total = 0
for datum in data:
    for i in range(2**(len(datum[1])-1)):
        evald = 0
        for x, var in enumerate(datum[1]):
            if x == 0:
                evald = int(var)
            else:
                evald = eval(f"{evald}{operators[(i >> x-1) & 1]}{var}")
                if evald > int(datum[0]):
                    break
        if evald == int(datum[0]):
            total += evald
            break
common.print_result(total)
time.stop()
time.restart()

# Part 2
operators = ("+","*","||")
total = 0
for datum in data:
    for i in range(3**(len(datum[1])-1)):
        tern = rebase(i, 3, pad=len(datum[1]))
        evald = 0
        for x, var in enumerate(datum[1]):
            if x == 0:
                evald = int(var)
            else:
                op = operators[int(tern[-x])]
                if op == "||":
                    evald = int(str(evald) + var)
                else:
                    evald = eval(f"{evald}{op}{var}")
                    if evald > int(datum[0]):
                        break
        if evald == int(datum[0]):
            total += evald
            break
common.print_result(total)
time.stop()