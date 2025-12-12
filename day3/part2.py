def determine_max_joltage(bank: list[int]) -> int:
    joltage = 0
    for remainder in range(11, -1, -1):
        b = max(bank[: len(bank) - remainder])
        joltage = joltage * 10 + b
        i = bank.index(b)
        bank = bank[i + 1 :]
    return joltage


def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            answer += determine_max_joltage(bank)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
