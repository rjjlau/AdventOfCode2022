import logging


class AnswerChecker:
    def __init__(self):
        logging.basicConfig(format="%(asctime)s.%(msecs)-3d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
                            datefmt="%Y-%m-%d:%H:%M:%S",
                            level="INFO")
        self.logger = logging.getLogger("logger")

    def check(self, expected, actual):
        if expected == actual:
            self.logger.info("SUCCESS: Actual matches expected")
        else:
            self.logger.error(f"FAILED:\nExpected:\t{expected}\nActual:\t\t{actual}")
            if expected is not None and actual is not None:
                if len(expected) != len(actual):
                    self.logger.error(f"Expected a string of length {len(expected)} but received a string of length "
                                      f"{len(actual)}")
                    return
                for i in range(len(expected)):
                    if expected[i] != actual[i]:
                        self.logger.error(f"First difference occurred at position {i}: "
                                          f"{expected[max(0, i-2):i]}>>>{expected[i]}<<<"
                                          f"{expected[min(len(expected)-1, i+1):min(len(expected)-1, i+2)+1]}")
                        return


if __name__ == "__main__":
    answer_checker = AnswerChecker()
    answer_checker.check("abcdef", "abcdefg")
