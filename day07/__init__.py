from utils import read_input


def contains_gold(name: str, bags):
    if 'shiny gold' in bags[name]:
        return True
    return any(contains_gold(n, bags) for n in bags[name])


def num_bags(name: str, bags):
    return 1 + sum(x[0] * num_bags(x[1], bags) for x in bags[name])


def part1(data):
    bags = dict()
    for line in data:
        name = ' '.join(line[:2])
        bags[name] = []
        i = 5
        while i < len(line):
            if ' '.join(line[i:i+2]) == 'other bags.':
                i += 4
                continue
            bags[name].append(' '.join(line[i:i+2]))
            i += 4
    return sum(contains_gold(n, bags) for n in bags)


def part2(data):
    bags = dict()
    for line in data:
        name = ' '.join(line[:2])
        bags[name] = []
        i = 4
        while i < len(line):
            if ' '.join(line[i+1:i+3]) == 'other bags.':
                i += 4
                continue
            bags[name].append((int(line[i]), ' '.join(line[i+1:i+3])))
            i += 4
    return num_bags('shiny gold', bags) - 1


if __name__ == '__main__':
    data = read_input('input.txt', by_line=True, fn=lambda x: x.strip(' \n').split(' '))
    print(part1(data))
    print(part2(data))
