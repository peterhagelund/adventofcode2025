def do_beam(location: tuple[int, int], height: int, splitters: set[tuple[int, int]], cache: dict[tuple[int, int], int]) -> int:
    if location in cache:
        return cache[location]
    if location[0] == height - 1:
        count = 1
    elif location in splitters:
        count = do_beam((location[0] + 1, location[1] - 1), height, splitters, cache) + do_beam((location[0] + 1, location[1] + 1), height, splitters, cache)
    else:
        count = do_beam((location[0] + 1, location[1]), height, splitters, cache)
    cache[location] = count
    return count


def main():
    splitters: set[tuple[int, int]] = set()
    height = 0
    start = 0
    with open('puzzle_input.txt') as f:
        y = 0
        for line in f:
            line = line.strip()
            for x in range(len(line)):
                if line[x] == 'S':
                    start = x
                    break
                if line[x] == '^':
                    splitters.add((y, x))
            y += 1
        height = y

    cache: dict[tuple[int, int], int] = {}
    answer = do_beam((0, start), height, splitters, cache)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
