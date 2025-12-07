def main():
    manifold: list[list[str]] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            manifold.append([c for c in line.strip()])
    height = len(manifold)
    width = len(manifold[0])
    answer = 0
    for y in range(0, height):
        for x in range(width):
            match manifold[y][x]:
                case 'S':
                    manifold[y + 1][x] = '|'
                case '^':
                    if manifold[y - 1][x] == '|':
                        answer += 1
                        manifold[y][x - 1] = '|'
                        manifold[y][x + 1] = '|'
                case _:
                    if y > 0 and manifold[y - 1][x] == '|':
                        manifold[y][x] = '|'
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
