import z3


def determine_min_presses(buttons: list[list[int]], joltages: list[int]) -> int:
    optimize = z3.Optimize()
    variables = z3.Ints(f'n{i}' for i in range(len(buttons)))
    for variable in variables:
        optimize.add(variable >= 0)
    for i, joltage in enumerate(joltages):
        equation = 0
        for b, button in enumerate(buttons):
            if i in button:
                equation += variables[b]
        optimize.add(equation == joltage)
    optimize.minimize(sum(variables))
    optimize.check()
    return optimize.model().eval(sum(variables)).as_long()


def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            buttons: list[list[int]] = []
            joltages: list[int] = []
            parts = line.split()
            for i, part in enumerate(parts):
                if i == 0:
                    continue
                elif part.startswith('('):
                    buttons.append([int(p) for p in part[1:-1].split(',')])
                else:
                    joltages = [int(j) for j in part[1:-1].split(',')]
            answer += determine_min_presses(buttons, joltages)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
