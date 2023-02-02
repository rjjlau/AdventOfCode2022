from Util.AnswerChecker import AnswerChecker

"""
--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?
"""


def answer(s):

    grid = [r for r in s.split("\n")]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                grid[y] = grid[y].replace("S", "a")
                start_x, start_y = x, y
            elif grid[y][x] == "E":
                grid[y] = grid[y].replace("E", "z")
                end_x, end_y = x, y

    stack = [((start_x, start_y), 0)]
    visited = [(start_x, start_y)]

    # define top left as (0, 0)
    while len(stack) > 0:
        print(stack)
        point = stack.pop(0)
        x, y = int(point[0][0]), int(point[0][1])
        steps = int(point[1])

        if point[0] == (end_x, end_y):
            return point[1]

        # left
        if x - 1 >= 0 and ord(grid[y][x - 1]) - ord(grid[y][x]) <= 1 and (x - 1, y) not in visited:
            if ((x - 1, y), steps + 1) not in stack:
                stack.append(((x - 1, y), steps + 1))
            print(f"Can go left from {x, y}")
        # up
        if y - 1 >= 0 and ord(grid[y - 1][x]) - ord(grid[y][x]) <= 1 and (x, y - 1) not in visited:
            if ((x, y - 1), steps + 1) not in stack:
                stack.append(((x, y - 1), steps + 1))
            print(f"Can go up from {x, y}")
        # right
        if x + 1 < len(grid[0]) and ord(grid[y][x + 1]) - ord(grid[y][x]) <= 1 and (x + 1, y) not in visited:
            if ((x + 1, y), steps + 1) not in stack:
                stack.append(((x + 1, y), steps + 1))
            print(f"Can go right from {x, y}")
        # down
        if y + 1 < len(grid) and ord(grid[y + 1][x]) - ord(grid[y][x]) <= 1 and (x, y + 1) not in visited:
            if ((x, y + 1), steps + 1) not in stack:
                stack.append(((x, y + 1), steps + 1))
            print(f"Can go down from {x, y}")
        visited.append(point[0])


if __name__ == "__main__":
    test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    expected_output = "31"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
