
# Case Study 12: Attendance Recovery Computation

print("====================================")
print("     ATTENDANCE RECOVERY SYSTEM")
print("====================================")

# Input details
total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
required_percentage = float(input("Enter required attendance percentage: "))

# Validate inputs
if total_classes <= 0:
    print("Invalid total classes!")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Invalid attended classes!")
elif required_percentage <= 0 or required_percentage > 100:
    print("Invalid eligibility percentage!")

else:
    # Calculate current attendance
    current_percentage = (attended_classes / total_classes) * 100

    print("\n----- CURRENT ATTENDANCE -----")
    print("Total Classes:", total_classes)
    print("Attended Classes:", attended_classes)
    print("Current Attendance:", round(current_percentage, 2), "%")

    if current_percentage >= required_percentage:
        print("Status: Eligible for examination")
        print("No additional classes are required.")
    else:
        print("Status: Not Eligible for examination")

    # Scenario 1: Attend all future classes
    print("\n----- SCENARIO 1 -----")
    print("Attend all future classes")

    new_total = total_classes
    new_attended = attended_classes
    classes_needed = 0

    while (new_attended / new_total) * 100 < required_percentage:
        new_total += 1
        new_attended += 1
        classes_needed += 1

    print("Minimum classes required:", classes_needed)
    print("Final Attendance:",
          round((new_attended / new_total) * 100, 2), "%")

    # Scenario 2: Attend 4 out of every 5 classes
    print("\n----- SCENARIO 2 -----")
    print("Attend 4 out of every 5 classes")

    new_total = total_classes
    new_attended = attended_classes
    classes_needed = 0
    pattern = 0

    while (new_attended / new_total) * 100 < required_percentage:
        pattern += 1
        new_total += 1
        classes_needed += 1

        if pattern <= 4:
            new_attended += 1

        if pattern == 5:
            pattern = 0

    print("Minimum classes required:", classes_needed)
    print("Final Attendance:",
          round((new_attended / new_total) * 100, 2), "%")

    # Scenario 3: Attend 3 out of every 5 classes
    print("\n----- SCENARIO 3 -----")
    print("Attend 3 out of every 5 classes")

    new_total = total_classes
    new_attended = attended_classes
    classes_needed = 0
    pattern = 0

    while (new_attended / new_total) * 100 < required_percentage:
        pattern += 1
        new_total += 1
        classes_needed += 1

        if pattern <= 3:
            new_attended += 1

        if pattern == 5:
            pattern = 0

    print("Minimum classes required:", classes_needed)
    print("Final Attendance:",
          round((new_attended / new_total) * 100, 2), "%")

    print("\n====================================")
    print("       ATTENDANCE REPORT")
    print("====================================")
