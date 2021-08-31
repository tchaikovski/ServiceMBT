

xxx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

x = list(func_chunks_generators(xxx, 4))


print(x)