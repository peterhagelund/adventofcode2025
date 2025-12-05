def overlap(r1: range, r2: range) -> bool:
    if r1.start in r2 or r1.stop in r2 or r2.start in r1 or r2.stop in r1:
        return True
    return False


def merge(ranges: set[range]):
    while True:
        merge_happened = False
        for r1 in ranges:
            for r2 in ranges:
                if r1 == r2:
                    continue
                if overlap(r1, r2):
                    r3 = range(min(r1.start, r2.start), max(r1.stop, r2.stop))
                    ranges.remove(r1)
                    ranges.remove(r2)
                    ranges.add(r3)
                    merge_happened = True
                    break
            if merge_happened:
                break
        if not merge_happened:
            break


def main():
    ranges: set[range] = set()
    with open('puzzle_input.txt') as f:
        for line in f:
            line = line.strip()
            if line == '':
                break
            parts = line.split('-')
            ranges.add(range(int(parts[0]), int(parts[1]) + 1))
    merge(ranges)
    print(sum([len(r) for r in ranges]))


if __name__ == '__main__':
    main()
