import unittest
from to_test import Student

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.no_student = Student()
        self.bad_student = Student()
        self.good_student = Student()
        
    def tearDown(self):
        self.no_student = None
        self.bad_student = None
        self.good_student = None
        
        
class TestNoStudent(StudentTestCase):
    def runTest(self):
        self.assertEqual(self.no_student.grades, [])
        
        
class TestAddGrade(StudentTestCase):
    def runTest(self):
        self.no_student.add_grade(50)
        self.assertEqual(self.no_student.grades, [50])
        self.no_student.add_grade(60)
        self.assertEqual(self.no_student.grades, [50, 60])
      
    
class TestBoostGrades(StudentTestCase):
    def runTest(self):
        self.no_student.boost_grades()
        self.assertEqual(self.no_student.grades, [])
        
        self.bad_student.add_grade(0)
        self.bad_student.boost_grades()
        self.assertEqual(self.bad_student.grades, [10])
        
        self.good_student.add_grade(99)
        self.good_student.boost_grades()
        self.assertEqual(self.good_student.grades, [100])
        self.good_student.add_grade(99)
        self.good_student.boost_grades()
        self.assertEqual(self.good_student.grades, [100, 100])
     
    
class TestRaiseExceptions(StudentTestCase):
    def runTest(self):
        with self.assertRaises(ValueError):          
            self.bad_student.add_grade(-1)
            self.good_student.add_grade(101)
        
        
    

if __name__ == '__main__':
    unittest.main()