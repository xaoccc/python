from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_init(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit(self):
        with self.assertRaises(ValueError) as valer:
            self.bookstore.books_limit = -1
        self.assertEqual("Books limit of -1 is not valid", str(valer.exception))

    def test_books_limit_edge_case(self):
        with self.assertRaises(ValueError) as valer:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(valer.exception))

    def test_books_limit_valid_edge_case(self):
        self.bookstore.books_limit = 1
        self.assertEqual(1, self.bookstore.books_limit)

    def test__len__books_number(self):
        self.assertEqual(0, len(self.bookstore))
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        self.assertEqual(56, len(self.bookstore))

    def test_receive_book_not_enough_place_edge_case(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 20, "Pooh Bear": 31}
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Pod Igoto", 50)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_enough_place(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        self.bookstore.receive_book("Pod Igoto", 20)
        self.assertEqual({"Pinocchio": 25, "Pooh Bear": 31, "Pod Igoto": 20}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(76, len(self.bookstore))
        self.assertEqual("3 copies of It are available in the bookstore.",
                         self.bookstore.receive_book("It", 3))
        self.assertEqual({"Pinocchio": 25, "Pooh Bear": 31, "Pod Igoto": 20, "It": 3},
                         self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(79, self.bookstore.__len__())
        self.assertEqual("21 copies of Judge is Hell are available in the bookstore.",
                         self.bookstore.receive_book("Judge is Hell", 21))
        self.assertEqual({"Pinocchio": 25, "Pooh Bear": 31, "Pod Igoto": 20, "It": 3, "Judge is Hell": 21},
                         self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(100, self.bookstore.__len__())

    def test_receive_book_same_book_twice_enough_place(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        self.assertEqual("45 copies of Pinocchio are available in the bookstore.",
                         self.bookstore.receive_book("Pinocchio", 20))
        self.assertEqual(76, self.bookstore.__len__())


    def test_sell_book_no_such_book(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("It", 5)
        self.assertEqual("Book It doesn't exist!", str(ex.exception))

    def test_sell_book_not_enough_book_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Pinocchio", 35)
        self.assertEqual("Pinocchio has not enough copies to sell. Left: 25", str(ex.exception))

    def test_sell_book_valid(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        self.assertEqual("Sold 12 copies of Pinocchio",
                         self.bookstore.sell_book("Pinocchio", 12))
        self.assertEqual(12, self.bookstore.total_sold_books)
        self.assertEqual(44, self.bookstore.__len__())
        self.assertEqual("Sold 11 copies of Pooh Bear",
                         self.bookstore.sell_book("Pooh Bear", 11))
        self.assertEqual(23, self.bookstore.total_sold_books)
        self.assertEqual(33, self.bookstore.__len__())


    def test_str(self):
        self.bookstore.availability_in_store_by_book_titles = {"Pinocchio": 25, "Pooh Bear": 31}
        self.bookstore.sell_book("Pinocchio", 12)
        self.bookstore.sell_book("Pooh Bear", 11)
        self.assertEqual("Total sold books: 23\nCurrent availability: 33\n - Pinocchio: 13 copies\n - Pooh Bear: 20 copies", str(self.bookstore))
        self.bookstore.sell_book("Pinocchio", 13)
        self.bookstore.sell_book("Pooh Bear", 20)
        self.assertEqual("Total sold books: 56\nCurrent availability: 0\n - Pinocchio: 0 copies\n - Pooh Bear: 0 copies", str(self.bookstore))


if __name__ == "__main__":
    unittest.main()

