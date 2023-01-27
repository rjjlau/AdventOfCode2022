from Util.AnswerChecker import AnswerChecker

"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
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

        for i in range(move_count):
            l = stack.get(source, [])
            if len(l) == 0:
                print(command)
                print(stack)

            popped = l.pop()
            stack[source] = l

            l2 = stack.get(destination, [])
            l2.append(popped)
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
    expected_output = """CMZ"""

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)
