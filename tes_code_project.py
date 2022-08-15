import unittest
from unittest import mock

import dietary
from welcome_page import formatted_name
from main import run
from dietary import DietaryRequirements




class Test(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name("jack", "black")
        actual = "Jack Black"
        self.assertEqual(result, actual)

    def test_if_input_is_string(self):
        string = formatted_name('first_name', 'last_name')
        self.assertEqual(True, isinstance(string, str))

    def test_exceptions(self):
      with self.assertRaises(Exception):
          formatted_name('Jack' + m)

    def test_if_capitalized(self):
        actual = 'python'
        result = actual.capitalize()
        self.assertEqual(result, 'Python')

    def test_if_lower(self):
        actual = 'Python'
        result = actual.lower()
        self.assertEqual(result, 'python')

    @mock.patch('dietary.DietaryRequirements.get_input',create=True)
    def test_requirements_input(self, mocked_input):
        mocked_input.side_effect = ['vegan']
        result = DietaryRequirements
        self.assertEqual(result, dietary.DietaryRequirements)

    @mock.patch('main.run.get_input', create=True)
    def test_requirement_input_is_none(self, mocked_input):
        mocked_input.side_effect = ['']
        result = run()
        self.assertEqual(result, None)




if __name__ == '__main__':
    unittest.main()