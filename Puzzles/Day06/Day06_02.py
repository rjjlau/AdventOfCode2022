from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
How many characters need to be processed before the first start-of-message marker is detected?
"""


def answer(s):
    for end_idx in range(13, len(s)):
        if len(set(s[end_idx-13: end_idx+1])) == 14:
            return end_idx + 1


if __name__ == "__main__":
    answer_checker = AnswerChecker()
    answer_checker.check(19, answer("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
    answer_checker.check(23, answer("bvwbjplbgvbhsrlpgdmjqwftvncz"))
    answer_checker.check(23, answer("nppdvjthqldpwncqszvftbrmjlhg"))
    answer_checker.check(29, answer("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
    answer_checker.check(26, answer("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

    answer_checker.generate_puzzle_output(__file__, answer)
