from string import punctuation
import re

text = input("Text: ")

letter_count = len(
    "".join(ch for ch in text if ch not in punctuation).replace(" ", ""))

word_count = len(text.split())

sentence_list = re.split('[.!?]', text)
sentence_list.pop()
sentence_count = len(sentence_list)

avg_letters_per100 = (100 / word_count) * letter_count

avg_sentences_per100 = (100 / word_count) * sentence_count

index = (0.0588 * avg_letters_per100) - (0.296 * avg_sentences_per100) - 15.8

if round(index) >= 16:
    grade = "Grade 16+"
elif round(index) < 1:
    grade = "Before Grade 1"
else:
    grade = f"Grade {round(index)}"

print(grade)
