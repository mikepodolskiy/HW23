def read_file(filepath):
    with open(filepath, mode='r', encoding='UTF-8') as file:
        return file.readlines()


def filter_data(data, val):
    return filter(lambda x: val in x, data)


def map_data(data, val):
    col = int(val)
    return map((lambda line: line.split(' ')[col]), data)


def sort_data(data, val):
    if val == 'asc':
        return sorted(data, reverse=False)
    if val == 'desc':
        return sorted(data, reverse=True)


def limit_data(data, val):
    limit = int(val)
    return list(data)[:limit]


def unique_data(data):
    return set(data)
