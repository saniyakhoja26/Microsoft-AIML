state = input("Enter your state: ")

n = int(input("Enter number of subjects: "))

total_marks = 0

for i in range(n):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total_marks += marks

total_score = n * 100   # assuming each subject is out of 100
percentage = (total_marks / total_score) * 100

if state.lower() == "gujarat":
    if percentage >= 60:
        print("Qualified (Gujarat criteria)")
    else:
        print("Not Qualified (Gujarat criteria)")
else:
    if percentage >= 70:
        print("Qualified (Other state criteria)")
    else:
        print("Not Qualified (Other state criteria)")

print("Percentage:", round(percentage, 2), "%")
