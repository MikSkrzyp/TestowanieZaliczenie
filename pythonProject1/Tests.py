import unittest
from unittest.mock import patch
from UserManager import UserManager
from Calculator import Calculator
class Tests(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.manager = UserManager()
    @patch('UserManager.UserManager.get_all_users')
    def test_get_all_users(self, mock_get_all):
        mock_get_all.return_value = {1: "Alice", 2: "Oskar"}
        result = self.manager.get_all_users()
        self.assertEqual(result, {1: "Alice", 2: "Oskar"})

    @patch('UserManager.UserManager.add_user')
    def test_add_user_Mikolaj(self, mock_add_user):
        mock_add_user.return_value = "User Mikolaj added with id 3"
        result = self.manager.add_user(3, "Mikolaj")
        self.assertEqual(result, "User Mikolaj added with id 3")

    @patch('UserManager.UserManager.update_user')
    def test_update_user_Alice(self, mock_update_user):
        mock_update_user.return_value = "User id 1 updated to Alice B."
        result = self.manager.update_user(1, "Alice B.")
        self.assertEqual(result, "User id 1 updated to Alice B.")

    @patch('UserManager.UserManager.delete_user')
    def test_delete_second_user(self, mock_delete_user):
        mock_delete_user.return_value = "User with id 2 deleted."
        result = self.manager.delete_user(2)
        self.assertEqual(result, "User with id 2 deleted.")

    @patch('UserManager.UserManager.add_user')
    def test_add_user_duplicate_id(self, mock_add_user):
        mock_add_user.return_value = "User with id 1 already exists."
        result = self.manager.add_user(1, "Bob")
        self.assertEqual(result, "User with id 1 already exists.")

    def test_add_two_positives(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract_two_positives(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply_positive_and_negative(self):
        self.assertEqual(self.calc.multiply(5, -1), -5)

    def test_divide_by_0(self):
        self.assertEqual(self.calc.divide(10, 0), "Error: Cannot divide by zero")

    def test_power_positive_and_negative(self):
        self.assertEqual(self.calc.power(2, -2), 0.25)

    def test_square_positive(self):
        self.assertEqual(self.calc.square(4), 16)

    def test_cube_positive(self):
        self.assertEqual(self.calc.cube(2), 8)

    def test_absolute_negative(self):
        self.assertEqual(self.calc.absolute(-5), 5)

    def test_sqrt_negative(self):
        self.assertEqual(self.calc.sqrt(-1), "Error: Cannot take the square root of a negative number")

    def test_mod_zero(self):
        self.assertEqual(self.calc.mod(25, 0), "Error: Cannot mod by zero")

if __name__ == '__main__':
    unittest.main()
