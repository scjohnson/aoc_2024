import numpy as np
from tqdm import tqdm


def length(array, count=True):
    location = np.where(array == "^")
    location = np.array([location[0][0], location[1][0]])
    direction = np.array([-1, 0])
    visited_states = set()
    if count:
        traversed = np.zeros(array.shape, dtype=np.int8)

    while (0 <= location[0] + direction[0] < array.shape[0]) and (
        0 <= location[1] + direction[1] < array.shape[1]
    ):
        next_pos = location + direction

        if array[next_pos[0], next_pos[1]] == "#":
            direction = np.array([[0, 1], [-1, 0]]) @ direction
        else:
            state = (tuple(location), tuple(direction))
            if state in visited_states:
                return -1, -1
            visited_states.add(state)

            location = next_pos
            if count:
                traversed[location[0], location[1]] = 1

    if count:
        return np.sum(traversed), traversed
    else:
        return 1, 1


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    array = np.array([list(line) for line in lines])

    l, traversed = length(array)
    print(f"Part One: {l}")

    possible_positions = [
        (i, j) for i, j in np.ndindex(array.shape) if traversed[i, j] == 1
    ]

    num_stuck = 0
    for i, j in tqdm(possible_positions, desc="Processing"):

        if array[i][j] == "^" or array[i][j] == "#":
            continue
        array[i][j] = "#"

        if length(array, False)[0] == -1:
            num_stuck += 1
        array[i][j] = "."

    print(f"Part Two: {num_stuck}")


if __name__ == "__main__":
    main()
