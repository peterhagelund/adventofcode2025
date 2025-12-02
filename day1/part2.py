def main():
    answer = 0
    dial = 50
    with open("puzzle_input.txt") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            for _ in range(distance):
                dial = dial + 1 if direction == 'R' else dial - 1
                if dial == -1:
                    dial = 99
                elif dial == 100:
                    dial = 0
                if dial == 0:
                    answer += 1
    print(f"answer = {answer}")


if __name__ == "__main__":
    main()
