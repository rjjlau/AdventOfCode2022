from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
"""


def answer(s):
    split_content = s.split("\n\n")

    stack_string = split_content[0].split("\n")
    commands = split_content[1].split("\n")
    stack = {}

    for line in stack_string:
        column = 0
        spaces = 0
        for c in line:
            if c == " ":
                spaces += 1
            elif c.isalpha():
                column += max(round((spaces-1)/4) + 1, 1)
                l = stack.get(column, [])
                l.insert(0, c)
                stack[column] = l
                spaces = 0

    for command in commands:
        move_count = int(command.split("move")[1].split("from")[0].strip())
        source = int(command.split("from")[1].split("to")[0].strip())
        destination = int(command.split("to")[1].strip())

        l = stack.get(source, [])
        popped = l[-move_count:]
        l = l[:-move_count]
        stack[source] = l

        l2 = stack.get(destination, [])
        l2 += popped
        stack[destination] = l2

    return "".join([stack[key][-1] for key in sorted(stack.keys())])


if __name__ == "__main__":

    test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    expected_output = """MCD"""

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)
