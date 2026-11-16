# I read text from a file and converted it to lowercase.
# I used a dictionary to count how many times each word appears.
# Exercise 7: Word Frequency Counter

with open(r"C:\Users\arooj\OneDrive\Desktop\New folder\task class.py\sample_text.txt", "r") as file:
    text = file.read()

text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Total words:", len(words))
print("Unique words:", len(word_count))
print("Word frequencies:")

for word, count in word_count.items():
    print(word, ":", count)
