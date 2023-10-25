import tkinter as tk
import unittest
import sys
sys.path.append('../../lab1')
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        calculator = Calculator(tk.Tk())
        calculator.button_5.invoke()
        calculator.add_button.invoke()
        calculator.button_7.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "12")

    def test_substruction(self):
        calculator = Calculator(tk.Tk())
        calculator.button_5.invoke()
        calculator.subtract_button.invoke()
        calculator.button_7.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "-2")

    def test_multiplication(self):
        calculator = Calculator(tk.Tk())
        calculator.button_8.invoke()
        calculator.multiply_button.invoke()
        calculator.button_2.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "16")

    def test_division(self):
        calculator = Calculator(tk.Tk())
        calculator.button_8.invoke()
        calculator.divide_button.invoke()
        calculator.button_2.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "4.0")

    def test_floor_division(self):
        calculator = Calculator(tk.Tk())
        calculator.button_8.invoke()
        calculator.floor_div_button.invoke()
        calculator.button_2.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "4")

    def test_moduling(self):
        calculator = Calculator(tk.Tk())
        calculator.button_3.invoke()
        calculator.modulus_button.invoke()
        calculator.button_2.invoke()
        calculator.equal_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "1")

    def test_root_calculation(self):
        calculator = Calculator(tk.Tk())
        calculator.button_4.invoke()
        calculator.sqrt_button.invoke()
        result = calculator.number_entry.get()
        self.assertEqual(result, "2")
