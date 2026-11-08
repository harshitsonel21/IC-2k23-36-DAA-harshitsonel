# Experimental Results

- `performance_results.csv` contains measured execution times for sorting and searching algorithms across input patterns.
- `graphs/` contains one PNG performance graph per algorithm.
- `sample_outputs.txt` contains example console outputs from the implemented algorithms.

Run `python performance_analyzer.py` from the repository root to regenerate the CSV and graphs. Timings vary by machine. Recursive sorting experiments use input sizes up to 800 to stay within the usual Python recursion limit.
