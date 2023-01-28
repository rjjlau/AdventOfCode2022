from Util.AnswerChecker import AnswerChecker

"""
Question
"""


def answer(s):
    return s


if __name__ == "__main__":
    test_input = """"""
    expected_output = ""

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
