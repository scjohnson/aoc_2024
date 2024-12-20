from tqdm import tqdm
import itertools


def check(nums, ops, total):
    for combs in itertools.product(ops, repeat=len(nums) - 1):
        to_eval = nums[0]
        for i in range(len(combs)):
            if combs[i] == "||":
                to_eval = to_eval + nums[i + 1]
            else:
                to_eval = to_eval + combs[i]
                to_eval = to_eval + nums[i + 1]
                to_eval = str(eval(to_eval))
        if eval(to_eval) == int(total):
            return True
    return False


def main():
    with open("input.txt", "r") as file:
        lines = file.read().splitlines()

    for ops in [["*", "+"], ["*", "+", "||"]]:
        score = 0
        for line in tqdm(lines):
            total, nums = line.split(": ")
            nums = nums.split(" ")
            if check(nums, ops, total):
                score += int(total)
        print(score)


if __name__ == "__main__":
    main()
