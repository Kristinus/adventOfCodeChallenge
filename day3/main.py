import sys

def part1(arr):
    half = int(len(arr)/2)
    bit_size = len(arr[0])
    bit_sum = [0] * bit_size
    for bin in arr:
        for i in range(0, len(bin)):
            bit_sum[i] += 1 if bin[i] == "1" else 0
    gamma = 0
    epsilon = 0
    for i in range(0, bit_size):
        if bit_sum[i] > half:
            gamma += 2**(bit_size-1-i)
        else:
            epsilon += 2**(bit_size-1-i)
    return gamma * epsilon

def part2(arr):
    bit_size = len(arr[0])
    bit_sum = [0] * bit_size
    common = arr
    uncommon = arr
    for i in range(0, bit_size):
        for bin in common:
            bit_sum[i] += 1 if bin[i] == "1" else -1
        common = [x for x in common if (bit_sum[i] >= 0 and x[i] == "1") or (bit_sum[i] < 0 and x[i] == "0")]
        if len(common) == 1:
            break
    o2 = int(common[0], 2)
    
    bit_sum = [0] * bit_size
    for i in range(0, bit_size):
        for bin in uncommon:
            bit_sum[i] += 1 if bin[i] == "1" else -1
        uncommon = [x for x in uncommon if (bit_sum[i] >= 0 and x[i] == "0") or (bit_sum[i] < 0 and x[i] == "1")]
        if len(uncommon) == 1:
            break
    co2 = int(uncommon[0], 2)
    return o2 * co2
if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        arr = f.read().splitlines()

        print(part1(arr))
        print(part2(arr))