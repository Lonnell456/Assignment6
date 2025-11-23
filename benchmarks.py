"""
Assignment 6 – Part 1: Empirical Comparison Script

Times randomized_select vs deterministic_select on different
input sizes and distributions. Run this from the terminal and
paste the output (with screenshot) into your report.
"""

import random
import time

from selection_algorithms import randomized_select, deterministic_select


def run_benchmarks():
    sizes = [100, 1000, 5000]
    distributions = ["random", "sorted", "reversed"]
    trials = 20

    print("Empirical comparison of selection algorithms")
    for n in sizes:
        print(f"\n=== n = {n} ===")
        for dist in distributions:
            base = list(range(n))
            if dist == "random":
                random.shuffle(base)
            elif dist == "sorted":
                pass
            elif dist == "reversed":
                base.reverse()

            t_rand = 0.0
            t_det = 0.0

            for _ in range(trials):
                arr = list(base)  # copy so each algorithm sees same input
                k = random.randint(0, n - 1)

                start = time.perf_counter()
                randomized_select(arr, k)
                t_rand += time.perf_counter() - start

                arr = list(base)
                start = time.perf_counter()
                deterministic_select(arr, k)
                t_det += time.perf_counter() - start

            print(
                f"{dist:8s}  randomized: {t_rand / trials:.6f}s  "
                f"deterministic: {t_det / trials:.6f}s"
            )


if __name__ == "__main__":
    run_benchmarks()
