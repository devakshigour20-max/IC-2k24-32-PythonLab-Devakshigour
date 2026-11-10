# Word Frequency Counter

paragraph = input("Enter a paragraph: ")

clean_text = ""
for ch in paragraph.lower():
    if ch.isalnum() or ch.isspace():
        clean_text += ch

words = clean_text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

if len(frequency) == 0:
    print("No words entered")
else:
    print("Word counts:", frequency)

    n = int(input("Enter N: "))
    top_words = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    print("Top words:", top_words[:n])

    once = [word for word in frequency if frequency[word] == 1]
    print("Words appearing once:", sorted(once))

    inverted = {}
    for word, count in frequency.items():
        inverted.setdefault(count, []).append(word)

    for count in inverted:
        inverted[count].sort()
    print("Inverted dictionary:", inverted)

    length_groups = {}
    for word in frequency:
        length_groups.setdefault(len(word), []).append(word)

    for length in length_groups:
        length_groups[length].sort()
    print("Words grouped by length:", length_groups)

    search_word = input("Enter word to search: ").lower()
    print("Count:", frequency.get(search_word, "not found"))
