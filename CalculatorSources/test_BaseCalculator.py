from unittest import TestCase
from BaseCalculator import BaseCalculator
import LookupError


# Class for testing the BaseCalculator implementation.
class TestBaseCalculator(TestCase):
    # DataDriven tests.
    # TODO: Read this from a resource file.
    inputs = (
        ["5*(4/2)", 10.0],
        ["6 * (7 / (3 + 4))", 6.0 ],
        ["259.41 + (-6) - (-362) - (-660) / (-900)", 614.6766666666667],
        ["6 *  7 / 3 + 4", 18.0],
        ["6 *  7 / 3 % 4", 2.0],
        ["6 *  19683 / 3 ^ 3 ^ 2", 6.0],
        ["6 *  27 / 3 ^ 3", 6.0],
        ["4! + 10 % 3", 25.0],
        ["6 *  4096 | 3 ^ 2", "ExpectError"],
        ["6& 2 (23)-", "ExpectError"],
        ["", "ExpectError"],
        ["2 + 3(5)", 17],
        ["sin(90) + 2 * 3", 7],
        ["23,000 * 2 + 3", "46,003"],
        ["2_4 * 2 + 3", 51],
        ["24 * 2 + 3 / 0", "ExpectError"]
    )

    # Running the tests from the list of inputs Tuple.
    def test_RunTest(self):
        calc = BaseCalculator()
        for input in self.inputs:
            try:
                result = calc.evaluate(input[0])
                self.assertEqual(input[1], result)
            except:
                print(str.format("Test failed for input:{0}, expected:{1}, got:{2}", input[0], input[1], result))

if __name__ == "__main__":
        unittest.main()