from utils import *


def parse(text: str) -> dict:
    text = text.replace('\n', '').strip().split(' ')
    ret = {}
    for field in text:
        if not field:
            continue
        k, v = field.split(':')
        ret[k] = v
    return ret


def parse_fields(data):
    line: str
    pp = []
    text = ''
    for line in data:
        line = line.strip(' \n')
        if not line:
            if text:
                pp.append(parse(text))
                text = ''
            continue
        text += line + ' '
    pp.append(parse(text))
    return pp


def is_valid_part1(di: dict) -> bool:
    return all(f in di for f in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})


def is_valid_part2(di: dict) -> bool:
    try:
        return (
            1920 <= int(di['byr']) <= 2002 and
            2010 <= int(di['iyr']) <= 2020 and
            2020 <= int(di['eyr']) <= 2030 and
            ((di['hgt'].endswith('cm') and 150 <= int(di['hgt'][:-2]) <= 193) or (di['hgt'].endswith('in') and 59 <= int(di['hgt'][:-2]) <= 76)) and
            di['hcl'].startswith('#') and all(x in '0123456789abcdef' for x in di['hcl'][1:].lower()) and
            int(di['pid']) and len(di['pid']) == 9 and
            di['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        )
    except:
        return False


if __name__ == '__main__':
    data = read_input('input.txt', fn=None, by_line=True)
    data = parse_fields(data)
    print(data)
    print(sum(is_valid_part1(x) for x in data))
    print(sum(is_valid_part2(x) for x in data))
