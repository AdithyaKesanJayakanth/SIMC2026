"""
main.py — Master runner for the SIMC 2024 Endeavour Challenge.
Executes all 7 tasks sequentially and generates all outputs.

Usage:
  python main.py                    # Run all tasks
  python main.py --task 1           # Run specific task
  python main.py --generate-data    # Generate synthetic test data only

Requirements: numpy, matplotlib. Optional: scikit-learn (for KMeans in Task 3).
"""

import numpy as np
import os
import sys
import time
import argparse

# Add source directory to path
sys.path.insert(0, os.path.dirname(__file__))

from task1 import solve_task1
from task2 import solve_task2
from task3 import solve_task3
from task4 import solve_task4
from task5 import solve_task5
from task6 import solve_task6
from task7 import solve_task7


def main():
    parser = argparse.ArgumentParser(description="SIMC 2024 Endeavour Challenge Solver")
    parser.add_argument('--task', type=int, choices=[1, 2, 3, 4, 5, 6, 7],
                        help='Run a specific task (1-7). Default: run all.')
    parser.add_argument('--generate-data', action='store_true',
                        help='Generate synthetic test data and exit.')
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "endeavor.npz")

    if args.generate_data:
        from generate_test_data import generate_all
        generate_all(data_path)
        return

    # Load data
    if not os.path.exists(data_path):
        print("=" * 60)
        print("  endeavor.npz not found!")
        print("  Place the competition data file in:")
        print(f"    {base_dir}/")
        print("  Or run: python main.py --generate-data")
        print("  to create synthetic test data.")
        print("=" * 60)
        print("\nGenerating synthetic test data for demonstration...\n")
        from generate_test_data import generate_all
        generate_all(data_path)

    loaded = np.load(data_path)

    print("\n" + "=" * 60)
    print("  SIMC 2024 Endeavour Challenge — Full Solution")
    print("  Team: India")
    print("=" * 60)
    print(f"\nData loaded from: {data_path}")
    print("Available keys:", list(loaded.keys()))
    for k in loaded.keys():
        print(f"  {k}: shape = {loaded[k].shape}")

    tasks_to_run = [args.task] if args.task else [1, 2, 3, 4, 5, 6, 7]
    results = {}

    for task_num in tasks_to_run:
        print(f"\n{'#' * 60}")
        print(f"# TASK {task_num}")
        print(f"{'#' * 60}")

        t0 = time.time()

        if task_num == 1:
            results[1] = solve_task1(loaded["task1"])

        elif task_num == 2:
            results[2] = solve_task2(loaded["task2"])

        elif task_num == 3:
            results[3] = solve_task3(loaded["task3"])

        elif task_num == 4:
            results[4] = solve_task4(loaded["task4"])

        elif task_num == 5:
            solve_task5()

        elif task_num == 6:
            results[6] = solve_task6(loaded["task6a"], loaded["task6b"])

        elif task_num == 7:
            results[7] = solve_task7(loaded["task7a"], loaded["task7b"])

        elapsed = time.time() - t0
        print(f"\n  Task {task_num} completed in {elapsed:.1f}s")

    print(f"\n{'=' * 60}")
    print("  All requested tasks complete!")
    print(f"  Outputs saved to: {os.path.join(base_dir, 'outputs')}/")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
