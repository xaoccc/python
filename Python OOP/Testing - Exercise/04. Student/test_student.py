from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("John")

    def test_init(self):
        self.assertEqual(self.student.name, "John")
        self.assertEqual(self.student.courses, {})
        self.student.courses = {"Physics": ["It is very hard"], "Java": []}
        self.assertEqual(self.student.courses, {"Physics": ["It is very hard"], "Java": []})

    def test_enroll(self):
        student = Student("John", {"Physics": ["It is very hard"], "Java": []})
        # testing course_name in self.courses.keys()
        self.assertEqual("Course already added. Notes have been updated.", student.enroll("Physics", ["I have to study more"], ""))
        # testing if notes in course_name are updated
        self.assertEqual(['It is very hard', 'I have to study more'], student.courses["Physics"])
        # testing add_course_notes == ""
        self.assertEqual("Course and course notes have been added.", student.enroll("Javascript", ["I love React"]))
        # testing add_course_notes == "Y"
        self.assertEqual("Course and course notes have been added.", student.enroll("HTML", ["I love web"], "Y"))
        # testing add new course
        self.assertEqual("Course has been added.", student.enroll("C++", ["aaa"], "bbb"))
        # testing add new course has empty list as notes
        self.assertEqual([], student.courses["C++"])

    def test_add_notes_return_updated(self):
        self.student.courses = {"Physics": ["It is very hard"], "Java": []}
        self.assertEqual("Notes have been updated", self.student.add_notes("Physics", ["It is easy"]))

    def test_add_notes_check_notes(self):
        self.student.courses = {"Physics": ["It is very hard"], "Java": []}
        self.student.add_notes("Physics", "It is easy")
        self.assertEqual(["It is very hard", "It is easy"], self.student.courses["Physics"])

    def test_add_notes_no_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("History", "It is easy")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_no_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("History")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_available_course_return_message(self):
        student = Student("John", {"Physics": ["It is very hard"], "Java": []})
        self.assertEqual("Course has been removed", student.leave_course("Physics"))

    def test_leave_available_course_check_if_removed_from_courses(self):
        student = Student("John", {"Physics": ["It is very hard"], "Java": []})
        student.leave_course("Physics")
        self.assertEqual({'Java': []}, student.courses)


if __name__ == "__main__":
    unittest.main()