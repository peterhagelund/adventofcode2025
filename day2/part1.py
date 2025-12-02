def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        for id_range in f.read().split(','):
            parts = id_range.split('-')
            first_id = int(parts[0])
            last_id = int(parts[1])
            for id in range(first_id, last_id + 1):
                s = str(id)
                l = len(s) // 2
                if s[:l] == s[l:]:
                    answer += id
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
