from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""


def answer(s):
    # going to favour speed of response over clever one-liners, will come back and try to make it one line in the future
    pairs = [i.split(",") for i in s.split("\n") ]
    i = 0
    for pair in pairs:
        first_min = int(pair[0].split("-")[0])
        first_max = int(pair[0].split("-")[1])
        second_min = int(pair[1].split("-")[0])
        second_max = int(pair[1].split("-")[1])

        if (first_max >= second_max >= first_min) or (second_max >= first_max >= second_min):
            i += 1

    return i


if __name__ == "__main__":
    test_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    expected_output = """4"""
    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)
