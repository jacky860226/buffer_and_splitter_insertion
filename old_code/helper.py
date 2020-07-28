def fragment_split(line: str):
    pair = {'(': ')', '[': ']'}
    level = {'(': 0, '[': 0}
    temp = line.split()
    accumulated = ''
    result = list()
    for frac in temp:
        accumulated = accumulated + frac
        for ltr in frac:
            for k in pair.keys():
                if ltr == k:
                    level[k] = level[k] + 1
                if ltr == pair[k]:
                    if level[k] > 0:
                        level[k] = level[k] - 1
        if sum(level.values()) == 0:
            result.append(accumulated)
            accumulated = ''
            continue
    return result


def get_between(line: str, start: str, end: str = None):
    if end is None:
        return line[line.find(start) + len(start):]
    return line[line.find(start) + len(start): line.rfind(end)]


