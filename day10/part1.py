import sys
from itertools import combinations


def determine_min_presses(lights: list[bool], buttons: list[list[bool]]) -> int:
    min_presses = sys.maxsize
    for r in range(1, len(buttons) + 1):
        for p in combinations(buttons, r=r):
            l = [False] * len(lights)
            presses = 0
            for button in p:
                for i in range(len(button)):
                    if button[i]:
                        l[i] = not l[i]
                presses += 1
                if presses >= min_presses:
                    break
            if presses >= min_presses:
                break
            if l == lights:
                min_presses = min(min_presses, presses)
    return min_presses


def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            buttons: list[list[bool]] = []
            lights: list[bool] = []
            parts = line.split()
            for i, part in enumerate(parts):
                if i == 0:
                    lights = [c == '#' for c in part[1:-1]]
                elif part.startswith('('):
                    button = [False] * len(lights)
                    for wire in [int(b) for b in part[1:-1].split(',')]:
                        button[wire] = True
                    buttons.append(button)
                else:
                    break
            answer += determine_min_presses(lights, buttons)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
