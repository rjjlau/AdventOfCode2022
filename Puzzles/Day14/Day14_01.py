from Util.AnswerChecker import AnswerChecker

"""
--- Day 14: Regolith Reservoir ---
The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. However, you do notice a little path that leads behind the waterfall.

Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! If you don't quickly figure out where the sand is going, you could quickly become trapped!

Fortunately, your familiarity with analyzing the path of falling material will come in handy here. You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

The sand is pouring into the cave from point 500,0.

Drawing rock as #, air as ., and the source of the sand as +, this becomes:


  4     5  5
  9     0  0
  4     0  3
0 ......+...
1 ..........
2 ..........
3 ..........
4 ....#...##
5 ....#...#.
6 ..###...#.
7 ........#.
8 ........#.
9 #########.
Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. A unit of sand is large enough to fill one tile of air in your scan.

A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
......o.#.
#########.
The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
........#.
.....oo.#.
#########.
After a total of five units of sand have come to rest, they form this pattern:

......+...
..........
..........
..........
....#...##
....#...#.
..###...#.
......o.#.
....oooo#.
#########.
After a total of 22 units of sand:

......+...
..........
......o...
.....ooo..
....#ooo##
....#ooo#.
..###ooo#.
....oooo#.
...ooooo#.
#########.
Finally, only two more units of sand can possibly come to rest:

......+...
..........
......o...
.....ooo..
....#ooo##
...o#ooo#.
..###ooo#.
....oooo#.
.o.ooooo#.
#########.
Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

.......+...
.......~...
......~o...
.....~ooo..
....~#ooo##
...~o#ooo#.
..~###ooo#.
..~..oooo#.
.~o.ooooo#.
~#########.
~..........
~..........
~..........
Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?
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

    largest_rock_y = sorted(rock_coordinates, key=lambda x: x[1])[-1][1]

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
                    if coord[1] + 1 > largest_rock_y:  # this sand grain will fall for perpetuity
                        break
                    else:
                        coord = (coord[0], coord[1] + 1)
            if coord[0] - 1 >= 0 \
                    and (coord[0] - 1, coord[1] + 1) not in rock_coordinates \
                    and (coord[0] - 1, coord[1] + 1) not in sand_at_rest_coordinates:  # can go diagonal left
                if coord[1] + 1 > largest_rock_y:  # this sand grain will fall for perpetuity
                    break
                else:
                    coord = (coord[0] - 1, coord[1] + 1)
            elif (coord[0] + 1, coord[1] + 1) not in rock_coordinates \
                    and (coord[0] + 1, coord[1] + 1) not in sand_at_rest_coordinates:  # can go diagonal right
                if coord[1] + 1 > largest_rock_y:  # this sand grain will fall for perpetuity
                    break
                else:
                    coord = (coord[0] + 1, coord[1] + 1)
            if coord == start_coord:  # sand has come to rest
                sand_at_rest_coordinates.add(coord)
                break
        if count_sand_at_rest == len(sand_at_rest_coordinates):  # sand has started falling perpetually
            break

    return count_sand_at_rest


if __name__ == "__main__":
    test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    expected_output = "24"

    answer_checker = AnswerChecker()

    answer_checker.check(expected_output, answer(test_input))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
