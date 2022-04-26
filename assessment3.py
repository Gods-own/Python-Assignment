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

    def gradeLetterFinal(self, Supplementary_score ): 
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

class Option1:

    def option11(self):  
        student_type = "BIT"
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_assessment = input("Enter student assessment marks (separated by comma): ")
        student_assessment_list = Student(student_assessment).get_score_list()
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
        
        student_ee = StudentInfo(student_id, student_name, student_type, student_assessment_list, grade_letter, grade_point, final_mark, grade_letter_final)
        student_scores.append(student_ee.studentPerformance())    

    def option12(self):     
        student_type = "DIT"
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_assessment = input("Enter student assessment marks (separated by comma): ")
        student_assessment_list = Student(student_assessment).get_score_list()
        final_mark = Student(student_assessment).finalMark()
        ditStudent = DITStudent(student_assessment, final_mark)
        grade_letter = ditStudent.gradeLetter()
        grade_point = ditStudent.gradePoint(grade_letter)  
        grade_letter_final = grade_letter 

        if grade_letter == "NYC":
            resubmission = input("What is this student's resubmission mark: ") 
            Supplementary_score = Student(resubmission).finalMark() 
            student_assessment = resubmission
            student_assessment_list = Student(student_assessment).get_score_list()
            grade_letter_final = ditStudent.gradeLetterFinal(Supplementary_score)   
            grade_point = ditStudent.gradePoint(grade_letter_final) 
        
        student_ee = StudentInfo(student_id, student_name, student_type, student_assessment_list, grade_letter, grade_point, final_mark, grade_letter_final)
        student_scores.append(student_ee.studentPerformance())    
  

class Option2:

    def option21(self):  
        sorted_student_scores = sorted(student_scores, key=lambda d: d['totalMark'], reverse=True)
        for dic in sorted_student_scores:
            print(f"{dic['studentID']} \t {dic['name']} \t {dic['studentType']} \t {dic['totalMark']} \t {dic['gradeLetterFinal']} \n")   

    def option22(self):     
        sorted_student_scores = sorted(student_scores, key=lambda d: d['totalMark'])
        for dic in sorted_student_scores:
            print(f"{dic['studentID']} \t {dic['name']} \t {dic['studentType']} \t {dic['totalMark']} \t {dic['gradeLetterFinal']} \n")     

