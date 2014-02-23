def process_data(filename):
    data = {}
    f = open(filename)
    for line in f:
        line = line.strip()
        attributes = line.split("::")
        data[attributes[0]] = attributes[1:]
    return data


def compile_data(filename):
    users = process_data('users.dat')
    movies = process_data('movies.dat')
    data = []
    f = open(filename)
    for line in f:
        line = line.strip()
        datum = line.split('::')
        user_attrs = users[datum[0]]
        movie_attrs = movies[datum[1]]
        data.append(user_attrs + movie_attrs + datum[3:] + datum[:3])
    return data

data = compile_data('data.dat')
