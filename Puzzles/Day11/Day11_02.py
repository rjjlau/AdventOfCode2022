from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
You're worried you might not ever get your items back. So worried, in fact, that your relief that a monkey's inspection didn't damage an item no longer causes your worry level to be divided by three.

Unfortunately, that relief was all that was keeping your worry levels from reaching ridiculous levels. You'll need to find another way to keep your worry levels manageable.

At this rate, you might be putting up with these monkeys for a very long time - possibly 10000 rounds!

With these new rules, you can still figure out the monkey business after 10000 rounds. Using the same example above:

== After round 1 ==
Monkey 0 inspected items 2 times.
Monkey 1 inspected items 4 times.
Monkey 2 inspected items 3 times.
Monkey 3 inspected items 6 times.

== After round 20 ==
Monkey 0 inspected items 99 times.
Monkey 1 inspected items 97 times.
Monkey 2 inspected items 8 times.
Monkey 3 inspected items 103 times.

== After round 1000 ==
Monkey 0 inspected items 5204 times.
Monkey 1 inspected items 4792 times.
Monkey 2 inspected items 199 times.
Monkey 3 inspected items 5192 times.

== After round 2000 ==
Monkey 0 inspected items 10419 times.
Monkey 1 inspected items 9577 times.
Monkey 2 inspected items 392 times.
Monkey 3 inspected items 10391 times.

== After round 3000 ==
Monkey 0 inspected items 15638 times.
Monkey 1 inspected items 14358 times.
Monkey 2 inspected items 587 times.
Monkey 3 inspected items 15593 times.

== After round 4000 ==
Monkey 0 inspected items 20858 times.
Monkey 1 inspected items 19138 times.
Monkey 2 inspected items 780 times.
Monkey 3 inspected items 20797 times.

== After round 5000 ==
Monkey 0 inspected items 26075 times.
Monkey 1 inspected items 23921 times.
Monkey 2 inspected items 974 times.
Monkey 3 inspected items 26000 times.

== After round 6000 ==
Monkey 0 inspected items 31294 times.
Monkey 1 inspected items 28702 times.
Monkey 2 inspected items 1165 times.
Monkey 3 inspected items 31204 times.

== After round 7000 ==
Monkey 0 inspected items 36508 times.
Monkey 1 inspected items 33488 times.
Monkey 2 inspected items 1360 times.
Monkey 3 inspected items 36400 times.

== After round 8000 ==
Monkey 0 inspected items 41728 times.
Monkey 1 inspected items 38268 times.
Monkey 2 inspected items 1553 times.
Monkey 3 inspected items 41606 times.

== After round 9000 ==
Monkey 0 inspected items 46945 times.
Monkey 1 inspected items 43051 times.
Monkey 2 inspected items 1746 times.
Monkey 3 inspected items 46807 times.

== After round 10000 ==
Monkey 0 inspected items 52166 times.
Monkey 1 inspected items 47830 times.
Monkey 2 inspected items 1938 times.
Monkey 3 inspected items 52013 times.
After 10000 rounds, the two most active monkeys inspected items 52166 and 52013 times. Multiplying these together, the level of monkey business in this situation is now 2713310158.

Worry levels are no longer divided by three after each item is inspected; you'll need to find another way to keep your worry levels manageable. Starting again from the initial state in your puzzle input, what is the level of monkey business after 10000 rounds?
"""


def apply_operation(operation, worry_level):
    left, operand, right = operation.split()
    left_int = worry_level if left == "old" else int(left)
    right_int = worry_level if right == "old" else int(right)

    if operand == "+":
        return left_int + right_int
    elif operand == "*":
        return left_int * right_int
    else:
        raise RuntimeError(f"Operand {operand} is not supported")


def answer(s):
    items_dict = {}
    operations_dict = {}
    test_divisors_dict = {}
    test_true_destinations_dict = {}
    test_false_destinations_dict = {}
    inspection_counts_dict = {}
    chinese_divisor = 1

    # Read input and initialize maps
    for monkey in s.split("Monkey")[1:]:
        monkey_details = monkey.split("\n")
        monkey_idx = int(monkey_details[0].strip().replace(":", ""))
        monkey_starting_items = [int(i.strip()) for i in monkey_details[1].split(":")[1].strip().split(",")]
        monkey_operation = monkey_details[2].split("=")[1].strip()
        monkey_test_divisor = int(monkey_details[3].split("by")[1].strip())
        monkey_test_true_destination = int(monkey_details[4].split("monkey")[1].strip())
        monkey_test_false_destination = int(monkey_details[5].split("monkey")[1].strip())

        items_dict[monkey_idx] = monkey_starting_items
        operations_dict[monkey_idx] = monkey_operation
        test_divisors_dict[monkey_idx] = monkey_test_divisor
        test_true_destinations_dict[monkey_idx] = monkey_test_true_destination
        test_false_destinations_dict[monkey_idx] = monkey_test_false_destination
        chinese_divisor *= monkey_test_divisor

    for r in range(1, 10001):
        for idx in range(len(items_dict)):
            items = items_dict[idx]
            operation = operations_dict[idx]
            test_divisor = test_divisors_dict[idx]
            test_true_destination = test_true_destinations_dict[idx]
            test_false_destination = test_false_destinations_dict[idx]

            for i in range(len(items)):
                inspection_counts_dict[idx] = inspection_counts_dict.get(idx, 0) + 1
                worry_level = items[i]
                worry_level = apply_operation(operation, worry_level)

                if worry_level % test_divisor == 0:
                    destination = test_true_destination
                else:
                    destination = test_false_destination
                items_dict[destination] = items_dict[destination] + [worry_level % chinese_divisor]
            items_dict[idx] = []

        # print(f"Round {r}: {items_dict}\n{inspection_counts_dict}\n")
    sorted_counts = sorted(inspection_counts_dict.values())
    return sorted_counts[-1] * sorted_counts[-2]


if __name__ == "__main__":
    test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    expected_output = "2713310158"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
