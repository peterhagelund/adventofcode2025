DELTAS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def main():
    floor: list[str] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            floor.append(line.strip())
    height = len(floor)
    width = len(floor[0])
    answer = 0
    for y in range(height):
        for x in range(width):
            if floor[y][x] != '@':
                continue
            count = 0
            for delta in DELTAS:
                _y = y + delta[0]
                _x = x + delta[1]
                if 0 <= _y < height and 0 <= _x < width and floor[_y][_x] == '@':
                    count += 1
            if count < 4:
                answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
