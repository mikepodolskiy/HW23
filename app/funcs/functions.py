# reading file using generator
def read_file(filepath):
    with open(filepath, mode='r', encoding='UTF-8') as file:
        for line in file:
            yield line


# filtering data by value consistence
def filter_data(data, val):
    return filter(lambda x: val in x, data)


# output one col acc to col number
def map_data(data, val):
    col = int(val)
    return map((lambda line: line.split(' ')[col]), data)


# sorting data asc or desc form val argument
def sort_data(data, val):
    if val == 'asc':
        return sorted(data, reverse=False)
    if val == 'desc':
        return sorted(data, reverse=True)


# limiting data to show
def limit_data(data, val):
    limit = int(val)
    return list(data)[:limit]


# showing only unique data
def unique_data(data):
    return set(data)
