from project.student_report_card import StudentReportCard
import unittest

class TestStudentReportCard(unittest.TestCase):
    def setUp(self) -> None:
        self.student_card = StudentReportCard("Pesho", 6)

    def test_init(self):
        self.assertEqual("Pesho", self.student_card.student_name)
        self.assertEqual(6, self.student_card.school_year)
        self.assertEqual({}, self.student_card.grades_by_subject)
        self.student_card.grades_by_subject = {"Python": [6.00], "Java": [4.63], "C++": [5.18]}
        self.assertEqual({"Python": [6.00], "Java": [4.63], "C++": [5.18]}, self.student_card.grades_by_subject)

    def test_name(self):
        with self.assertRaises(ValueError) as ve:
            self.student_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))
        self.student_card.student_name = "a"
        self.assertEqual("a", self.student_card.student_name)

    def test_school_year(self):
        with self.assertRaises(ValueError) as ve:
            self.student_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))
        self.student_card.school_year = 1
        self.assertEqual(1, self.student_card.school_year)
        self.student_card.school_year = 12
        self.assertEqual(12, self.student_card.school_year)


    def test_school_year_more_than_twelve(self):
        with self.assertRaises(ValueError) as ve:
            self.student_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade(self):
        self.student_card.grades_by_subject = {"Python": [6.00], "Java": [4.63], "C++": [5.18]}
        self.student_card.add_grade("HTML", 5.78)
        self.assertEqual({"Python": [6.00], "Java": [4.63], "C++": [5.18], "HTML": [5.78]}, self.student_card.grades_by_subject)
        self.student_card.add_grade("HTML", 5.63)
        self.assertEqual({"Python": [6.00], "Java": [4.63], "C++": [5.18], "HTML": [5.78, 5.63]},
                         self.student_card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student_card.grades_by_subject = {"Python": [6.00], "Java": [4.63], "C++": [5.18]}
        self.assertEqual("Python: 6.00\nJava: 4.63\nC++: 5.18", self.student_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.student_card.grades_by_subject = {"Python": [6.00], "Java": [4.63], "C++": [5.18]}
        self.assertEqual("Average Grade: 5.27", self.student_card.average_grade_for_all_subjects())

    def test__repr__(self):
        self.student_card.grades_by_subject = {"Python": [6.00], "Java": [4.63], "C++": [5.18]}
        self.assertEqual("Name: Pesho\nYear: 6\n----------\nPython: 6.00\nJava: 4.63\nC++: 5.18\n----------\nAverage Grade: 5.27", str(self.student_card))


if __name__ == "__main__":
    unittest.main()
