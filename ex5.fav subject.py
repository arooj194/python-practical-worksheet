# I created a list to store favourite subjects.
# I used append, remove and a for loop to manage and display the subjects.
# Ex 5: Fav sub List

subjects = ["Python", "Security", "AI"]

print("First subject:", subjects[0])
print("Last subject:", subjects[-1])

new_subject = input("Enter your favourite subject: ")
subjects.append(new_subject)

print("All subjects:")

for subject in subjects:
    print(subject)

if "Python" in subjects:
    print("Python is in the list.")

remove_subject = input("Enter a subject to remove: ")

if remove_subject in subjects:
    subjects.remove(remove_subject)
    print("Updated list:", subjects)
else:
    print("Subject not found.")
