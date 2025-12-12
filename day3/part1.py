def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            i1 = bank.index(max(bank[:-1]))
            i2 = bank.index(max(bank[i1 + 1 :]))
            answer += bank[i1] * 10 + bank[i2]
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
