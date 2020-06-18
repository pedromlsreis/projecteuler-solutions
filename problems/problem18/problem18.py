# # Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


import time
from num2words import num2words


def run():
    solution = 0
    first_num = 1
    last_num = 1000

    for n in range(first_num, last_num+1):
        solution += len(num2words(n, lang="en_GB", to="cardinal").replace("-", "").replace(" ", ""))
    
    print("solution:", solution)

                       
if __name__ == "__main__":
    startTime = time.time()
    run()
    print(f"\nThe script took {round(time.time() - startTime, 2)} seconds.")