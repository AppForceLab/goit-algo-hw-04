import timeit
import random
import matplotlib.pyplot as plt
import pandas as pd

# Implementing sorting algorithms
def insertion_sort(arr):
    """Sorts an array using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Sorts an array using merge sort."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Generating test cases
sizes = [100, 500, 1000, 5000, 10000, 50000]
data = {size: [random.randint(0, 100000) for _ in range(size)] for size in sizes}

# Running benchmarks with a cutoff for insertion sort
results = []
for size, arr in data.items():
    arr_copy = arr[:]

    time_insert = None
    if size <= 1000:  # Limit insertion sort to smaller sizes
        time_insert = timeit.timeit(lambda: insertion_sort(arr_copy[:]), number=1)

    time_merge = timeit.timeit(lambda: merge_sort(arr_copy[:]), number=1)
    time_timsort = timeit.timeit(lambda: sorted(arr_copy[:]), number=1)

    results.append([size, time_insert, time_merge, time_timsort])

# Converting results to a DataFrame
df = pd.DataFrame(results, columns=["Size", "Insertion Sort", "Merge Sort", "Timsort"])

# Plotting results (excluding None values)
plt.figure(figsize=(10, 6))
if df["Insertion Sort"].notna().any():
    plt.plot(df["Size"][df["Insertion Sort"].notna()], df["Insertion Sort"].dropna(), label="Insertion Sort", marker="o")
plt.plot(df["Size"], df["Merge Sort"], label="Merge Sort", marker="s")
plt.plot(df["Size"], df["Timsort"], label="Timsort", marker="^")
plt.xlabel("Array Size")
plt.ylabel("Execution Time (s)")
plt.title("Sorting Algorithm Performance Comparison")
plt.legend()
plt.grid(True)
plt.show()
