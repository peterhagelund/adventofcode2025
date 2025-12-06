def main():
    problems: list[str] = []
    operators: list[str] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            line = line.replace('\n', ' ')
            if '+' not in line:
                problems.append(line)
            else:
                operators = line.split()
    answer = 0
    start = 0
    for i in range(len(operators)):
        width = max([r[start:].index(' ') for r in problems])
        values = [r[start : start + width] for r in problems]
        start += width + 1
        result = 0 if operators[i] == '+' else 1
        for j in range(width):
            value = ''.join([v[j] for v in values])
            number = int(value)
            if operators[i] == '+':
                result += number
            else:
                result *= number
        answer += result
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
