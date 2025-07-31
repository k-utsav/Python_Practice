"""
Write a program that asks the user to enter a sentence. The program should then count and display the number of words in that sentence.
"""

sentence = input("Enter a sentence: ")

words = sentence.split()
print(words)
word_count = len(words)
print(word_count)