from string import punctuation
import re

text = input("Text: ")
# Creates new string with all letters in text, not including an punctation or spaces.
# Counts length of string to get number of letters in text
letter_count = len(
    "".join(ch for ch in text if ch no in punctuation).replace(" ", ""))
# Splits text into list of each word and counts number of words
word_count = len(text.split())
# Splits text into list of sentences, by ., ! and ?
sentence_list = re.split('[.!?]', text)
# Removes empy string from end of list
sentence_list.pop()
# Gets length of list (number of sentences in text)
sentence_count = len(sentence_list)

# Calculates avergae number of letters per 100 words and sentences per 100 words
avg_letters_per100 = (100 / word_count) * letter_count
avg_sentences_per100 = (100 / word_count) * sentence_count

# Calculates grade of writing using Coleman-Liau formula
index = (0.0588 * avg_letters_per100) - (0.296 * avg_sentences_per100) - 15.8

if round(index) >= 16:
    grade = "Grade 16+"
elif round(index) < 1:
    grade = "Before Grade 1"
else:
    grade = f"Grade {round(index)}"

print(grade)
