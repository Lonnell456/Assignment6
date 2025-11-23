"""
Assignment 6 – Part 1: Selection Algorithms
Deterministic (Median-of-Medians) and Randomized Selection (Quickselect)

This file implements:
- randomized_select: expected O(n) time
- deterministic_select: worst-case O(n) time (median-of-medians)
and a small demo you can run from the terminal.
"""

import random


def _partition(arr, low, high, pivot_index):
    """Partition arr[low:high+1] around pivot; return final pivot index."""
    pivot = arr[pivot_index]
    # Move pivot to end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1
    # Move pivot to its final place
    arr[store], arr[high] = arr[high], arr[store]
    return store


def randomized_select(arr, k):
    """
    Randomized selection (Quickselect variant).
    Returns the k-th smallest element (0-based index).
    Expected time complexity: O(n).
    """
    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds")

    # Work on a copy so we don't modify the caller's array
    a = list(arr)
    low, high = 0, len(a) - 1

    while True:
        if low == high:
            return a[low]

        pivot_index = random.randint(low, high)
        pivot_index = _partition(a, low, high, pivot_index)

        if k == pivot_index:
            return a[k]
        elif k < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1


def _select_pivot_index(a, low, high):
    """
    Helper for deterministic_select.
    Uses the Median-of-Medians idea to choose a good pivot index.
    """
    n = high - low + 1
    if n <= 5:
        # For small groups, just sort and return the median index
        sub = sorted((a[i], i) for i in range(low, high + 1))
        return sub[n // 2][1]

    medians = []
    median_indices = []
    i = low

    # Group into chunks of 5, compute medians
    while i <= high:
        group = []
        idxs = []
        for j in range(i, min(i + 5, high + 1)):
            group.append(a[j])
            idxs.append(j)
        sorted_group = sorted(zip(group, idxs))
        median_val, median_idx = sorted_group[len(sorted_group) // 2]
        medians.append(median_val)
        median_indices.append(median_idx)
        i += 5

    # Recursively find the median of the medians
    mom_val = deterministic_select(medians, len(medians) // 2)

    # Map that value back to one of the original indices
    for idx in median_indices:
        if a[idx] == mom_val:
            return idx

    # Fallback (should almost never be used)
    return median_indices[0]


def deterministic_select(arr, k):
    """
    Deterministic selection using Median-of-Medians pivot selection.
    Returns the k-th smallest element (0-based index).

    Worst-case time complexity: O(n).
    """

    if k < 0 or k >= len(arr):
        raise IndexError("k is out of bounds")

    a = list(arr)

    def select(low, high, k_index):
        if low == high:
            return a[low]

        pivot_index = _select_pivot_index(a, low, high)
        pivot_index = _partition(a, low, high, pivot_index)

        if k_index == pivot_index:
            return a[k_index]
        elif k_index < pivot_index:
            return select(low, pivot_index - 1, k_index)
        else:
            return select(pivot_index + 1, high, k_index)

    return select(0, len(a) - 1, k)


def _self_test():
    """Sanity check: compare against Python's sorted array."""
    print("Running self-test for selection algorithms...")
    for n in range(1, 60):
        for _ in range(30):
            arr = [random.randint(-100, 100) for _ in range(n)]
            k = random.randint(0, n - 1)
            expected = sorted(arr)[k]

            r_val = randomized_select(arr, k)
            d_val = deterministic_select(arr, k)

            assert r_val == expected, "Randomized select mismatch"
            assert d_val == expected, "Deterministic select mismatch"
    print("All tests passed!")


if __name__ == "__main__":
    # Small demo for the terminal screenshot
    sample = [7, 2, 9, 4, 1, 5, 8, 3, 6]
    print("Sample array:", sample)
    for k in range(len(sample)):
        print(f"k = {k} (k-th smallest):")
        print("  randomized_select:", randomized_select(sample, k))
        print("  deterministic_select:", deterministic_select(sample, k))

    # Run the internal self-test
    _self_test()
