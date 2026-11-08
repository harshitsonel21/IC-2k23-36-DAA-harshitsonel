"""
DAA Algorithm Performance Analyzer
----------------------------------
Measures sorting/searching execution times for best-, average-, and
worst-case style test patterns.

Creates:
  results/performance_results.csv
  results/graphs/*.png (if matplotlib is installed)

Run this file from the repository root in Python IDLE (F5) or terminal.
"""

import csv
import importlib.util
import os
import random
import time

ROOT = os.path.dirname(os.path.abspath(__file__))


def load_module(module_name, relative_path):
    path = os.path.join(ROOT, relative_path)
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


sorting = load_module(
    "sorting_algorithms",
    os.path.join("Unit01-Introduction-Algorithms", "sorting_algorithms.py")
)
divide = load_module(
    "divide_conquer",
    os.path.join("Unit02-Divide-and-Conquer", "divide_conquer.py")
)
searching = load_module(
    "searching_algorithms",
    os.path.join("Unit05-Traversal-and-Search", "searching_algorithms.py")
)

SORTS = {
    "Bubble Sort": (sorting.bubble_sort, "Best O(n), Average O(n^2), Worst O(n^2)"),
    "Recursive Bubble Sort": (sorting.recursive_bubble_sort, "Best/Average/Worst O(n^2)"),
    "Selection Sort": (sorting.selection_sort, "Best/Average/Worst O(n^2)"),
    "Insertion Sort": (sorting.insertion_sort, "Best O(n), Average O(n^2), Worst O(n^2)"),
    "Recursive Insertion Sort": (sorting.recursive_insertion_sort, "Best O(n), Average O(n^2), Worst O(n^2)"),
    "Merge Sort": (divide.merge_sort, "Best/Average/Worst O(n log n)"),
    "Quick Sort": (divide.quick_sort, "Best/Average O(n log n), Worst O(n^2)"),
}

SEARCHES = {
    "Linear Search": (searching.linear_search, "Best O(1), Average/Worst O(n)"),
    "Iterative Binary Search": (searching.iterative_binary_search, "Best O(1), Average/Worst O(log n)"),
    "Recursive Binary Search": (divide.recursive_binary_search, "Best O(1), Average/Worst O(log n)"),
}


def make_data(size, case, rng):
    if case == "best":
        return list(range(size))
    if case == "worst":
        return list(range(size, 0, -1))
    values = list(range(size))
    rng.shuffle(values)
    return values


def timed_call(function, *args, repeats=3):
    """Return median elapsed seconds; input creation is outside timed region."""
    samples = []
    for _ in range(repeats):
        start = time.perf_counter()
        function(*args)
        samples.append(time.perf_counter() - start)
    return sorted(samples)[len(samples) // 2]


def run_experiments():
    rng = random.Random(2026)
    sizes = [100, 250, 500, 800]  # capped to stay below Python recursion depth for recursive sorts
    cases = ["best", "average", "worst"]
    rows = []

    # Sorting: each case is an input order; function returns a sorted copy.
    for algorithm_name, (function, theory) in SORTS.items():
        for case in cases:
            for size in sizes:
                data = make_data(size, case, rng)
                elapsed = timed_call(function, data)
                rows.append({
                    "category": "sorting",
                    "algorithm": algorithm_name,
                    "case": case,
                    "input_size": size,
                    "time_seconds": f"{elapsed:.10f}",
                    "theoretical_complexity": theory,
                })
                print(f"{algorithm_name:26} {case:7} n={size:4} {elapsed:.8f}s")

    # Search: sorted data for binary search; target placement is chosen to
    # represent a best hit, middle hit, or worst/absent target.
    search_sizes = [1000, 5000, 10000, 20000, 50000]
    for algorithm_name, (function, theory) in SEARCHES.items():
        for case in cases:
            for size in search_sizes:
                data = list(range(size))
                if case == "best":
                    target = data[0]
                elif case == "average":
                    target = data[size // 2]
                else:
                    target = -1  # absent target forces a full scan / full binary search
                elapsed = timed_call(function, data, target)
                rows.append({
                    "category": "searching",
                    "algorithm": algorithm_name,
                    "case": case,
                    "input_size": size,
                    "time_seconds": f"{elapsed:.10f}",
                    "theoretical_complexity": theory,
                })
                print(f"{algorithm_name:26} {case:7} n={size:5} {elapsed:.8f}s")

    results_dir = os.path.join(ROOT, "results")
    os.makedirs(results_dir, exist_ok=True)
    csv_path = os.path.join(results_dir, "performance_results.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "category", "algorithm", "case", "input_size",
                "time_seconds", "theoretical_complexity"
            ]
        )
        writer.writeheader()
        writer.writerows(rows)
    print("\\nCSV results saved to:", csv_path)
    return rows, results_dir


def create_graphs(rows, results_dir):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Matplotlib is not installed. CSV was saved; install with:")
        print("  py -m pip install matplotlib")
        return

    graph_dir = os.path.join(results_dir, "graphs")
    os.makedirs(graph_dir, exist_ok=True)

    # One graph per algorithm, with best/average/worst series.
    algorithms = sorted({row["algorithm"] for row in rows})
    for algorithm in algorithms:
        subset = [row for row in rows if row["algorithm"] == algorithm]
        plt.figure()
        for case in ("best", "average", "worst"):
            points = sorted(
                (int(row["input_size"]), float(row["time_seconds"]))
                for row in subset if row["case"] == case
            )
            if points:
                x_values, y_values = zip(*points)
                plt.plot(x_values, y_values, marker="o", label=case.title())
        plt.title(algorithm + " – Experimental Performance")
        plt.xlabel("Input size (n)")
        plt.ylabel("Median execution time (seconds)")
        plt.legend()
        plt.grid(True)
        safe_name = "".join(
            character.lower() if character.isalnum() else "_"
            for character in algorithm
        ).strip("_")
        output_path = os.path.join(graph_dir, safe_name + ".png")
        plt.savefig(output_path, dpi=150, bbox_inches="tight")
        plt.close()
    print("Performance graphs saved in:", graph_dir)


if __name__ == "__main__":
    experiment_rows, output_directory = run_experiments()
    create_graphs(experiment_rows, output_directory)
