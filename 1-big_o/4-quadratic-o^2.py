def get_all_pairs(arr: list):

    for i in range(len(arr)):  # o(n)
        for j in range(len(arr)):  # o(n) * o(n)
            yield (i, j)


for pair in get_all_pairs([i for i in range(10)]):
    print(pair)

# results => n * n => O(n *2)


def get_all_pairs2(arr1: list, arr2: list):

    for i in range(len(arr1)):  # o(a)
        for j in range(len(arr2)):  # o(a) * o(b)
            yield (i, j)


# results => a * b => O(a * b)


# remove Drop None Dominant


def get_all_pairs2(arr: list):
    for i in range(len(arr)):  # o(n)
        print(i)
    for i in range(len(arr)):  # o(n)
        for j in range(len(arr)):  # o(n) * o(n)
            yield (i, j)


# results => n + n * n => O(n + n*n) => O(N*2)


def get_all_pairs3(arr: list):
    for i in range(len(arr)):  # o(n)
        for j in range(len(arr)):  # o(n) * o(n)
            yield (i, j)

    for i in range(len(arr)):  # o(n)
        for j in range(len(arr)):  # o(n) * o(n)
            yield (i, j)


# results => n*n + n * n => O(2n*n) => O(N^2)


def get_all_pairs4(arr: list, arr2: list):
    for i in range(len(arr2)):  # o(a)
        for j in range(len(arr2)):  # o(a) * o(a)
            yield (i, j)

    for i in range(len(arr)):  # o(b)
        for j in range(len(arr)):  # o(b) * o(b)
            yield (i, j)


# results => a*a + b *b => O(a) => O(a^2 + b^2)
