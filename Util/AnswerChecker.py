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
            self.logger.info("SUCCESS: Actual matches expected")
        else:
            self.logger.error(f"FAILED:\nExpected:\t{expected}\nActual:\t\t{actual}")
            if expected is not None and actual is not None:
                if len(expected) != len(actual):
                    self.logger.error(f"Expected a string of length {len(expected)} but received a string of length "
                                      f"{len(actual)}")
                    raise RuntimeError()
                for i in range(len(expected)):
                    if expected[i] != actual[i]:
                        self.logger.error(f"First difference occurred at position {i}: "
                                          f"{expected[max(0, i-2):i]}>>>{expected[i]}<<<"
                                          f"{expected[min(len(expected)-1, i+1):min(len(expected)-1, i+2)+1]}")
                        raise RuntimeError()

    def __get_puzzle_input(self, input_file_path):
        self.logger.info(f"Reading file {input_file_path} to get puzzle input")
        with open(Path(input_file_path)) as f:
            return f.read()

    def __ensure_directory_exists(self, directory):
        if not os.path.exists(directory):
            self.logger.info(f"Creating directory {directory}")
            os.mkdir(directory)

    def __write_results_to_file(self, results, file_name, directory):
        self.__ensure_directory_exists(directory)
        file_path = os.path.join(directory, file_name)
        self.logger.info(f"Writing results to file {file_path}")
        with open(file_path, "w") as f:
            f.write(str(results))

    def generate_puzzle_output(self, puzzle_file_path, function):
        file_path, file_name = os.path.split(os.path.abspath(puzzle_file_path))
        file_name = file_name.replace(".py", ".txt")
        input_path = os.path.join(os.path.join(Path(file_path).parent.parent, "Inputs"), file_path.split("\\")[-1])
        output_path = os.path.join(os.path.join(Path(file_path).parent.parent, "Outputs"), file_path.split("\\")[-1])
        input_text = self.__get_puzzle_input(os.path.join(input_path, file_name))
        output_text = function(input_text)
        self.__write_results_to_file(output_text, file_name, output_path)
        self.logger.info(f"Result(s): {output_text}")





if __name__ == "__main__":
    # answer_checker = AnswerChecker()
    # answer_checker.check("abcdef", "abcdefg")

    # x = os.path.split(os.path.abspath(__file__))
    print(x)



