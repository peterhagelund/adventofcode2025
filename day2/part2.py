def is_invalid(id: int) -> bool:
    s = str(id)
    l = len(s)
    for size in range(1, l // 2 + 1):
        if l % size != 0:
            continue
        digits: set[str] = set()
        for i in range(0, len(s), size):
            digits.add(s[i : i + size])
        if len(digits) == 1:
            return True
    return False


def main():
    answer = 0
    with open('puzzle_input.txt') as f:
        ids = f.read()
        id_ranges = ids.split(',')
        for id_range in id_ranges:
            parts = id_range.split('-')
            first_id = int(parts[0])
            last_id = int(parts[1])
            for id in range(first_id, last_id + 1):
                if is_invalid(id):
                    answer += id
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
