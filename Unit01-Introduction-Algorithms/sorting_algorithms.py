"""Elementary sorting algorithms for DAA.
All methods sort in ascending order and return a new list.
"""

def bubble_sort(a):
    a = a.copy()
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def recursive_bubble_sort(a, n=None):
    a = a.copy() if n is None else a
    if n is None:
        n = len(a)
    if n <= 1:
        return a
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return recursive_bubble_sort(a, n - 1)


def selection_sort(a):
    a = a.copy()
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


def insertion_sort(a):
    a = a.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def recursive_insertion_sort(a, n=None):
    a = a.copy() if n is None else a
    if n is None:
        n = len(a)
    if n <= 1:
        return a
    recursive_insertion_sort(a, n - 1)
    key = a[n - 1]
    j = n - 2
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
    return a


def read_numbers():
    return [int(x) for x in input("Enter integers separated by spaces: ").split()]


def main():
    methods = {
        "1": ("Bubble Sort", bubble_sort),
        "2": ("Recursive Bubble Sort", recursive_bubble_sort),
        "3": ("Selection Sort", selection_sort),
        "4": ("Insertion Sort", insertion_sort),
        "5": ("Recursive Insertion Sort", recursive_insertion_sort),
    }
    while True:
        print("\\n--- Sorting Algorithms ---")
        for key, (name, _) in methods.items():
            print(f"{key}. {name}")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "0":
            break
        if choice not in methods:
            print("Invalid choice. Try again.")
            continue
        values = read_numbers()
        name, function = methods[choice]
        print(name, "->", function(values))


if __name__ == "__main__":
    main()
