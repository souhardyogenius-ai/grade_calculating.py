name = input("Enter Name: ")

# Truthy/Falsy Check
if not name:
    print("Invalid Name Input")
else:
    math = float(input("Math: "))
    english = float(input("English: "))
    science = float(input("Science: "))
    attendance = float(input("Attendance: "))

    # Pass/Fail condition
    if math < 33 or english < 33 or science < 33:
        print("Result: FAIL")
        print("Better luck next time")
    else:
        print("Result: PASS")

        # Average calculation
        average = (math + english + science) / 3

        # Grade calculation
        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)

        # Scholarship eligibility
        if average >= 75 and attendance >= 80:
            print("Scholarship: Eligible")
        else:
            print("Scholarship: Not Eligible")

        # Warning system
        if math < 40:
            print("Warning: Improve in Math")
        if english < 40:
            print("Warning: Improve in English")
        if science < 40:
            print("Warning: Improve in Science")

        # Excellent performance
        if math >= 90 and english >= 90 and science >= 90:
            print("Excellent Performance")