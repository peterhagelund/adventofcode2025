def main():
    tiles: list[tuple[int, int]] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            x, y = [int(p) for p in line.split(',')]
            tiles.append((x, y))
    answer = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = abs(1 + tiles[i][0] - tiles[j][0]) * abs(1 + tiles[i][1] - tiles[j][1])
            answer = max(answer, area)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