class Option3:

    def no_students(self):  
        no_of_students = len(student_scores)
        return no_of_students

    def no_BIT_students(self):     
        bit_count = 0
        for dic in student_scores:
            if dic["studentType"] == "BIT":
                bit_count = bit_count + 1
        return bit_count  

    def no_DIT_students(self):     
        dit_count = 0
        for dic in student_scores:
            if dic["studentType"] == "DIT":
                dit_count = dit_count + 1
        return dit_count

    def no_each_grade(self):
        no_HD = 0
        no_D = 0
        no_C = 0
        no_P = 0
        no_SP = 0
        no_CP = 0
        no_F = 0
        no_AF = 0

        for dic in student_scores:
            if dic["gradeLetterFinal"] == "HD":
                no_HD += 1
            elif dic["gradeLetterFinal"] == "D":
                no_D += 1
            elif dic["gradeLetterFinal"] == "C":
                no_C += 1
            elif dic["gradeLetterFinal"] == "P":
                no_P += 1
            elif dic["gradeLetterFinal"] == "SP":
                no_SP += 1
            elif dic["gradeLetterFinal"] == "CP":
                no_CP += 1  
            elif dic["gradeLetterFinal"] == "F":
                no_F += 1      
            elif dic["gradeLetter"] == "AF":
                no_AF += 1   

        total_HD_D_C_P_SP_CP = no_HD + no_D + no_C + no_P + no_SP + no_CP    

        gradeInfo = {
            "total_No_Of_Pass_Grade": total_HD_D_C_P_SP_CP,
            "total_No_Of_HD_Grade" : no_HD,
            "total_No_Of_D_Grade" : no_D,
            "total_No_Of_C_Grade" : no_C,
            "total_No_Of_P_Grade" : no_P,
            "total_No_Of_SP_Grade" : no_SP,
            "total_No_Of_CP_Grade" : no_CP,
            "total_No_Of_F_Grade" : no_F,
            "total_No_Of_AF_Grade" : no_AF
        } 

        return gradeInfo

    def student_pass_rate(self):
        number_of_students = self.no_students()
        total_No_Of_Pass_Grade = self.no_each_grade()["total_No_Of_Pass_Grade"]
        pass_rate = round(((total_No_Of_Pass_Grade)/number_of_students) * 100, 2)
        return pass_rate

    def student_pass_rate_adj(self):
        number_of_students = self.no_students()
        total_No_Of_Pass_Grade = self.no_each_grade()["total_No_Of_Pass_Grade"]
        total_No_Of_AF_Grade = self.no_each_grade()["total_No_Of_AF_Grade"]
        pass_rate_adj = round(((total_No_Of_Pass_Grade)/(number_of_students - total_No_Of_AF_Grade)) * 100, 2)
        return pass_rate_adj

    def avg_assessment1(self):
        total_asse1 = 0
        number_of_students = self.no_students()

        for dic in student_scores:
            total_asse1 = total_asse1 + dic["assessments"][0]
        avg_mark1 = round(total_asse1/number_of_students, 2)

        return avg_mark1

    def avg_assessment2(self):
        total_asse2 = 0
        number_of_students = self.no_students()

        for dic in student_scores:
            total_asse2 = total_asse2 + dic["assessments"][1]

        avg_mark2 = round(total_asse2/number_of_students, 2)

        return avg_mark2

    def avg_assessment3(self):
        total_asse3 = 0
        number_of_students = self.no_students()

        for dic in student_scores:
            total_asse3 = total_asse3 + dic["assessments"][2]

        avg_mark3 = round(total_asse3/number_of_students, 2)

        return avg_mark3

    def avg_final(self):
        total_final = 0
        number_of_students = self.no_students()

        for dic in student_scores:
            total_final = total_final + dic["totalMark"]

        avg_markFinal = round(total_final/number_of_students, 2)

        return avg_markFinal

    def avg_grade_point(self):
        total_grade_point = 0
        number_of_students = self.no_students()

        for dic in student_scores:
            total_grade_point = total_grade_point + dic["gradePoint"]

        avg_gradePoint = round(total_grade_point/number_of_students, 1)

        return avg_gradePoint     

    def print_no_of_each_grade(self):
        no_HD = self.no_each_grade()["total_No_Of_HD_Grade"]
        no_D = self.no_each_grade()["total_No_Of_D_Grade"]
        no_C = self.no_each_grade()["total_No_Of_C_Grade"]
        no_P = self.no_each_grade()["total_No_Of_P_Grade"]
        no_SP = self.no_each_grade()["total_No_Of_SP_Grade"]
        no_CP = self.no_each_grade()["total_No_Of_CP_Grade"]
        no_F = self.no_each_grade()["total_No_Of_F_Grade"]

        print(no_HD)
        print(no_D)
        print(no_C)
        print(no_P)
        print(no_SP)
        print(no_CP)
        print(no_F)

    def print_opt3_ans(self):
        print(self.no_students())
        print(self.no_BIT_students())
        print(self.no_DIT_students())
        print(self.student_pass_rate())
        print(self.student_pass_rate_adj())
        print(self.avg_assessment1())
        print(self.avg_assessment2())
        print(self.avg_assessment3())
        print(self.avg_final())
        print(self.avg_grade_point())
        self.print_no_of_each_grade()





student_scores = []        

menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

if menu not in [1,2,3,4]:
    sys.exit("Please enter a whole number between 1 and 4")

while True:  

    if menu == 1:
        option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
    
        if option1 not in [1.1,1.2,1.3]:
            sys.exit("Please select a valid option")

        while True:
                
            if option1 == 1.1:
                option_one_of_one = Option1()
                option_one_of_one.option11() 

            elif option1 == 1.2:   
                option_one_of_two = Option1()
                option_one_of_two.option12() 

            elif option1 == 1.3:
                print(student_scores)
                break

            option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
        
            if option1 not in [1.1,1.2,1.3]:
                sys.exit("Please select a valid option")  
        
    elif menu == 2:    
        option2 = float(input(f"Choose one of the following options: \n 2.1 - Print all student grade information ascendingly by final mark\n 2.2 - Print all student grade information descendingly by final mark \n 2.3 - Go back to the main menu \n"))
        
        if option2 not in [2.1,2.2,2.3]:
            sys.exit("Please select a valid option")

        while True:    

            if option2 == 2.1:
                option_two_of_one = Option2()
                option_two_of_one.option21() 

            elif option2 == 2.2:
                option_two_of_two = Option2()
                option_two_of_two.option22() 

            elif option2 == 2.3:
                    print(student_scores)
                    break

            option2 = float(input(f"Choose one of the following options: \n 2.1 - Print all student grade information ascendingly by final mark\n 2.2 - Print all student grade information descendingly by final mark \n 2.3 - Go back to the main menu \n"))
        
            if option2 not in [2.1,2.2,2.3]:
                sys.exit("Please select a valid option")

            
    elif menu == 3:
        option_three = Option3()
        option_three.print_opt3_ans()
        
    elif menu == 4:
        sys.exit("Program exited")    

    menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

    if menu not in [1,2,3,4]:
        sys.exit("Please enter a whole number between 1 and 4")    


# student_scores = []        

# menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

