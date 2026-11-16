
# Ex 6: Mini St Record

student = {
    "name": "Ali",
    "course": "Python",
    "mark": 65
}

print("Student name:", student["name"])
print("Student mark:", student["mark"])

if student["mark"] >= 50:
    print("Pass")
else:
    print("Review required")

student["mark"] = 75

print("Updated student record:", student)
