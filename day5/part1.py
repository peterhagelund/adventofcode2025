def main():
    ranges: list[range] = []
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            if '-' in line:
                parts = line.split('-')
                ranges.append(range(int(parts[0]), int(parts[1]) + 1))
            else:
                id = int(line)
                for r in ranges:
                    if id in r:
                        answer += 1
                        break
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
