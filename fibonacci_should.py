#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR

import unittest

from Fibonacci import Fibbonacci


class Fibonacci_should(unittest.TestCase):
    def test_position_0_returns_1(self):
        #Arrange
        number = 0

        #Act
        result = Fibbonacci().act(number)

        #Assert
        self.assertEqual(result,1)

    def test_position_1_returns_1(self):
        #Arrange
        number = 1

        #Act
        result = Fibbonacci().act(number)

        #Assert
        self.assertEqual(result,1)