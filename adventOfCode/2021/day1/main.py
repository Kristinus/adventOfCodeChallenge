import sys 

def part1(arr):
    increase_count = 0
    prev_depth = None
    for depth in arr:
        if prev_depth and depth > prev_depth:
            increase_count += 1
        prev_depth = depth
    return increase_count


def part2(arr):
    increase_count = 0
    w_len = 3
    for i in range(w_len, len(arr)):
        if arr[i] > arr[i - w_len]:
            increase_count += 1
    return increase_count


if __name__ == "__main__":
    f = open(sys.argv[1], "r")

    input = f.readlines()
    arr = list(map(lambda x: int(x), input))

    print(part1(arr))
    print(part2(arr))
