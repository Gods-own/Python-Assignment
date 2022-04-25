import math
import sys

class Student:
    def __init__(self, scores):
        self.scores = scores

    def get_score_list(self):
        list_scores = self.scores.split(",")
        list_scores = [float(i) for i in list_scores]
        return list_scores

    def finalMark(self):
        sum_of_assessments = math.ceil(self.get_score_list()[0] * 0.2 + self.get_score_list()[1] * 0.4 + self.get_score_list()[2] * 0.4)
        return sum_of_assessments


class BITStudent(Student):
    def __init__(self, scores, mark):
        super().__init__(scores)
        self.mark = mark

    def gradeLetter(self):
        if 100 >= self.mark and self.mark  >= 85:
            grade = "HD"
            return grade
        elif 84 >= self.mark  and self.mark  >= 75:
            grade = "D"   
            return grade
        elif 74 >= self.mark  and self.mark  >= 65:
            grade = "C"   
            return grade
        elif 64 >= self.mark  and self.mark  >= 50:
            grade = "P"   
            return grade 
        elif 49 >= self.mark  and self.mark  >= 45:
            b = 0
            for y in self.get_score_list():
                if y < 50:
                    b = b + 1
                else:
                    continue

            if 0 in self.get_score_list() or b >= 2:
                grade = "F"
                return grade  
            elif 0 not in self.get_score_list() and self.get_score_list()[2] < 50:
                grade = "SE"
                return grade
            elif 0 not in self.get_score_list() and self.get_score_list()[0] < 50 or self.get_score_list()[1] < 50:
                grade = "SA"
                return grade  
        
        elif 44 >= self.mark and self.mark >= 0:
            a = 0
            for x in self.get_score_list():
                if x == 0:
                    a = a + 1
                else:
                    continue
            if a >= 2:            
                grade = "AF"   
                return grade  
            else:
                grade = "F"                  
                return grade  

    def gradePoint(self, grade):
        if grade == "HD":
            point_value = 4.0
            return point_value
        elif grade == "D":
            point_value = 3.0 
            return point_value
        elif grade == "C":
            point_value = 2.0 
            return point_value        
        elif grade == "P":
            point_value = 1.0  
            return point_value 
        elif grade == "SP":
            point_value = 0.5 
            return point_value  
        elif grade == "F":
            point_value = 0  
            return point_value    

    def gradeLetterFinal(self, Supplementary_score): 
            if Supplementary_score >= 50:
                gradeLetter = "SP"
                return gradeLetter
            elif Supplementary_score < 50: 
                gradeLetter = "F" 
                return gradeLetter        


class DITStudent(Student):                 
    def __init__(self, scores, mark):
        super().__init__(scores)
        self.mark = mark

    def gradeLetter(self):
        if 100 >= self.mark and self.mark  >= 50:
            grade = "CP"
            return grade
        elif 49 >= self.mark  and self.mark  >= 0:
            grade = "NYC"   
            return grade

    def gradePoint(self, grade):
        if grade == "CP":
            point_value = 4.0
            return point_value
        elif grade == "NC":
            point_value = 0 
            return point_value

    def gradeLetterFinal(self, resubmission): 
            if Supplementary_score >= 50:
                gradeLetter = "CP"
                return gradeLetter
            if Supplementary_score < 50:
                gradeLetter = "NC"
                return gradeLetter    

class StudentInfo:
    def __init__(self, studentID, name, studentType, assessments, gradeLetter, gradePoint, totalMark, gradeLetterFinal):
        self.studentID = studentID
        self.name = name
        self.studentType = studentType
        self.assessments = assessments
        self.gradeLetter = gradeLetter
        self.gradePoint = gradePoint
        self.totalMark = totalMark
        self.gradeLetterFinal = gradeLetterFinal

    def studentPerformance(self):
        student_Info = {
            "studentID": self.studentID,
            "name": self.name,
            "studentType": self.studentType,
            "assessments": self.assessments,
            "gradeLetter": self.gradeLetter,
            "gradePoint": self.gradePoint,
            "totalMark": self.totalMark,
            "gradeLetterFinal": self.gradeLetterFinal
        }   
        return student_Info

student_scores = []        

menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

if menu not in [1,2,3,4]:
    sys.exit("Please enter a whole number between 1 and 4")

if menu == 1:
    option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
    
    if option1 not in [1.1,1.2,1.3]:
        sys.exit("Please select a valid option")

while True:  

    while True:
            
        if option1 == 1.1:
            student_type = "BIT"
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_assessment = input("Enter student assessment marks (separated by comma): ")
            final_mark = Student(student_assessment).finalMark()
            bitStudent = BITStudent(student_assessment, final_mark)
            grade_letter = bitStudent.gradeLetter()
            grade_letter_final = grade_letter
            grade_point = bitStudent.gradePoint(grade_letter)

            if grade_letter == "SA" or grade_letter == "SE":
                Supplementary_score = int(input("What is this student's supplementary exam mark: "))
                grade_letter_final = bitStudent.gradeLetterFinal(Supplementary_score)
                grade_point = bitStudent.gradePoint(grade_letter_final) 
            elif grade_letter == "AF":
                grade_letter_final = "F"   
                grade_point = bitStudent.gradePoint(grade_letter_final)      
            
            student_ee = StudentInfo(student_id, student_name, student_type, student_assessment, grade_letter, grade_point, final_mark, grade_letter_final)
            student_scores.append(student_ee.studentPerformance())  

        elif option1 == 1.2:   
            student_type = "DIT"
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_assessment = input("Enter student assessment marks (separated by comma): ")
            final_mark = Student(student_assessment).finalMark()
            ditStudent = DITStudent(student_assessment, final_mark)
            grade_letter = ditStudent.gradeLetter()
            grade_point = ditStudent.gradePoint(grade_letter)  
            grade_letter_final = grade_letter 

            if grade_letter == "NYC":
                resubmission = input("What is this student's resubmission mark: ") 
                Supplementary_score = Student(resubmission).finalMark() 
                grade_letter_final = ditStudent.gradeLetterFinal(Supplementary_score)   
                grade_point = ditStudent.gradePoint(grade_letter_final) 
            
            student_ee = StudentInfo(student_id, student_name, student_type, student_assessment, grade_letter, grade_point, final_mark, grade_letter_final)
            student_scores.append(student_ee.studentPerformance())  

        elif option1 == 1.3:
            print(student_scores)
            continue

        option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
    
        if option1 not in [1.1,1.2,1.3]:
            sys.exit("Please select a valid option")

    menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

    if menu not in [1,2,3,4]:
        sys.exit("Please enter a whole number between 1 and 4")

    if menu == 1:
        option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
        
        if option1 not in [1.1,1.2,1.3]:
            sys.exit("Please select a valid option")              
            
        
elif menu == 4:
    sys.exit("Program exited")    


# while True:
#     slected_students_scores = []

# scores = input("Enter score: ")
# sic = Student(scores)

# mark = sic.finalMark()

# sib = BITStudent(scores, mark)
# sid = DITStudent(scores, mark)

# print(sib.gradeLetter())
# print(sib.gradePoint())
# print(sid.gradeLetter())
# print(sid.gradePoint())

# kk = StudentInfo("A98766569", "mary djdj", "BIT", [100,36,50], "SE", 4.0, 74, "SP")

# print(kk.studentPerformance())