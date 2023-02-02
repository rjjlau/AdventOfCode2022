from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?
"""


def answer(s):
    grid = [r for r in s.split("\n")]
    start_pts = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                grid[y] = grid[y].replace("S", "a")
            elif grid[y][x] == "E":
                grid[y] = grid[y].replace("E", "z")
                end_x, end_y = x, y
            if grid[y][x] == "a":
                start_pts.append((x, y))

    min_steps = len(grid) * len(grid[0])

    for start_pt in start_pts:
        start_x, start_y = start_pt
        stack = [((start_x, start_y), 0)]
        visited = [(start_x, start_y)]

        # define top left as (0, 0)
        while len(stack) > 0:
            point = stack.pop(0)
            x, y = int(point[0][0]), int(point[0][1])
            steps = int(point[1])

            if point[0] == (end_x, end_y):
                min_steps = min(min_steps, point[1])

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
    return min_steps


if __name__ == "__main__":
    test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
    expected_output = "29"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)