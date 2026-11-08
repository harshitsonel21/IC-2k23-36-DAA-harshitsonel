"""Searching algorithms for DAA."""

def linear_search(a, target):
    for index, value in enumerate(a):
        if value == target:
            return index
    return -1


def iterative_binary_search(a, target):
    low, high = 0, len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        if target < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def read_numbers():
    return [int(x) for x in input("Enter integers separated by spaces: ").split()]


def main():
    while True:
        print("\\n--- Searching Algorithms ---")
        print("1. Linear Search")
        print("2. Iterative Binary Search")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            break
        if choice not in ("1", "2"):
            print("Invalid choice. Try again.")
            continue
        values = read_numbers()
        target = int(input("Enter value to search: "))
        if choice == "1":
            result = linear_search(values, target)
        else:
            values.sort()
            print("Sorted list:", values)
            result = iterative_binary_search(values, target)
        print("Found at index:", result if result != -1 else "Not found")


if __name__ == "__main__":
    main()
