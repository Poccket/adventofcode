import common
node_map = common.load_day(8, map=True)

time = common.Timer()
# Part 1
antinodes = []
for ay, aRow in enumerate(node_map):
    for ax, aColumn in enumerate(aRow):
        if aColumn in (".", "#"):
            continue
        for by, bRow in enumerate(node_map):
            for bx, bColumn in enumerate(bRow):
                if ay == by and ax == bx:
                    continue
                if aColumn != bColumn:
                    continue
                yAntinode = by-(ay-by)
                xAntinode = bx-(ax-bx)
                if 0 <= yAntinode < len(node_map) and 0 <= xAntinode < len(bRow):
                    if not (yAntinode, xAntinode) in antinodes:
                        antinodes += [(yAntinode, xAntinode)]
                        if node_map[yAntinode][xAntinode] == ".":
                            node_map[yAntinode][xAntinode] = "#"
common.print_result(len(antinodes))
time.stop()

time.restart()
# Part 2
antinodes = []
for ay, aRow in enumerate(node_map):
    for ax, aColumn in enumerate(aRow):
        if aColumn in (".", "#"):
            continue
        for by, bRow in enumerate(node_map):
            for bx, bColumn in enumerate(bRow):
                if ay == by and ax == bx:
                    continue
                if aColumn != bColumn:
                    continue
                yAntinode = by
                xAntinode = bx
                if (by, bx) not in antinodes:
                    antinodes += [(by, bx)]
                while True:
                    yAntinode = yAntinode-(ay-by)
                    xAntinode = xAntinode-(ax-bx)
                    if 0 <= yAntinode < len(node_map) and 0 <= xAntinode < len(bRow):
                        if not (yAntinode, xAntinode) in antinodes:
                            antinodes += [(yAntinode, xAntinode)]
                            if node_map[yAntinode][xAntinode] == ".":
                                node_map[yAntinode][xAntinode] = "#"
                    else:
                        break
common.print_result(len(antinodes))
time.stop()