# if menu not in [1,2,3,4]:
#     sys.exit("Please enter a whole number between 1 and 4")

# while True:  

#     if menu == 1:
#         option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
    
#         if option1 not in [1.1,1.2,1.3]:
#             sys.exit("Please select a valid option")

#         while True:
                
#             if option1 == 1.1:
#                 student_type = "BIT"
#                 student_id = input("Enter student ID: ")
#                 student_name = input("Enter student name: ")
#                 student_assessment = input("Enter student assessment marks (separated by comma): ")
#                 final_mark = Student(student_assessment).finalMark()
#                 bitStudent = BITStudent(student_assessment, final_mark)
#                 grade_letter = bitStudent.gradeLetter()
#                 grade_letter_final = grade_letter
#                 grade_point = bitStudent.gradePoint(grade_letter)

#                 if grade_letter == "SA" or grade_letter == "SE":
#                     Supplementary_score = int(input("What is this student's supplementary exam mark: "))
#                     grade_letter_final = bitStudent.gradeLetterFinal(Supplementary_score)
#                     grade_point = bitStudent.gradePoint(grade_letter_final) 
#                 elif grade_letter == "AF":
#                     grade_letter_final = "F"   
#                     grade_point = bitStudent.gradePoint(grade_letter_final)      
                
#                 student_ee = StudentInfo(student_id, student_name, student_type, student_assessment, grade_letter, grade_point, final_mark, grade_letter_final)
#                 student_scores.append(student_ee.studentPerformance())  

#             elif option1 == 1.2:   
#                 student_type = "DIT"
#                 student_id = input("Enter student ID: ")
#                 student_name = input("Enter student name: ")
#                 student_assessment = input("Enter student assessment marks (separated by comma): ")
#                 final_mark = Student(student_assessment).finalMark()
#                 ditStudent = DITStudent(student_assessment, final_mark)
#                 grade_letter = ditStudent.gradeLetter()
#                 grade_point = ditStudent.gradePoint(grade_letter)  
#                 grade_letter_final = grade_letter 

#                 if grade_letter == "NYC":
#                     resubmission = input("What is this student's resubmission mark: ") 
#                     Supplementary_score = Student(resubmission).finalMark() 
#                     grade_letter_final = ditStudent.gradeLetterFinal(Supplementary_score)   
#                     grade_point = ditStudent.gradePoint(grade_letter_final) 
                
#                 student_ee = StudentInfo(student_id, student_name, student_type, student_assessment, grade_letter, grade_point, final_mark, grade_letter_final)
#                 student_scores.append(student_ee.studentPerformance())  

#             elif option1 == 1.3:
#                 print(student_scores)
#                 break

#             option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
        
#             if option1 not in [1.1,1.2,1.3]:
#                 sys.exit("Please select a valid option")

#     # menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

#     # if menu not in [1,2,3,4]:
#     #     sys.exit("Please enter a whole number between 1 and 4")

#     # if menu == 1:
#     #     option1 = float(input(f"Choose one of the following options: \n 1.1 - Enter a BIT student information \n 1.2 - Enter a DIT student information \n 1.3 - Go back to the main menu \n"))
        
#     #     if option1 not in [1.1,1.2,1.3]:
#     #         sys.exit("Please select a valid option")     
        
#     elif menu == 2:    
#         option2 = float(input(f"Choose one of the following options: \n 2.1 - Print all student grade information ascendingly by final mark\n 2.2 - Print all student grade information descendingly by final mark \n 2.3 - Go back to the main menu \n"))
        
#         if option2 not in [2.1,2.2,2.3]:
#             sys.exit("Please select a valid option")

#         if option2 == 2.1:
#             sorted_student_scores = sorted(student_scores, key=lambda d: d['totalMark'], reverse=True)
#             for dic in sorted_student_scores:
#                 print(f"{dic['studentID']} \t {dic['name']} \t {dic['studentType']} \t {dic['totalMark']} \t {dic['gradeLetterFinal']} \n")   

#         elif option2 == 2.2:
#             sorted_student_scores = sorted(student_scores, key=lambda d: d['totalMark'])
#             for dic in sorted_student_scores:
#                 print(f"{dic['studentID']} \t {dic['name']} \t {dic['studentType']} \t {dic['totalMark']} \t {dic['gradeLetterFinal']} \n")  

#         elif option1 == 2.3:
#                 print(student_scores)
#                 break
            
#     elif menu == 3:
#         pass
        
#     elif menu == 4:
#         sys.exit("Program exited")    

#     menu = int(input(f"Choose one of the following options: \n 1 - Enter student grade information \n 2 - Print all student grade information \n 3 - Print class performance statistics \n 4 - Exit \n"))

#     if menu not in [1,2,3,4]:
#         sys.exit("Please enter a whole number between 1 and 4")    


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
