from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

        ...........+........
        ....................
        ....................
        ....................
        .........#...##.....
        .........#...#......
        .......###...#......
        .............#......
        .............#......
        .....#########......
        ....................
<-- etc #################### etc -->
To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

............o............
...........ooo...........
..........ooooo..........
.........ooooooo.........
........oo#ooo##o........
.......ooo#ooo#ooo.......
......oo###ooo#oooo......
.....oooo.oooo#ooooo.....
....oooooooooo#oooooo....
...ooo#########ooooooo...
..ooooo.......ooooooooo..
#########################
Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?
"""


def answer(s):
    lines = s.split("\n")
    rock_coordinates = set()
    for line in lines:
        line_split = line.split(" -> ")
        for i in range(len(line_split) - 1):
            left = tuple([int(coord) for coord in line_split[i].split(",")])
            right = tuple([int(coord) for coord in line_split[i + 1].split(",")])
            if left[0] == right[0]:  # moving vertically
                for j in range(min(left[1], right[1]),  max(left[1], right[1]) + 1):
                    rock_coordinates.add((left[0], j))
            if left[1] == right[1]:  # moving horizontally
                for k in range(min(left[0], right[0]),  max(left[0], right[0]) + 1):
                    rock_coordinates.add((k, left[1]))

    largest_rock_y = sorted(rock_coordinates, key=lambda x: x[1])[-1][1] + 2

    sand_at_rest_coordinates = set()
    while True:  # while sand can still fall to rest
        count_sand_at_rest = len(sand_at_rest_coordinates)
        coord = (500, 0)  # fixed start point
        while True:  # while this particular grain can still fall
            start_coord = coord
            if (coord[0], coord[1] + 1) not in rock_coordinates \
                    and (coord[0], coord[1] + 1) not in sand_at_rest_coordinates:  # can go down
                while (coord[0], coord[1] + 1) not in rock_coordinates \
                        and (coord[0], coord[1] + 1) not in sand_at_rest_coordinates:
                    if coord[1] + 1 == largest_rock_y:  # this sand grain will hit the ground on the next iteration
                        sand_at_rest_coordinates.add(coord)
                        break
                    else:
                        coord = (coord[0], coord[1] + 1)
            if coord[0] - 1 >= 0 \
                    and (coord[0] - 1, coord[1] + 1) not in rock_coordinates \
                    and (coord[0] - 1, coord[1] + 1) not in sand_at_rest_coordinates:  # can go diagonal left
                if coord[1] + 1 == largest_rock_y:  # this sand grain will hit the ground on the next iteration
                    sand_at_rest_coordinates.add(coord)
                    break
                else:
                    coord = (coord[0] - 1, coord[1] + 1)
            elif (coord[0] + 1, coord[1] + 1) not in rock_coordinates \
                    and (coord[0] + 1, coord[1] + 1) not in sand_at_rest_coordinates:  # can go diagonal right
                if coord[1] + 1 == largest_rock_y:  # this sand grain will hit the ground on the next iteration
                    sand_at_rest_coordinates.add(coord)
                    break
                else:
                    coord = (coord[0] + 1, coord[1] + 1)
            if coord == start_coord:  # sand has come to rest
                sand_at_rest_coordinates.add(coord)
                break
        if count_sand_at_rest == len(sand_at_rest_coordinates):  # sand inlet has been blocked
            break

    return count_sand_at_rest


if __name__ == "__main__":
    test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    expected_output = "93"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
