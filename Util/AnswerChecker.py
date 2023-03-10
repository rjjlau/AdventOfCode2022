import logging
import os
from pathlib import Path


class AnswerChecker:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s.%(msecs)-3d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                            datefmt="%Y-%m-%d:%H:%M:%S",
                            level="INFO")
        self.logger = logging.getLogger("logger")

    def check(self, expected, actual):
        expected = str(expected)
        actual = str(actual)

        if expected == actual:
            self.logger.info(f"SUCCESS: Actual matches expected -> {actual}")
        else:
            self.logger.error(f"FAILED:\nExpected:\t{expected}\nActual:\t\t{actual}")
            if expected is not None and actual is not None:
                if len(expected) != len(actual):
                    e1 = f"Expected a string of length {len(expected)} but received a string of length " \
                         f"{len(actual)}"
                    self.logger.error(e1)
                    raise RuntimeError(e1)
                for i in range(len(expected)):
                    if expected[i] != actual[i]:
                        e2 = f"First difference occurred at position {i}: " \
                             f"{expected[max(0, i-2):i]}>>>{expected[i]}<<<" \
                             f"{'' if i == len(expected) - 1 else expected[min(len(expected)-1, i+1):min(len(expected)-1, i+2)+1]}"
                        self.logger.error(e2)
                        raise RuntimeError(e2)

    def __get_puzzle_input(self, input_file_path):
        self.logger.info(f"Reading file {input_file_path} to get puzzle input")
        with open(Path(input_file_path)) as f:
            return f.read()

    def __create_directory_if_not_exists(self, directory):
        if not os.path.exists(directory):
            self.logger.info(f"Creating directory {directory}")
            os.mkdir(directory)

    def __write_results_to_file(self, results, file_name, directory):
        self.__create_directory_if_not_exists(directory)
        file_path = os.path.join(directory, file_name.replace(".py", ".txt"))
        self.logger.info(f"Writing results to file {file_path}")
        with open(file_path, "w") as f:
            f.write(str(results))

    def generate_puzzle_output(self, puzzle_file_path, function):
        day_path, file_name = os.path.split(os.path.abspath(puzzle_file_path))
        puzzle_path, day = os.path.split(os.path.abspath(day_path))
        input_path = os.path.join(os.path.join(Path(puzzle_path).parent, "Inputs"), day)
        input_text = self.__get_puzzle_input(os.path.join(input_path, day + ".txt"))
        output_path = os.path.join(os.path.join(Path(puzzle_path).parent, "Outputs"), day)
        output_text = function(input_text)
        self.__write_results_to_file(output_text, file_name, output_path)
        self.logger.info(f"Answer: {output_text}")

    def generate_next_day_files(self, puzzle_file_path):
        day_path, file_name = os.path.split(os.path.abspath(puzzle_file_path))
        puzzle_path, day = os.path.split(os.path.abspath(day_path))
        next_day = "Day" + str(int(day.split("Day")[1]) + 1).rjust(2, "0")

        with open(os.path.join(puzzle_path, "template.py"), "r") as f:
            template_content = f.read()
            new_day_path = os.path.join(puzzle_path, next_day)
            self.__create_directory_if_not_exists(new_day_path)
            with open(os.path.join(new_day_path, next_day + "_01.py"), "w") as p1:
                p1.write(template_content)
            with open(os.path.join(new_day_path, next_day + "_02.py"), "w") as p2:
                p2.write(template_content)

        input_path = os.path.join(os.path.join(Path(puzzle_path).parent, "Inputs"), next_day)
        self.__create_directory_if_not_exists(input_path)
        f2 = open(os.path.join(input_path, next_day + ".txt"), "w")
        f2.close()





