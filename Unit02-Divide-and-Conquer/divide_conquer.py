"""Divide-and-conquer algorithms for DAA."""

def recursive_binary_search(a, target, low=0, high=None):
    if high is None:
        high = len(a) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if a[mid] == target:
        return mid
    if target < a[mid]:
        return recursive_binary_search(a, target, low, mid - 1)
    return recursive_binary_search(a, target, mid + 1, high)


def merge_sort(a):
    if len(a) <= 1:
        return a.copy()
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(a):
    if len(a) <= 1:
        return a.copy()
    pivot = a[len(a) // 2]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def read_numbers():
    return [int(x) for x in input("Enter integers separated by spaces: ").split()]


def main():
    while True:
        print("\\n--- Divide and Conquer ---")
        print("1. Recursive Binary Search")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            break
        if choice == "1":
            values = read_numbers()
            values.sort()
            target = int(input("Enter value to search: "))
            print("Sorted list:", values)
            result = recursive_binary_search(values, target)
            print("Found at index:", result if result != -1 else "Not found")
        elif choice in ("2", "3"):
            values = read_numbers()
            function = merge_sort if choice == "2" else quick_sort
            print("Sorted list:", function(values))
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
