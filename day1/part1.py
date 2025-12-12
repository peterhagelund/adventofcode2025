def main():
    answer = 0
    dial = 50
    with open('puzzle_input.txt') as f:
        for line in f:
            line = line.strip().replace('R', '+').replace('L', '-')
            dial = (dial + int(line)) % 100
            answer += 1 if dial == 0 else 0
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
