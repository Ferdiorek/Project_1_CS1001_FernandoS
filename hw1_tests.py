"""CSC 1001 - Programming Assignment 1: student-written unit tests.

Create at least TWO separate, meaningful unit tests for each function.
The sixteen methods below are ONLY PLACEHOLDERS: they are not real tests.

Replace each self.fail(...) with test inputs, a call to the appropriate
hw1 function, and unittest assertions about its expected output.
Use methods like self.assertEqual(...) or self.assertAlmostEqual(...).

IMPORTANT: The initial test failures are intentional until you write tests
and implement the functions in hw1.py. Do not simply delete the tests.
"""

import unittest

import data
import hw1
import math

class TestHomework1(unittest.TestCase):

    # Part 1: vowel_count
    def test_vowel_count_case_insensitive(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count("taco"), 2)

    def test_vowel_count_empty_string(self):
        # TODO: Arrange inputs, call hw1.vowel_count, and assert the result.
        self.assertEqual(hw1.vowel_count(""), 0)

    # Part 2: short_lists
    def test_short_lists_mixed_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([[1], [2,3],[],[4,5,6]]), [[2,3]])

    def test_short_lists_no_matching_lengths(self):
        # TODO: Arrange inputs, call hw1.short_lists, and assert the result.
        self.assertEqual(hw1.short_lists([[]]), [])

    # Part 3: ascending_pairs
    def test_ascending_pairs_reversed_pairs(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs([[9, 2], [3, 1, 2], [5, 5]]),[[2, 9], [3, 1, 2], [5, 5]])

    def test_ascending_pairs_other_lengths_unchanged(self):
        # TODO: Arrange inputs, call hw1.ascending_pairs, and assert the result.
        self.assertEqual(hw1.ascending_pairs([]), [])

    # Part 4: add_prices
    def test_add_prices_no_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(5,0),data.Price(2,50)),data.Price(7,50))

    def test_add_prices_with_cents_carry(self):
        # TODO: Arrange inputs, call hw1.add_prices, and assert the result.
        self.assertEqual(hw1.add_prices(data.Price(3,75),data.Price(4,50)),data.Price(8,25))
    # Part 5: rectangle_area
    def test_rectangle_area_standard_rectangle(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(3,2),data.Point(0,1))),3)

    def test_rectangle_area_negative_coordinates(self):
        # TODO: Arrange inputs, call hw1.rectangle_area, and assert the result.
        self.assertEqual(hw1.rectangle_area(data.Rectangle(data.Point(-3,-3),data.Point(-3,-3))),0)

    # Part 6: books_by_author
    def test_books_by_author_matching_authors(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        library = [data.Book(['Neil Gaiman', 'Terry Pratchett'], 'Good Omens'),
                   data.Book(["Darren Shan"], "Cirque Du Freak"),
                   data.Book(["Michael Crichton"], 'Jurassic Park')]

        self.assertEqual(hw1.books_by_author("Darren Shan", library),[data.Book(["Darren Shan"], "Cirque Du Freak")])

    def test_books_by_author_no_matches(self):
        # TODO: Arrange inputs, call hw1.books_by_author, and assert the result.
        self.assertEqual(hw1.books_by_author("Darren Shan", []),[])
    # Part 7: circle_bound
    def test_circle_bound_square(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        new_rect = data.Rectangle(data.Point(0,5),data.Point(5,0))
        self.assertEqual(hw1.circle_bound(new_rect), data.Circle(data.Point(2.5,2.5), math.sqrt(50)/2 ))


    def test_circle_bound_non_square_rectangle(self):
        # TODO: Arrange inputs, call hw1.circle_bound, and assert the result.
        new_rect = data.Rectangle(data.Point(3, 7), data.Point(5, 1))
        self.assertEqual(hw1.circle_bound(new_rect), data.Circle(data.Point(1,3), math.sqrt(40)/2))

    # Part 8: below_pay_average
    def test_below_pay_average_different_pay_rates(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        employee1 = data.Employee('Brendon', 20)
        employee2 = data.Employee('Queona', 23)
        employee3 = data.Employee('Samantha', 50)
        employee4 = data.Employee('Edwin', 0)
        employees = [employee1, employee2, employee3, employee4]
        self.assertEqual(hw1.below_pay_average(employees),["Brendon","Queona","Edwin"])

    def test_below_pay_average_empty_list(self):
        # TODO: Arrange inputs, call hw1.below_pay_average, and assert the result.
        self.assertEqual(hw1.below_pay_average([]),[])


if __name__ == '__main__':
    unittest.main()
