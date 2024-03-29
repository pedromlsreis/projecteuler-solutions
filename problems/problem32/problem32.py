## Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import math
import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger
import tqdm


def run():
    n = 9
    products = set()
    min_number = 1
    max_number = math.ceil(math.sqrt(int(n * "9")))

    for a in tqdm.tqdm(range(min_number, max_number + 1)):
        for b in range(min_number, max_number + 1):
            prod = a * b
            all_digits = str(a) + str(b) + str(prod)
            if len(all_digits) == n:
                if sorted(all_digits) == [f"{i}" for i in range(1, n + 1)]:
                    products.add(prod)

    results = sum(products)
    print(f"result: {results}")
    return results


if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(
        solution, problem_id=problem_id, duration=duration, language="Python"
    )
    print(f"\nThe script took {round(duration, 2)} seconds.")
