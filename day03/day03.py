import re
import bisect
import numpy as np


def do(index, dos, donts):

    d = bisect.bisect_left(dos, index) - 1
    dn = bisect.bisect_left(donts, index) - 1

    if dn < 0 or dos[d] > donts[dn]:
        return 1
    return 0


def main():

    with open("input.txt", "r") as file:
        lines = file.readlines()
    text = "".join(lines)

    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, text)

    mults = [int(int1) * int(int2) for int1, int2 in matches]
    print(sum(mults))

    dos = [match.start() for match in re.finditer(re.escape("do()"), text)]
    dos.insert(0, 0)
    donts = [match.start() for match in re.finditer(re.escape("don't()"), text)]
    matches = re.finditer(pattern, text)
    do_array = [do(m.start(), dos, donts) for m in matches]
    print(np.sum(np.array(do_array) * np.array(mults)))


if __name__ == "__main__":
    main()
