"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


def pattern(n: int) -> None:
    for _ in range(1, n + 1):
        for j in range(1, 6):
            print(j, end=" ")
        print()


pattern(10)

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(10)

"""
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
"""


def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


pattern(5)

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()


pattern(5)

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(5)

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()


pattern(5)

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


pattern(5)

"""
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


pattern(5)