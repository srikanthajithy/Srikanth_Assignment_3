import Test
import Login
import Caluclation


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    Test.UnitTest_Assignment().test_positive()
    Test.UnitTest_Assignment().test_positiveForGreater()
    Test.UnitTest_Assignment().test_negative()
    Test.UnitTest_Assignment().test_file_not_found()
    Caluclation.Cal()
