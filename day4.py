import common
word_search = common.load_day(4, False)
time = common.Timer()
# part 1
directions = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1)]
count = 0
for x in range(len(word_search)):
    for y in range(len(word_search[x])):
        if word_search[x][y] == "X":
            for dx, dy in directions:
                if 0 <= x+(dx*3) < len(word_search) and 0 <= y+(dy*3) < len(word_search[0])-1:
                    if word_search[x+dx][y+dy] == "M" and\
                       word_search[x+(dx*2)][y+(dy*2)] == "A" and\
                       word_search[x+(dx*3)][y+(dy*3)] == "S":
                        count += 1
common.print_result(count)
time.stop()
time.restart()
# part 2
neighbors = [(-1, -1), (-1, 1),
             ( 1, -1), ( 1, 1)]
count = 0
for x in range(1, len(word_search)-1):
    for y in range(1, len(word_search[x])-1):
        if word_search[x][y] == "A":
            corners = word_search[x+neighbors[0][0]][y+neighbors[0][1]] +\
                      word_search[x+neighbors[1][0]][y+neighbors[1][1]] +\
                      word_search[x+neighbors[2][0]][y+neighbors[2][1]] +\
                      word_search[x+neighbors[3][0]][y+neighbors[3][1]]
            if corners in ("MMSS","MSMS","SSMM","SMSM"):
                count += 1
common.print_result(count)
time.stop()