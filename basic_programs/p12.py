'''
Given the average marks of a student, print the result as follows:
0  - 49 Fail
50 - 79 SC
80 - 95 FC
96- 100 Excellent 
Also check for invalid Input

Read average score avg_score
if avg_score is in range 0 to  49 then print fail
else if avg_score is in range 50 to 79 then print second class
else if avg_score is in range 80 to 95 then print first class
else if avg_score is in range 96 to 100 then print Excellent
else invalid score
'''
avg_score = float(input('Enter average score of the student: '))
if avg_score >= 96 and avg_score <= 100:
    print('Result is Excellent')
elif avg_score >= 80:
    print('Result is First Class')
elif avg_score >= 50:
    print('Result is Second Class')
elif avg_score >= 0:
    print('Result is Fail')
else:
    print('Input is invalid')