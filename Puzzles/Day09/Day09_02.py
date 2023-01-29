from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the ropes that broke are now whipping toward you as you fall through the air!

The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being hit. Fortunately, your simulation can be extended to support longer ropes.

Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same rules as before.

Using the same series of motions as the above example, but with the knots marked H, 1, 2, ..., 9, the motions now occur as follows:

== Initial State ==

......
......
......
......
H.....  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)

== R 4 ==

......
......
......
......
1H....  (1 covers 2, 3, 4, 5, 6, 7, 8, 9, s)

......
......
......
......
21H...  (2 covers 3, 4, 5, 6, 7, 8, 9, s)

......
......
......
......
321H..  (3 covers 4, 5, 6, 7, 8, 9, s)

......
......
......
......
4321H.  (4 covers 5, 6, 7, 8, 9, s)

== U 4 ==

......
......
......
....H.
4321..  (4 covers 5, 6, 7, 8, 9, s)

......
......
....H.
.4321.
5.....  (5 covers 6, 7, 8, 9, s)

......
....H.
....1.
.432..
5.....  (5 covers 6, 7, 8, 9, s)

....H.
....1.
..432.
.5....
6.....  (6 covers 7, 8, 9, s)

== L 3 ==

...H..
....1.
..432.
.5....
6.....  (6 covers 7, 8, 9, s)

..H1..
...2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

.H1...
...2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

== D 1 ==

..1...
.H.2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

== R 4 ==

..1...
..H2..
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

..1...
...H..  (H covers 2)
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

......
...1H.  (1 covers 2)
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

......
...21H
..43..
.5....
6.....  (6 covers 7, 8, 9, s)

== D 1 ==

......
...21.
..43.H
.5....
6.....  (6 covers 7, 8, 9, s)

== L 5 ==

......
...21.
..43H.
.5....
6.....  (6 covers 7, 8, 9, s)

......
...21.
..4H..  (H covers 3)
.5....
6.....  (6 covers 7, 8, 9, s)

......
...2..
..H1..  (H covers 4; 1 covers 3)
.5....
6.....  (6 covers 7, 8, 9, s)

......
...2..
.H13..  (1 covers 4)
.5....
6.....  (6 covers 7, 8, 9, s)

......
......
H123..  (2 covers 4)
.5....
6.....  (6 covers 7, 8, 9, s)

== R 2 ==

......
......
.H23..  (H covers 1; 2 covers 4)
.5....
6.....  (6 covers 7, 8, 9, s)

......
......
.1H3..  (H covers 2, 4)
.5....
6.....  (6 covers 7, 8, 9, s)
Now, you need to keep track of the positions the new tail, 9, visits. In this example, the tail never moves, and so it only visits 1 position. However, be careful: more types of motion are possible than before, so you might want to visually compare your simulated rope to the one above.

Here's a larger example:

R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
These motions occur as follows (individual steps are not shown):

== Initial State ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........H..............  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
..........................
..........................
..........................
..........................
..........................

== R 5 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........54321H.........  (5 covers 6, 7, 8, 9, s)
..........................
..........................
..........................
..........................
..........................

== U 8 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
................H.........
................1.........
................2.........
................3.........
...............54.........
..............6...........
.............7............
............8.............
...........9..............  (9 covers s)
..........................
..........................
..........................
..........................
..........................

== L 8 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
........H1234.............
............5.............
............6.............
............7.............
............8.............
............9.............
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

== D 3 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
.........2345.............
........1...6.............
........H...7.............
............8.............
............9.............
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

== R 17 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
................987654321H
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

== D 10 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........s.........98765
.........................4
.........................3
.........................2
.........................1
.........................H

== L 25 ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
H123456789................

== U 20 ==

H.........................
1.........................
2.........................
3.........................
4.........................
5.........................
6.........................
7.........................
8.........................
9.........................
..........................
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

Now, the tail (9) visits 36 positions (including s) at least once:

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
#.........................
#.............###.........
#............#...#........
.#..........#.....#.......
..#..........#.....#......
...#........#.......#.....
....#......s.........#....
.....#..............#.....
......#............#......
.......#..........#.......
........#........#........
.........########.........
Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?
"""


def __move_one_step(coordinate, direction):
    if direction == "L":
        coordinate[0] -= 1
    elif direction == "U":
        coordinate[1] += 1
    elif direction == "R":
        coordinate[0] += 1
    elif direction == "D":
        coordinate[1] -= 1
    return coordinate


def plot(coordinates):
    # min_x, max_x = min(c[0] for c in coordinates), max(c[0] for c in coordinates)
    # min_y, max_y = min(c[1] for c in coordinates), max(c[1] for c in coordinates)

    adjustment = 20
    # if min_x < 0 or min_y < 0:
    #     adjustment = abs(min(min_x, min_y))

    coordinates = [[c[0] + adjustment, c[1] + adjustment] for c in coordinates]
    grid_size = 40
    grid = [["." * grid_size] for i in range(grid_size)]

    for i in range(len(coordinates)):
        c = coordinates[i]
        x, y = c[0], c[1]
        l = [c for c in grid[y][0]]
        l[x] = "H" if i == 0 else str(i)
        grid[y] = ["".join(l)]

    s = [c for c in grid[adjustment][0]]
    s[adjustment] = "s"
    grid[adjustment] = ["".join(s)]

    for r in grid[::-1]:
        print(r[0])
    print("\n")


def answer(s):
    commands = s.split("\n")
    coordinates = [[0, 0] for i in range(10)]
    tail_visited = {(0, 0)}

    for command in commands:
        direction = command.split()[0]
        steps = int(command.split()[1])

        for step in range(steps):
            __move_one_step(coordinates[0], direction)
            for i in range(1, len(coordinates)):
                h = coordinates[i-1]
                t = coordinates[i]
                # directly left, up, right or down by 2 steps
                if (h[0] == t[0] and abs(h[1] - t[1]) == 2) or (h[1] == t[1] and abs(h[0] - t[0]) == 2):
                    if h[0] == t[0]:
                        if h[1] > t[1]:
                            d = "U"
                        else:
                            d = "D"
                    if h[1] == t[1]:
                        if h[0] < t[0]:
                            d = "L"
                        else:
                            d = "R"
                    __move_one_step(t, d)
                elif (h[0] != t[0] and abs(h[1] - t[1]) == 2) or (h[1] != t[1] and abs(h[0] - t[0]) == 2):  # diagonal
                    if h[0] < t[0]:  # head is to left of tail
                        __move_one_step(t, "L")
                    elif h[0] > t[0]:  # head is to right of tail
                        __move_one_step(t, "R")
                    if h[1] < t[1]:  # head is below tail
                        __move_one_step(t, "D")
                    elif h[1] > t[1]:  # head is above tail
                        __move_one_step(t, "U")
                if i == len(coordinates) - 1:
                    tail_visited.add(tuple(t))
    return len(tail_visited)


if __name__ == "__main__":
    test_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    expected_output = "36"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    answer_checker.generate_next_day_files(__file__)