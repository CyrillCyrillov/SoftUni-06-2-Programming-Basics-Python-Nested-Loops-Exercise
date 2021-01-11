numbers_of_assessments = int(input())
next = " "
number_of_themes = 0
global_assessment = 0

while next != "Finish":
    next = input()
    if next != "Finish":
        number_of_themes += 1
        current_assessment = 0
        for i in range(1, numbers_of_assessments + 1):
            next_assessment = float(input())
            current_assessment += next_assessment

        print(f"{next} - {current_assessment / numbers_of_assessments:.2f}.")
        global_assessment += current_assessment

print(f"Student's final assessment is {(global_assessment / number_of_themes / numbers_of_assessments):.2f}.")

