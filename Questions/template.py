from Util.AnswerChecker import AnswerChecker

"""
Question
"""

if __name__ == "__main__":
    test_input = ""
    expected_output = ""

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, (test_input))  # TODO - add answer function

    puzzle_input = answer_checker.get_puzzle_input(__file__.split("Questions")[1])
    puzzle_output = (puzzle_input)  # TODO - add answer function
