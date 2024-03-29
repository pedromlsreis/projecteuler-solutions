# # Problem 14

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
import sys

sys.path.append("../..")
from utils.log import MarkdownLogger


def run():

    end_no = 1
    max_sequence = 0

    for i in range(1, 1000000):
        # print(i)
        sequence = [i]
        n = sequence[-1]

        while sequence[-1] != end_no:
            n = sequence[-1]

            if n % 2 == 0:
                sequence.append(int(n / 2))
            else:
                sequence.append(int((3 * n) + 1))

        if len(sequence) > max_sequence:
            max_sequence = len(sequence)
            answer = sequence[0]
            print(answer, max_sequence)

    print(answer)
    return answer


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
