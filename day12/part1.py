def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        part_counts: list[int] = []
        part_count = 0
        for line in f:
            line = line.strip()
            if line == '':
                if part_count > 0:
                    part_counts.append(part_count)
                    part_count = 0
            elif line.endswith(':'):
                pass
            elif '#' in line:
                part_count += sum([1 if c == '#' else 0 for c in line])
            else:
                size, _counts = line.split(':')
                width, length = [int(p) for p in size.split('x')]
                area = width * length
                counts = [int(c) for c in _counts.strip().split(' ')]
                needed = 0
                for i in range(len(counts)):
                    needed += counts[i] * part_counts[i]
                if needed <= area:
                    answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
