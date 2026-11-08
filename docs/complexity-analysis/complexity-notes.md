# Complexity Analysis Notes

| Algorithm | Best Time | Average Time | Worst Time | Auxiliary Space |
|---|---:|---:|---:|---:|
| Linear Search | O(1) | O(n) | O(n) | O(1) |
| Iterative Binary Search | O(1) | O(log n) | O(log n) | O(1) |
| Recursive Binary Search | O(1) | O(log n) | O(log n) | O(log n) |
| Bubble Sort (optimized) | O(n) | O(n²) | O(n²) | O(1) |
| Recursive Bubble Sort | O(n²)* | O(n²) | O(n²) | O(n) call stack |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Recursive Insertion Sort | O(n) | O(n²) | O(n²) | O(n) call stack |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort (pivot implementation may vary) | O(n log n) expected/best | O(n log n) expected | O(n²) | O(n) in this list-based implementation (plus recursion) |

*The provided recursive bubble sort does not include an early-exit optimization, so its best case is O(n²), not O(n). The analyzer's theoretical note should be interpreted accordingly.
