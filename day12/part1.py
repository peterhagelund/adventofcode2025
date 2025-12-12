def do_presents_fit(presents: list[list[str]], size: tuple[int, int], counts: list[int]) -> bool:
    parts = [0] * len(presents)
    for i in range(len(presents)):
        for row in presents[i]:
            parts[i] += sum([1 if p == '#' else 0 for p in row])
    area = size[0] * size[1]
    needed = 0
    for i in range(len(counts)):
        needed += counts[i] * parts[i]
    if needed > area:
        return False
    return True


def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        presents: list[list[str]] = []
        present: list[str] = []
        for line in f:
            line = line.strip()
            if line == '':
                if len(present) > 0:
                    presents.append(present)
                    present = []
            elif line.endswith(':'):
                _ = int(line[:-1])
            elif '#' in line:
                present.append(line)
            else:
                size, counts = line.split(':')
                width, length = [int(p) for p in size.split('x')]
                if do_presents_fit(presents, (width, length), [int(c) for c in counts.strip().split(' ')]):
                    answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
