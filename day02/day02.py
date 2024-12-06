import numpy as np


def is_safe(report):
    diffs = report[1:] - report[:-1]
    if 0 in diffs or np.max(np.abs(diffs)) > 3:
        return False
    if np.all(diffs < 0) or np.all(diffs > 0):
        return True
    return False


def is_safe_dampen(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(np.delete(report, i)):
            return True
    return False


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    results = [is_safe(np.array([int(r) for r in report.split()])) for report in lines]
    print(results.count(True))
    results = [
        is_safe_dampen(np.array([int(r) for r in report.split()])) for report in lines
    ]
    print(results.count(True))


if __name__ == "__main__":
    main()
