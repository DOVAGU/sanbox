"""
Word Occurrences
Estimate: 10 minutes
Actual:   18 minutes
"""

text = input("Enter a string: ")

word_counts = {}

for word in text.split():
    word = word.lower()
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

max_width = max(len(word) for word in word_counts)

for word, count in sorted(word_counts.items()):
    print(f"{word:{max_width}} : {count}")
