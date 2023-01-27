from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""


def get_score_revised(g):
    return sum([{"X": 0, "Y": 3, "Z": 6}[r[1]] + ord({"X": {"A": "Z", "B": "X", "C": "Y"}, "Y": {"A": "X", "B": "Y", "C": "Z"}, "Z": {"A": "Y", "B": "Z", "C": "X"}}[r[1]][r[0]]) - 87 for r in [i.split(" ") for e in g.split("\n\n") for i in e.split("\n") if len(i) > 0]])


if __name__ == "__main__":
    test_input = """A Y
B X
C Z"""
    expected_output = """12"""

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, get_score_revised(test_input))

    answer_checker.generate_puzzle_output(__file__, get_score_revised)
