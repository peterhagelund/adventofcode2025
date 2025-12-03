def determine_max_joltage(bank: list[int]) -> int:
    joltage = ''
    for remainder in range(11, -1, -1):
        l = len(bank)
        available = bank[: l - remainder]
        levels = sorted(available, reverse=True)
        b = levels[0]
        joltage += str(b)
        i = bank.index(b)
        bank = bank[i + 1 :]
    return int(joltage)


def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            answer += determine_max_joltage(bank)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
