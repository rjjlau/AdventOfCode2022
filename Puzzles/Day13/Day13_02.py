from Util.AnswerChecker import AnswerChecker



"""
--- Part Two ---
Now, you just need to put all of the packets in the right order. Disregard the blank lines in your list of received packets.

The distress signal protocol also requires that you include two additional divider packets:

[[2]]
[[6]]
Using the same rules as before, organize all packets - the ones in your list of received packets as well as the two divider packets - into the correct order.

For the example above, the result of putting the packets in the correct order is:

[]
[[]]
[[[]]]
[1,1,3,1,1]
[1,1,5,1,1]
[[1],[2,3,4]]
[1,[2,[3,[4,[5,6,0]]]],8,9]
[1,[2,[3,[4,[5,6,7]]]],8,9]
[[1],4]
[[2]]
[3]
[[4,4],4,4]
[[4,4],4,4,4]
[[6]]
[7,7,7]
[7,7,7,7]
[[8,7,6]]
[9]
Afterward, locate the divider packets. To find the decoder key for this distress signal, you need to determine the indices of the two divider packets and multiply them together. (The first packet is at index 1, the second packet is at index 2, and so on.) In this example, the divider packets are 10th and 14th, and so the decoder key is 140.

Organize all of the packets into the correct order. What is the decoder key for the distress signal?
"""


def string_to_list(s):
    if s[0] == "[" and s[-1] == "]":
        s = s[1:-1]
    if s.isnumeric():
        return [int(s)]
    opens = []
    results = []
    start = None
    for i, v in enumerate(s):
        if v == "[":
            opens.append(i)
        elif v == "]":
            if len(opens) == 1:
                results.append(s[opens.pop(-1): i + 1])
            elif len(opens) > 0:
                opens.pop(-1)
        elif len(opens) == 0 and (i == 0 or s[i-1] != "]"):
            if v == ",":
                results.append(s[start:i])
                start = None
            elif start is None:
                if i == len(s) - 1:
                    results.append(s[-1:])
                else:
                    start = i
    return [string_to_list(i) if "[" in i and i != "[]" else [] if i == "[]" else int(i) for i in results]


def merge_sort(lists):
    if len(lists) == 1:
        return lists
    elif len(lists) == 2:
        if compare(lists[0], lists[1]):
            return lists
        else:
            return [lists[1], lists[0]]

    left = merge_sort(lists[:len(lists)//2])
    right = merge_sort(lists[len(lists)//2:])

    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) == 0:
            result += right
            break
        if len(right) == 0:
            result += left
            break
        result.append(left.pop(0) if compare(left[0], right[0]) else right.pop(0))
    return result


def compare(l, r):
    left_copy = list(l)
    right_copy = list(r)
    while len(left_copy) > 0 or len(right_copy) > 0:
        if len(left_copy) == 0:
            return True
        if len(right_copy) == 0:
            return False

        l = left_copy.pop(0)
        r = right_copy.pop(0)

        if isinstance(l, list) and isinstance(r, list):
            if len(l) > 0 and len(r) > 0:
                result = compare(l, r)
                if result is not None:
                    return result
            if len(l) == 0 and len(r) > 0:
                return True
            if len(l) > 0 and len(r) == 0:
                return False
        elif isinstance(l, list) or isinstance(r, list):
            result = compare(l if isinstance(l, list) else [l], r if isinstance(r, list) else [r])
            if result is not None:
                return result
        elif isinstance(l, int) or isinstance(r, int):
            if l < r:
                return True
            elif l > r:
                return False


def answer(s):
    lists = [[[2]], [[6]]]
    for i, pair in enumerate(s.split("\n\n")):
        lists.append(string_to_list(pair.split("\n")[0]))
        lists.append(string_to_list(pair.split("\n")[1]))

    sorted_lists = merge_sort(lists)
    indexes = [i + 1 for i, v in enumerate(sorted_lists) if v in ([[2]], [[6]])]
    output = 1
    while len(indexes) > 0:
        output *= indexes.pop(0)
    return output


if __name__ == "__main__":
    test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""
    expected_output = "140"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
