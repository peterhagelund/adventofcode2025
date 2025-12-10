from typing import NewType

import drawsvg as d

Tile = NewType('Tile', tuple[int, int])
Line = NewType('Line', tuple[Tile, Tile])
X = 0
Y = 1


def find_two_longest_lines(lines: list[Line]) -> tuple[Line, Line]:
    lines.sort(key=lambda l: abs(l[0][X] - l[1][X]), reverse=True)
    l1 = lines[0]
    l2 = lines[1]
    if l1[0][Y] > l1[1][Y]:
        upper_line = l1
        lower_line = l2
    else:
        upper_line = l2
        lower_line = l1
    if lower_line[0][X] > lower_line[1][X]:
        lower_line = Line((lower_line[1], lower_line[0]))
    if upper_line[0][X] > upper_line[1][X]:
        lower_line = Line((upper_line[1], upper_line[0]))
    return (lower_line, upper_line)


def create_lines(tiles: list[Tile]) -> list[Line]:
    lines: list[Line] = []
    for i in range(len(tiles)):
        j = i + 1
        if j == len(tiles):
            j = 0
        lines.append(Line((tiles[i], tiles[j])))
    return lines


def find_horizontal_line(lines: list[Line], x: int, min_y: int) -> Line | None:
    for line in lines:
        if line[0][Y] != line[1][Y]:
            continue
        if line[0][Y] <= min_y:
            continue
        if line[0][X] <= x <= line[1][X] or line[1][X] <= x <= line[0][X]:
            return line
    return None


def main():
    drawing = d.Drawing(1000, 1000)
    group = d.Group(transform='translate(0,1000) scale(0.01,-0.01)')
    group.append(d.Rectangle(0, 0, 100000, 100000, stroke='black', stroke_width=100, fill='none'))
    drawing.append(group)
    tiles: list[Tile] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            x, y = [int(p) for p in line.split(',')]
            tiles.append(Tile((x, y)))
    lines = create_lines(tiles)
    for line in lines:
        group.append(d.Line(line[0][X], line[0][Y], line[1][X], line[1][Y], stroke='blue', stroke_width=100))
    _, upper_line = find_two_longest_lines(lines)
    x = upper_line[1][X]
    min_y = upper_line[1][Y] + 1
    right_upper_line = find_horizontal_line(lines, x, min_y)
    assert right_upper_line is not None
    left_upper_lines: set[Line] = set()
    x = upper_line[0][X]
    while x < 50000:
        left_upper_line = find_horizontal_line(lines, x, min_y)
        assert left_upper_line is not None
        if left_upper_line[0][Y] <= right_upper_line[0][Y]:
            left_upper_lines.add(left_upper_line)
        x = max(left_upper_line[0][X], left_upper_line[1][X]) + 1
    candidates = sorted(left_upper_lines, key=lambda l: l[0][Y], reverse=True)
    left_upper_line = candidates[0]
    top_left = left_upper_line[1]
    bottom_right = upper_line[1]
    sx = top_left[X]
    sy = top_left[Y]
    ex = bottom_right[X]
    ey = sy
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    sx, sy = ex, ey
    ex = bottom_right[X]
    ey = bottom_right[Y]
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    sx, sy = ex, ey
    ex = top_left[X]
    ey = bottom_right[Y]
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    sx, sy = ex, ey
    ex = top_left[X]
    ey = top_left[Y]
    group.append(d.Line(sx, sy, ex, ey, stroke='red', stroke_width=100))
    answer = (bottom_right[X] - top_left[X] + 1) * (top_left[Y] - bottom_right[Y] + 1)
    print(f'answer = {answer}')
    drawing.save_svg('floor.svg')


if __name__ == '__main__':
    main()
