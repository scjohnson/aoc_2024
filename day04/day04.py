import numpy as np
from itertools import product

dirs = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def main():
    array = np.genfromtxt("input.txt", dtype=str, delimiter=1)

    vector = np.array(["X", "M", "A", "S"])
    nums = 0
    for x, y in np.ndindex(array.shape):
        for dir in dirs:
            index = 0
            i, j = x, y
            while (
                index < 4
                and 0 <= i < array.shape[0]
                and 0 <= j < array.shape[1]
                and array[i, j] == vector[index]
            ):
                if index == 3:
                    nums += 1
                i += dir[0]
                j += dir[1]
                index += 1
    print(nums)

    nums = 0
    for x, y in product(range(1, array.shape[0] - 1), range(1, array.shape[1] - 1)):
        if array[x, y] == "A":
            check = False
            corners = [
                array[x - 1, y - 1],
                array[x - 1, y + 1],
                array[x + 1, y + 1],
                array[x + 1, y - 1],
            ]
            if (corners[0] == corners[1] and corners[2] == corners[3]) or (
                corners[1] == corners[2] and corners[3] == corners[0]
            ):
                if sorted(set(corners)) == ["M", "S"]:
                    check == True
                    nums += 1
    print(nums)


if __name__ == "__main__":
    main()
