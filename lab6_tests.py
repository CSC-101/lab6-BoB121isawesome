import data
import lab6
import unittest

from lab6 import selection_sort_books


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books(self):
        book1 = data.Book(["J.K. Rowling"],"Harry Potter")
        book2 = data.Book(["Paulo Coelho"],"The Alchemist")
        book3 = data.Book(["Ray Bradbury"],"Fahrenheit 451")

        book_list = [book1, book2, book3]
        expected = [book3, book1, book2]
        self.assertEqual(expected, lab6.selection_sort_books(book_list))

    def test_selection_sort_books_2(self):
        book1 = data.Book(["J.K. Rowling"],"abcdef")
        book2 = data.Book(["Paulo Coelho"],"aabcdef")
        book3 = data.Book(["Ray Bradbury"],"acbderf")

        book_list = [book1, book2, book3]
        expected = [book2, book1, book3]
        self.assertEqual(expected, lab6.selection_sort_books(book_list))

    # Part 2
    def test_swap_case(self):
        expected = "heLlO fRiEndS, I Am FrIEndLY"
        input = "HElLo FrIeNDs, i aM fRieNDly"
        self.assertEqual(expected, lab6.swap_case(input))

    def test_swap_case_2(self):
        expected = "i lIEd, i aM NOt FRieNdLy"
        input = "I LieD, I Am noT frIEnDlY"
        self.assertEqual(expected, lab6.swap_case(input))

    # Part 3
    def test_str_translate(self):
        expected="xbcdcbx"
        self.assertEqual(expected, lab6.str_translate('abcdcba', 'a', 'x'))

    def test_str_translate2(self):
        expected="mippippippi"
        self.assertEqual(expected, lab6.str_translate('mississippi', 's', 'p'))

    # Part 4
    def test_histogram(self):
        expected={'burritos': 1, 'i': 2, 'love': 2, 'tacos,': 1}
        input="i love tacos, i love burritos"
        self.assertEqual(expected, lab6.histogram(input))

    def test_histogram_2(self):
        expected={'hello': 2, 'said': 2, 'she': 1, 'then': 1, 'he': 1}
        input="she said hello then he said hello"
        self.assertEqual(expected, lab6.histogram(input))


if __name__ == '__main__':
    unittest.main()
