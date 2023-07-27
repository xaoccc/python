from project.library import Library
import unittest


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("Bookhouse")

    def test_init(self):
        self.assertEqual("Bookhouse", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name(self):
        with self.assertRaises(ValueError) as valer:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(valer.exception))

    def test_add_book(self):
        self.library.books_by_authors = {"Isaac Asimov": ["I, Robot"]}
        self.library.add_book("Isaac Asimov", "I, Robot")
        self.assertEqual({"Isaac Asimov": ["I, Robot"]}, self.library.books_by_authors)
        self.library.add_book("Isaac Asimov", "Foundation")
        self.assertEqual({"Isaac Asimov": ["I, Robot", "Foundation"]}, self.library.books_by_authors)
        self.library.add_book("Robert A. Heinlein", "Stranger in a Strange Land")
        self.assertEqual({"Isaac Asimov": ["I, Robot", "Foundation"], "Robert A. Heinlein": ["Stranger in a Strange Land"]}, self.library.books_by_authors)

    def test_add_reader(self):
        self.library.readers = {"Ivan": []}
        self.assertEqual("Ivan is already registered in the Bookhouse library.", self.library.add_reader("Ivan"))
        self.assertEqual({"Ivan": []}, self.library.readers)
        self.library.add_reader("Pencho ne chete")
        self.assertEqual({"Ivan": [], "Pencho ne chete": []}, self.library.readers)

    def test_rent_book_no_reader(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Isaac Asimov": ["I, Robot"]}
        self.assertEqual(f"Peter is not registered in the Bookhouse Library.", self.library.rent_book("Peter", "Isaac Asimov", "I, Robot"))
        self.assertEqual({"Ivan": []}, self.library.readers)
        self.assertEqual({"Isaac Asimov": ["I, Robot"]}, self.library.books_by_authors)

    def test_rent_book_no_author(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Isaac Asimov": ["I, Robot"]}
        self.assertEqual("Bookhouse Library does not have any Robert A. Heinlein's books.",
                         self.library.rent_book("Ivan", "Robert A. Heinlein", "Stranger in a Strange Land"))
        self.assertEqual({"Ivan": []}, self.library.readers)
        self.assertEqual({"Isaac Asimov": ["I, Robot"]}, self.library.books_by_authors)

    def test_rent_book_no_book(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Isaac Asimov": ["I, Robot"]}
        self.assertEqual("""Bookhouse Library does not have Isaac Asimov's "Foundation".""",
                         self.library.rent_book("Ivan", "Isaac Asimov", "Foundation"))
        self.assertEqual({"Ivan": []}, self.library.readers)
        self.assertEqual({"Isaac Asimov": ["I, Robot"]}, self.library.books_by_authors)

    def test_rent_book(self):
        self.library.readers = {"Ivan": []}
        self.library.books_by_authors = {"Isaac Asimov": ["I, Robot"]}
        self.library.rent_book("Ivan", "Isaac Asimov", "I, Robot")
        self.assertEqual({"Ivan": [{"Isaac Asimov": "I, Robot"}]}, self.library.readers)
        self.assertEqual({'Isaac Asimov': []}, self.library.books_by_authors)


if __name__ == "__main__":
    unittest.main()



