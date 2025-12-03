def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            levels = sorted(bank[:-1], reverse=True)
            v1 = levels[0]
            i1 = bank.index(v1)
            joltage = str(v1)
            bank = bank[i1 + 1 :]
            levels = sorted(bank, reverse=True)
            v2 = levels[0]
            joltage += str(v2)
            answer += int(joltage)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
