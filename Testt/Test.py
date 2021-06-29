import unittest
import errno


class UnitTest_Assignment(unittest.TestCase):
    # AssertTrue
    def test_positive(self):
        testValue = True
        message = "Test value is not true."
        self.assertTrue(testValue, message)

    # assert Greater
    def test_positiveForGreater(self):
        first = 5
        second = 2
        message = "first value is not greater that second value."
        self.assertGreater(first, second, message)

    # assert equal
    def test_negative(self):
        firstValue = "Srikanth"
        secondValue = "Srikanth"
        message = "First value and second value are not equal !"
        self.assertEqual(firstValue, secondValue, message)

    # assert Raises
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')
