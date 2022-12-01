from rich import print

sentence = "This is a sentence consisting of eight words."
words = sentence.split()

print()
print(f"Words in sentence: {words}")

words[0] = words[0].lower()
print(f"First element all lower-case: {words[0]}")

last_element = words[-1]
# We can slice on a string as well
last_element = last_element[:-1]
words[-1] = last_element
print(f"Last element no trailing period: {words[-1]}")

eight_exist = "eight" in words
print(f"Does the value 'eight' exist in words: {eight_exist}")
print()
