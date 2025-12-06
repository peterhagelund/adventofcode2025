def main():
    problems: list[list[int]] = []
    operators: list[str] = []
    with open('puzzle_input.txt') as f:
        for line in f:
            line = line.strip()
            if line[0].isdigit():
                problems.append([int(v) for v in line.split()])
            else:
                operators = line.split()
    answer = 0
    for i in range(len(operators)):
        result = 0 if operators[i] == '+' else 1
        for row in problems:
            if operators[i] == '+':
                result += row[i]
            else:
                result *= row[i]
        answer += result
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
