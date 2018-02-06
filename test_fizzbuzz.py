import unittest


def fizzbuzz(number):
    if number == 3:
        return 'fuzz'


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')


unittest.main()
