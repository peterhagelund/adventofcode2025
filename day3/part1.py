def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            bank = line.strip()
            levels = sorted([c for c in bank], reverse=True)
            v1 = levels[0]
            i1 = bank.index(v1)
            if i1 == len(bank) - 1:
                v1 = levels[1]
                i1 = bank.index(v1)
            bank = bank[i1 + 1 :]
            levels = sorted([c for c in bank], reverse=True)
            v2 = levels[0]
            joltage = int(v1) * 10 + int(v2)
            answer += joltage
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
