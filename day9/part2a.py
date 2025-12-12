from collections import deque
from typing import NewType

import drawsvg as d

Tile = NewType('Tile', tuple[int, int])
Line = NewType('Line', tuple[Tile, Tile])
Rectangle = NewType('Rectangle', tuple[Tile, Tile, int])

DELTAS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]
X = 0
Y = 1


def create_lines(tiles: list[Tile]) -> list[Line]:
    lines: list[Line] = []
    for i in range(len(tiles)):
        j = i + 1
        if j == len(tiles):
            j = 0
        lines.append(Line((tiles[i], tiles[j])))
    return lines


def create_compressed_floor(tiles: list[Tile], xs: list[int], ys: list[int]) -> list[list[int]]:
    # Even columns are for the x/y coordinates
    # Odd columns are for the space(s) in between
    floor = [[0] * (len(ys) * 2 - 1) for _ in range(len(xs) * 2 - 1)]  # Count * (1 for event + 1 for odd) - 1 because there is no space at the end
    lines = create_lines(tiles)
    for (x1, y1), (x2, y2) in lines:
        compressed_x1, compressed_x2 = sorted([xs.index(x1) * 2, xs.index(x2) * 2])  # Multiply by 2 to get the x coordinate columns
        compressed_y1, compressed_y2 = sorted([ys.index(y1) * 2, ys.index(y2) * 2])  # Multiply by 2 to get the y coordinate columns
        for x in range(compressed_x1, compressed_x2 + 1):
            for y in range(compressed_y1, compressed_y2 + 1):
                floor[x][y] = 1  # We don't care if a cell is red or green - just whether it's red/green or not - we have the tiles which are red
    # Run a flood-fill on the outside (easier)
    # Anything not in the outside, ipso facto, must be in the inside
    # Because the floor is compressed, there are tiles along the edges, so flood-fill must include a one-cell buffer around the floor
    outside = {(-1, -1)}
    queue = deque(outside)
    while len(queue) > 0:
        x, y = queue.popleft()
        for delta in DELTAS:
            _x = x + delta[X]
            _y = y + delta[Y]
            # Is it within the floor + buffer?
            if _x < -1 or _y < -1 or _x > len(floor) or _y > len(floor[0]):
                continue
            # Have we hit a colored tile?
            if 0 <= _x < len(floor) and 0 <= _y < len(floor[0]) and floor[_x][_y] == 1:
                continue
            # Have we been here before?
            if (_x, _y) in outside:
                continue
            # Part of the outside, then
            outside.add((_x, _y))
            # Go here next
            queue.append((_x, _y))
    # Fill in everything that is *not* outside
    for x in range(len(floor)):
        for y in range(len(floor[0])):
            if floor[x][y] == 1:
                continue
            if (x, y) not in outside:
                floor[x][y] = 1
    return floor


def is_valid(t1: Tile, t2: Tile, xs: list[int], ys: list[int], floor: list[list[int]]) -> bool:
    compressed_x1, compressed_x2 = sorted([xs.index(t1[X]) * 2, xs.index(t2[X]) * 2])
    compressed_y1, compressed_y2 = sorted([ys.index(t1[Y]) * 2, ys.index(t2[Y]) * 2])
    for x in range(compressed_x1, compressed_x2):
        for y in range(compressed_y1, compressed_y2):
            if floor[x][y] == 0:
                return False
    return True


def main():
    drawing = d.Drawing(1000, 1000)
    group = d.Group(transform='translate(0,1000) scale(0.01,-0.01)')
    group.append(d.Rectangle(0, 0, 100000, 100000, fill='none', stroke='black', stroke_width=100))
    tiles: list[Tile] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            x, y = [int(p) for p in line.split(',')]
            tiles.append(Tile((x, y)))
    lines = zip(tiles, tiles[1:] + tiles[:1])
    for line in lines:
        group.append(d.Line(line[0][X], line[0][Y], line[1][X], line[1][Y], stroke='blue', stroke_width=100))
    xs = sorted({x for x, _ in tiles})
    ys = sorted({y for _, y in tiles})
    floor = create_compressed_floor(tiles, xs, ys)
    rectangles: list[Rectangle] = []
    for i in range(len(tiles)):
        for j in range(i):
            t1 = tiles[i]
            t2 = tiles[j]
            if is_valid(t1, t2, xs, ys, floor):
                area = (abs(t1[X] - t2[X]) + 1) * (abs(t1[Y] - t2[Y]) + 1)
                rectangle = Rectangle((t1, t2, area))
                rectangles.append(rectangle)
    rectangles.sort(key=lambda r: r[2], reverse=True)
    rectangle = rectangles[0]
    sx = rectangle[0][X]
    sy = rectangle[0][Y]
    ex = rectangle[1][X]
    ey = sy
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    sx, sy = ex, ey
    ex = rectangle[1][X]
    ey = rectangle[1][Y]
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    sx, sy = ex, ey
    ex = rectangle[0][X]
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    sx, sy = ex, ey
    sx = rectangle[0][X]
    sy = rectangle[0][Y]
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    answer = rectangle[2]
    print(f'answer = {answer}')
    drawing.append(group)
    drawing.save_svg('floor.svg')


if __name__ == '__main__':
    main()
