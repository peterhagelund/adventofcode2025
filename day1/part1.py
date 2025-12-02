def main():
    answer = 0
    dial = 50
    with open('puzzle_input.txt') as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            if direction == 'R':
                dial += distance
                while dial > 99:
                    dial -= 100
            else:
                dial -= distance
                while dial < 0:
                    dial += 100
            if dial == 0:
                answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
