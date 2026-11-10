import random
import time

def kth_smallest_naive(arr, k):
    sums = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sums.append(arr[i] + arr[j])

    sums.sort()
    return sums[k - 1]

def count_pairs_leq(arr, value):
    count = 0
    j = len(arr) - 1

    for i in range(len(arr)):
        if j <= i:
            break

        while j > i and arr[i] + arr[j] > value:
            j -= 1

        if j <= i:
            break

        count += j - i

    return count

def kth_smallest_optimized(arr, k):
    arr.sort()

    low = arr[0] + arr[1]
    high = arr[-2] + arr[-1]

    while low < high:
        mid = (low + high) // 2

        if count_pairs_leq(arr, mid) >= k:
            high = mid
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    random.seed(42)
    n = int(input("Enter N: "))
    arr = [random.randint(1, 100000) for _ in range(n)]
    k = int(input("Enter K: "))

    start = time.time()
    print("Optimized answer:", kth_smallest_optimized(arr.copy(), k))
    print("Optimized time:", time.time() - start)

    # Naive is intentionally not run for large N because it stores O(N^2) sums.
