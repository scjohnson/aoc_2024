import numpy as np


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    left = []
    right = []

    for line in lines:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()
    print(np.sum(np.abs(np.array(left) - np.array(right))))

    score = 0
    for item in left:
        score += right.count(item) * item
    print(score)


if __name__ == "__main__":
    main()
