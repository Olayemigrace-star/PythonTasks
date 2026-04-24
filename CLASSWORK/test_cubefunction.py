import unittest
import cubefunction

class TestCubeFunction(unittest.TestCase):

    def test_that_cube_function_exists(self):
        cubefunction.cube(3)
    def test_that_cube_function_return_correct_result(self):
        actual = cubefunction.cube(3)
        expected = 27
        self.assertEqual(actual, expected)
    def test_that_cube_function_return_invalid_data_type_with_wrong_input(self):
        actual = cubefunction.cube("boy")
        expected = "invalid input"
        self.assertEqual(actual, expected)
