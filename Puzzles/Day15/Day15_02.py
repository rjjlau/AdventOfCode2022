from Util.AnswerChecker import AnswerChecker

"""
--- Part Two ---
Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

To isolate the distress beacon's signal, you need to determine its tuning frequency, which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. The tuning frequency for this distress beacon is 56000011.

Find the only possible position for the distress beacon. What is its tuning frequency?
"""


def calculate_tuning_frequency(c):
    return c[0] * 4000000 + c[1]


def manhattan_distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def string_to_tuple_coord(s):
    return tuple(int(i.split("=")[1]) for i in s.replace(" ", "").split(","))


def answer(s, search_area=4000000):
    sensors = []
    candidates = set()
    for line in s.split("\n"):
        sensor_line, beacon_line = line.split(":")
        sensor_coord_str = sensor_line.replace("Sensor at ", "").strip()
        beacon_coord_str = beacon_line.replace("closest beacon is at ", "").strip()
        sensor_coord = string_to_tuple_coord(sensor_coord_str)
        beacon_coord = string_to_tuple_coord(beacon_coord_str)
        m_dist = manhattan_distance(sensor_coord, beacon_coord)

        sensors.append((sensor_coord, m_dist))

        if search_area >= sensor_coord[0] >= 0:
            if search_area >= sensor_coord[1] - m_dist - 1 >= 0:
                candidates.add((sensor_coord[0], sensor_coord[1] - m_dist - 1))  # top of diamond
            if search_area >= sensor_coord[1] + m_dist + 1:
                candidates.add((sensor_coord[0], sensor_coord[1] + m_dist + 1))  # bottom of diamond

        step = 0
        y = sensor_coord[1] - m_dist
        while y <= sensor_coord[1] + m_dist:
            if search_area >= y >= 0:
                if search_area >= sensor_coord[0] - step - 1 >= 0:  # left
                    candidates.add((sensor_coord[0] - step - 1, y))
                if search_area >= sensor_coord[0] + step + 1 >= 0:  # right
                    candidates.add((sensor_coord[0] + step + 1, y))
            y += 1
            if y <= sensor_coord[1]:
                step += 1
            else:
                step -= 1

    for i, candidate in enumerate(candidates):
        print(f"Checking candidate number {i} out of {len(candidates)} possible candidates: {candidate} ")
        for sensor in sensors:
            if manhattan_distance(candidate, sensor[0]) <= sensor[1]:
                break
        else:
            return calculate_tuning_frequency(candidate)


if __name__ == "__main__":
    test_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
    expected_output = "56000011"

    answer_checker = AnswerChecker()
    answer_checker.check(expected_output, answer(test_input, 20))

    answer_checker.generate_puzzle_output(__file__, answer)

    # answer_checker.generate_next_day_files(__file__)
