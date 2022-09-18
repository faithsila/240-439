from code_main.code_fizzbuzz import super_fizz_buzz

import unittest


class Mod_3(unittest.TestCase):

    def test_give_lowwest_bordery(self):
        test_number = 3
        test = super_fizz_buzz(test_number)
        self.assertEqual('Fizz', test, 'fail')

    def test_give_middle_bordery(self):
        test_number = 5001
        test = super_fizz_buzz(test_number)
        self.assertEqual('Fizz', test, 'fail')

    def test_give_highest_bordery(self):
        test_number = 9996
        test = super_fizz_buzz(test_number)
        self.assertEqual('Fizz', test, 'fail')


class Mod_5(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        test_number = 5
        test = super_fizz_buzz(test_number)
        self.assertEqual('Buzz', test, 'fail')

    def test_give_middile_bordery(self):
        test_number = 5005
        test = super_fizz_buzz(test_number)
        self.assertEqual('Buzz', test, 'fail')
    
    def test_give_highest_bordery(self):
        test_number = 9995
        test = super_fizz_buzz(test_number)
        self.assertEqual('Buzz', test, 'fail')


class Mod_9(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        test_number = 9
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzFizz', test, 'fail')

    def test_give_middle_bordery(self):
        test_number = 4986
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzFizz', test, 'fail')

    def test_give_highest_bordery(self):
        test_number = 9999
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzFizz', test, 'fail')


class Mod_25(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        test_number = 25
        test = super_fizz_buzz(test_number)
        self.assertEqual('BuzzBuzz', test, 'fail')

    def test_give_middle_bordery(self):
        test_number = 5000
        test = super_fizz_buzz(test_number)
        self.assertEqual('BuzzBuzz', test, 'fail')

    def test_give_highest_bordery(self):
        test_number = 10000
        test = super_fizz_buzz(test_number)
        self.assertEqual('BuzzBuzz', test, 'fail')


class Mod_3and5(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        test_number = 15
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzBuzz', test, 'fail')

    def test_give_middle_bordery(self):
        test_number = 5010
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzBuzz', test, 'fail')

    def test_give_highest_bordery(self):
        test_number = 9975
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzBuzz', test, 'fail')


class Mod_9and25(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        test_number = 225
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')

    def test_give_middle_bordery(self):    
        test_number = 5175
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')
        
    def test_give_highhest_bordery(self):
        test_number = 9900
        test = super_fizz_buzz(test_number)
        self.assertEqual('FizzFizzBuzzBuzz', test, 'fail')

class Notmacthcase(unittest.TestCase):
    def test_give_lowwest_bordery(self):
        test_number = 1
        test = super_fizz_buzz(test_number)
        self.assertEqual('NoFizzBuzz', test, 'fail')

    def test_give_middle_bordery(self):
        test_number = 5002
        test = super_fizz_buzz(test_number)
        self.assertEqual('NoFizzBuzz', test, 'fail')

    def test_give_highhest_bordery(self):
        test_number = 9998
        test = super_fizz_buzz(test_number)
        self.assertEqual('NoFizzBuzz', test, 'fail')