## Problem 29
# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

# 22=4, 23=8, 24=16, 25=32
# 32=9, 33=27, 34=81, 35=243
# 42=16, 43=64, 44=256, 45=1024
# 52=25, 53=125, 54=625, 55=3125
# If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

# 4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

import time
import sys
sys.path.append("../..")
from utils.log import MarkdownLogger

def run():
    maximum = 100

    for a in range(2, maximum + 1):
        for b in range(2, maximum + 1):
            try:
                terms.add(a**b)
            except NameError:
                terms = {a**b}
    
    result = len(terms)
    print(f"result: {result}")
    return result

                       
if __name__ == "__main__":
    logger = MarkdownLogger(last_problem=723)
    problem_id = int(sys.argv[0].split("m")[1].split(".")[0])
    startTime = time.time()
    solution = run()
    duration = round(time.time() - startTime, 5)
    logger.add_problem(solution, problem_id=problem_id, duration=duration, language="Python")
    print(f"\nThe script took {round(duration, 2)} seconds.")