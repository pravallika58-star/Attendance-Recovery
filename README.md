# Attendance-Recovery
# Case Study 12: Attendance Recovery Computation

## Python Activity-Based Learning

### Student Details
- **Name:** DURGA SURYA PRAVALLIKA
- **Roll Number:** N26VO1AO383
- **Branch:** CSE
- **Section:** SECTION-5
- **Programming Language:** Python

---

## 1. Problem Statement

The Attendance Recovery Computation system calculates the current attendance percentage of a student and determines the minimum number of consecutive classes required to reach the required attendance eligibility percentage.

It also analyses different future attendance scenarios, such as attending all classes, attending 4 out of 5 classes, and attending 3 out of 5 classes.

## 2. Objectives

- To calculate the current attendance percentage.
- To check examination eligibility.
- To determine the minimum additional classes required.
- To analyse different future attendance scenarios.
- To understand the use of loops and conditional statements in Python.

## 3. Assumptions

1. Total classes conducted must be greater than zero.
2. Attended classes cannot exceed total classes.
3. Required attendance percentage must be between 0 and 100.
4. Future attendance follows the specified repeating patterns.
5. Attendance percentage is calculated using the total classes conducted.

## 4. Algorithm

1. Start the program.
2. Read total classes conducted.
3. Read the number of classes attended.
4. Read the required attendance percentage.
5. Validate the input values.
6. Calculate the current attendance percentage.
7. Check whether the student is eligible.
8. Calculate the minimum classes required when attending all future classes.
9. Calculate attendance recovery when attending 4 out of every 5 classes.
10. Calculate attendance recovery when attending 3 out of every 5 classes.
11. Display the results of all scenarios.
12. Stop the program.

## 5. Pseudocode

```text
START

INPUT total_classes
INPUT attended_classes
INPUT required_percentage

IF inputs are invalid
    DISPLAY error message
ELSE
    CALCULATE current attendance

    IF current attendance >= required percentage
        DISPLAY Eligible
    ELSE
        DISPLAY Not Eligible

    SCENARIO 1:
        Attend every future class
        COUNT required classes using WHILE loop
        DISPLAY result

    SCENARIO 2:
        Attend 4 out of every 5 classes
        CHECK whether target is achievable
        CALCULATE required classes
        DISPLAY result

    SCENARIO 3:
        Attend 3 out of every 5 classes
        CHECK whether target is achievable
        CALCULATE required classes
        DISPLAY result
END IF

STOP
```

## 6. Python Source Code

The complete Python program is available in `attendance_recovery.py`.

## 7. Test Cases

| Test | Total | Attended | Target |
|---|---:|---:|---:|
| 1 | 100 | 70 | 75% |
| 2 | 100 | 80 | 75% |
| 3 | 50 | 30 | 75% |
| 4 | 100 | 90 | 75% |

## 8. Expected Output

For Test Case 1:

```text
ATTENDANCE RECOVERY SYSTEM

Total classes: 100
Attended classes: 70
Required attendance: 75%

Current attendance: 70.0%
Status: Not Eligible

SCENARIO 1:
Attend all classes
Classes needed: 20
Final percentage: 75.0%

SCENARIO 2:
Attend 4 out of 5 classes
Classes needed: 50
Final percentage: 80.0%

SCENARIO 3:
Attend 3 out of 5 classes
Target cannot be achieved in this scenario.
```

## 9. Conclusion

The Attendance Recovery Computation system successfully calculates student attendance percentages and determines examination eligibility. It also analyses different future attendance patterns and calculates the minimum number of classes required to reach the eligibility target.

This project helps us understand Python variables, data types, operators, conditional statements, and loops through a real-life student attendance problem.

---

**Project:** Python Activity-Based Learning  
**Case Study Number:** 12  
**Topic:** Attendance Recovery Computation
