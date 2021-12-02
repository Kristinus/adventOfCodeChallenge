import sys

def part1(arr):
    forward = 0
    depth = 0
    for i in arr:
        [command, amount] = i.split(" ")
        if command == "forward":
            forward += int(amount)
        elif command == "down":
            depth += int(amount)
        else:
            depth -= int(amount)
    return forward * depth


def part2(arr):
    forward = 0
    aim = 0
    depth = 0
    for i in arr:
        [command, amount] = i.split(" ")
        if command == "forward":
            forward += int(amount)
            depth += aim * int(amount)
        elif command == "down":
            aim += int(amount)
        else:
            aim -= int(amount)
    return forward * depth


if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    arr = f.readlines()

    print(part1(arr))
    print(part2(arr))
