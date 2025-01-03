from copy import copy
import common
reports = common.load_day(2, False)

time = common.Timer()
# part 1
safety = 0
safe_change = (1,3)
for report in reports:
    report = list(map(int, report.split(" ")))
    ascend = report[0] < report[1]
    safe = True
    for i in range(len(report)-1):
        if (not ascend and report[i] <= report[i+1]) or\
               (ascend and report[i] >= report[i+1]):
            safe = False
            break
        if not (safe_change[0] <= abs(report[i] - report[i+1]) <= safe_change[1]):
            safe = False
            break
    if safe:
        safety += 1
common.print_result(safety)
time.stop()
time.restart()
# part 2
safety = 0
for report in reports:
    report = list(map(int, report.split(" ")))
    for i in range(len(report)):
        working_report = copy(report)
        working_report.pop(i)
        ascend = working_report[0] < working_report[1]
        safe = True
        for i in range(len(working_report)-1):
            if (not ascend and report[i] <= report[i+1]) or\
                   (ascend and report[i] >= report[i+1]):
                safe = False
                break
            if not (1 <= abs(report[i] - report[i+1]) <= 3):
                safe = False
                break
        if safe:
            safety += 1
            break
common.print_result(safety)
time.stop()