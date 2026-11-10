import random
import time

def count_pairs_naive(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count

def count_pairs_optimized(arr, target):
    seen = {}
    count = 0

    for x in arr:
        needed = target - x
        if needed in seen:
            count += seen[needed]

        if x in seen:
            seen[x] += 1
        else:
            seen[x] = 1

    return count


if __name__ == "__main__":
    random.seed(42)
    n = int(input("Enter N: "))
    arr = [random.randint(1, 20000) for _ in range(n)]
    target = 20000

    start = time.time()
    print("Naive:", count_pairs_naive(arr, target))
    print("Naive time:", time.time() - start)

    start = time.time()
    print("Optimized:", count_pairs_optimized(arr, target))
    print("Optimized time:", time.time() - start)
