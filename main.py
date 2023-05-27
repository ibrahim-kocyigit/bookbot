def count_letters(text):
    count = {}

    for c in text.lower():
        if c.isalpha():
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

    for i in sorted(count):
        print(f"The '{i}' character was found {count[i]} times.")


def count_words(text):
    count = 0

    for i in text.split():
        count += 1

    print(f"{count} words found in the document.")


with open("books/frankenstein.txt") as f:
    text = f.read()

count_words(text)
count_letters(text)
