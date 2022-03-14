import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculate_filed(self):
        assert self.calc.multiply(self, 2, 2) != 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_division_calculate_filed(self):
        assert self.calc.division(self, 8, 2) != 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_subtraction_calculate_filed(self):
        assert self.calc.subtraction(self, 8, 2) != 3

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 10, 2) == 12

    def test_adding_calculate_filed(self):
        assert self.calc.adding(self, 8, 2) != 11
        
