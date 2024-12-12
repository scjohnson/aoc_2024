def verify_update(update, checks):
    for check in checks:
        if check[0] in update and check[1] in update:
            if update.index(check[0]) > update.index(check[1]):
                return False
    return True


def fix(update, checks):
    while verify_update(update, checks) == False:
        for check in checks:
            if check[0] in update and check[1] in update:
                in0 = update.index(check[0])
                in1 = update.index(check[1])
                if in0 > in1:
                    update[in0], update[in1] = update[in1], update[in0]
    return update


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
    checks = []
    updates = []
    updates_section = False
    for line in lines:
        if line == "\n":
            updates_section = True
            continue
        if updates_section:
            updates.append([int(num) for num in line.split(",")])
        else:
            checks.append([int(num) for num in line.split("|")])

    values = []
    new_values = []
    for update in updates:
        if verify_update(update, checks):
            values.append(update[len(update) // 2])
        else:
            new_update = fix(update, checks)
            new_values.append(new_update[(len(new_update) // 2)])
    print(sum(values))
    print(sum(new_values))


if __name__ == "__main__":
    main()
