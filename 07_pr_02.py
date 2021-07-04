marks1 = int(input("Enter subject 1 marks : "))
marks2 = int(input("Enter subject 2 marks : "))
marks3 = int(input("Enter subject 3 marks : "))


if (marks1<33 or marks2<33 or marks3<33):
    print("You are fail because you have less than 33% in one of the exam.")

elif ((marks1 + marks2 + marks3)/3 < 40):
    print("You are fail because your total percentage is less than 40% .")


else:
    print("Congratulations You Passed the exam.")