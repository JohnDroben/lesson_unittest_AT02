import pytest
import unittest
from main import add, subtract, multiply, divide, safe_remainder, count_vowels

class TestMath(unittest.TestCase):
   def test_add(self):
       self.assertEqual(add(2, 5),7)
       self.assertNotEqual(add(3, 7), 9)

   def test_subtract(self):
       self.assertEqual(subtract(7, 4), 3)
       self.assertNotEqual(subtract(4, 2), 1)

   def test_multiply(self):
       self.assertNotEqual(multiply(2, 5), 12)
       self.assertEqual(multiply(3, 6), 18)

   def test_divide(self):
       self.assertNotEqual(divide(4, 2), 3)
       self.assertEqual(divide(20, 5), 4)

   def test_safe_remainder(self):
       self.assertEqual(safe_remainder(10, 3), 1)
       self.assertEqual(safe_remainder(20, 7), 6)
       self.assertEqual(safe_remainder(0, 5), 0)
       self.assertEqual(safe_remainder(20, -7), -1)
       self.assertEqual(safe_remainder(-20, -7), -6)
       self.assertEqual(safe_remainder(10 ** 15, 123), 10 ** 15 % 123)

# Тесты для проверки функции count_vowels
class TestCountVowels(unittest.TestCase):
    def test_all_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("aAeEiIoOuU"), 10)

    def test_no_vowels(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels("XYZ"), 0)
        self.assertEqual(count_vowels("123!@#"), 0)

    def test_mixed_case_and_characters(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("Python is AWESOME"), 6)
        self.assertEqual(count_vowels("The quick brown fox"), 5)
        self.assertEqual(count_vowels("Привет мир!"), 0)  # Кириллица не содержит английских гласных

    def test_only_vowels_mixed_case(self):
        self.assertEqual(count_vowels("aEiOu"), 5)
        self.assertEqual(count_vowels("AeIoU"), 5)

    # Тесты Pytest для функции count_vowels
    def test_only_vowels_lowercase(self):
        assert count_vowels("aeiou") == 5

    def test_only_vowels_uppercase(self):
        assert count_vowels("AEIOU") == 5

    def test_only_vowels_mixed_case(self):
        assert count_vowels("aAeEiIoOuU") == 10

    def test_no_vowels_empty_string(self):
        assert count_vowels("") == 0

    def test_no_vowels_consonants(self):
        assert count_vowels("bcdfgxyz") == 0

    def test_no_vowels_special_chars(self):
        assert count_vowels("123!@# $%^&*()") == 0

    def test_mixed_string(self):
        assert count_vowels("Hello World") == 3

    def test_mixed_case_complex(self):
        assert count_vowels("Python is AWESOME") == 6

    def test_with_numbers_and_punctuation(self):
        assert count_vowels("A1e! I?o U.") == 5

    def test_non_english_chars(self):
        assert count_vowels("Привет мир!") == 0  # Кириллица
        assert count_vowels("こんにちは") == 0  # Японские иероглифы




if __name__ == '__main__':
   unittest.main()
