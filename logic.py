from PyQt6.QtWidgets import *
from Project1_gui import *
import csv



class Logic(QMainWindow,Ui_MainWindow):
    """
    A class representing storing functions that collect and store grade data to a csv file
    """
    def __init__(self) -> None:
        """
        Method to set default values of playlist and connect gui buttons to logic
        """
        super().__init__()
        self.setupUi(self)
        self.Test1_input.setVisible(False)
        self.Test2_input.setVisible(False)
        self.Test3_input.setVisible(False)
        self.Test4_input.setVisible(False)

        self.Submit_button.clicked.connect(lambda: self.submit())

    def num_boxes(self, num_attempts: int) -> bool:
        """
        Method to display number of input boxes based on number of attempts
        :param num_attempts: Input from number of attempts box
        :return: Validity of input (True/False)
        """
        if 0 < num_attempts < 5:
            self.Attempts_error.setText('')
            self.Test1.setText('Test 1')
            self.Test1_input.setVisible(True)
            if num_attempts >= 2:
                self.Test2.setText('Test 2')
                self.Test2_input.setVisible(True)
            if num_attempts >= 3:
                self.Test3.setText('Test 3')
                self.Test3_input.setVisible(True)
            if num_attempts == 4:
                self.Test4.setText('Test 4')
                self.Test4_input.setVisible(True)
            return True
        else:
            self.Attempts_error.setText('Please enter a value from 1-4')
            return False

    def check_name(self, name_input: str) -> bool:
        """
        Method to verify that name input is not an empty string
        :param name_input: input from student name box
        :return: Validity of name input (True/False)
        """
        if not name_input:
            self.Name_error.setText('Please enter student name')
            return False
        else:
            self.Name_error.setText('')
            return True
    def check_score(self, test_input: str) -> int:
        """
        Method to determine if test score input is a number and between 1-100
        :param test_input: Test score taken from input box
        :return: corrected test score (if invalid, score is 0)
        """
        test_input  = (test_input.strip())
        if not test_input:
            return 0
        if test_input.isdigit():
            test_input = int(test_input)
            if test_input < 0 or test_input > 100:
                return 0
            else:
                return test_input
    def calculate_final(self, test1: int, test2: int, test3: int, test4: int) -> int:
        """
        Method to calculate the highest score, which is the final grade
        :param test1: Test 1 input from gui
        :param test2: Test 2 input from gui
        :param test3: Test 3 input from gui
        :param test4: Test 4 input from gui
        :return: Highest score
        """
        test_scores = [test1, test2, test3, test4]
        high_score = max(test_scores)
        return high_score
    def calculate_letter_grade(self, final: int) -> str:
        """
        Method to determine letter grade
        :param final: highest score
        :return: letter grade
        """
        if 100 >= final >= 90:
            grade = 'A'
        elif final >= 80:
            grade = 'B'
        elif final >= 70:
            grade = 'C'
        elif final >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return grade
    def write(self, student_name:str, num_attempts: int, input_test1: int, input_test2: int,
              input_test3: int, input_test4: int, final_score: int, letter_grade: str) -> None:
        """
        Method to write grade data to a csv file
        :param student_name: Data from student name input box
        :param num_attempts: Data from number of attempts input box
        :param input_test1: Test 1 input
        :param input_test2: Test 2 input
        :param input_test3: Test 3 input
        :param input_test4: Test 4 input
        :param final_score: Calculated highest score
        :param letter_grade: Calculated letter grade
        """

        with open('grades.csv', 'a', newline='') as file:
            content = csv.writer(file)
            content.writerow([student_name, num_attempts, input_test1, input_test2,
                              input_test3, input_test4, final_score, letter_grade])


    def submit(self) -> None:
        """
        Method to display submit messages and ensure that the data is written to the file after scores are input
        """
        student_name = self.Name_input.text().strip()
        num_attempts = int(self.Num_attempts_input.text().strip())

        if not self.check_name(student_name):
            return
        if not self.num_boxes(num_attempts):
            return

        input_test1 = self.check_score(self.Test1_input.text())
        input_test2 = self.check_score(self.Test2_input.text())
        input_test3 = self.check_score(self.Test3_input.text())
        input_test4 = self.check_score(self.Test4_input.text())

        final_score = self.calculate_final(input_test1, input_test2, input_test3, input_test4)
        letter_grade = self.calculate_letter_grade(final_score)

        if num_attempts == 1 and input_test1 !=0:
            self.write(student_name, num_attempts, input_test1, input_test2,
                       input_test3, input_test4, final_score, letter_grade)
            self.Submit_message.setText('SUBMITTED')
        elif num_attempts == 2 and input_test1 != 0 and input_test2 != 0:
            self.write(student_name, num_attempts, input_test1, input_test2,
                       input_test3, input_test4, final_score, letter_grade)
            self.Submit_message.setText('SUBMITTED')
        elif num_attempts == 3 and input_test1 != 0 and input_test2 != 0 and input_test3 != 0:
            self.write(student_name, num_attempts, input_test1, input_test2,
                       input_test3, input_test4, final_score, letter_grade)
            self.Submit_message.setText('SUBMITTED')
        elif num_attempts == 4 and input_test1 != 0 and input_test2 != 0 and input_test3 != 0 and input_test4 != 0:
            self.write(student_name, num_attempts, input_test1, input_test2,
                       input_test3, input_test4, final_score, letter_grade)
            self.Submit_message.setText('SUBMITTED')
        else:
            self.Submit_message.setText('Please enter a number 1-100 in test score boxes')





