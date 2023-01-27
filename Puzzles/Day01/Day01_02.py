from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""


def get_top_three_sum(s):
    return sum(sorted([sum([int(c) for c in e.split("\n") if len(c) > 0]) for e in s.split("\n\n")])[-3:])


if __name__ == "__main__":
    test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
    expected_output = "45000"

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, get_top_three_sum(test_input))

    answer_checker.generate_puzzle_output(__file__, get_top_three_sum)
