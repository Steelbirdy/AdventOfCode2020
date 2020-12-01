from utils import readlines


def part1(expenses):
    nums = set(expenses)
    for n in expenses:
        if (2020 - n) in nums:
            return n * (2020 - n)


def part2(expenses):
    nums = set(expenses)
    for i, m in enumerate(expenses):
        for j, n in enumerate(expenses[i+1:]):
            if m + n >= 2020:
                continue
            if (2020 - (m + n)) in nums:
                return m * n * (2020 - (m + n))


if __name__ == '__main__':
    expenses = readlines('input.txt', fn=int)
    solution1 = part1(expenses)
    solution2 = part2(expenses)

    print(f'Solution 1: {solution1}\nSolution 2: {solution2}')
