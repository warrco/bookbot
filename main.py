def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    characters = character_count(text)
    report_listdict = sort_report(characters)

# Genenerate report of words
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} words found in the document")
    print()

    for char_dict in report_listdict:
        if not char_dict["letter"].isalpha():
            continue
        print(f"The letter {char_dict['letter']} was found {char_dict['count']} times")

    print("--- End report ---")

# Count the number of words within a book
def word_count(text):
    
    num_of_words = 0
    words = text.split()

    for word in words:
        num_of_words += 1
    return num_of_words

# Define the book's path
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

# Count the number of times a character appears
def character_count(text):
    characters = {}
    for letter in text:
        letter = letter.lower()
        characters[letter] = characters.get(letter, 0) + 1
    return characters

#   Sort and print a report of the characters

def sort_on(characters):
    return characters["count"]

def sort_report(characters):

    report_listdict = []

    for key, value in characters.items():
            report_listdict.append({"letter": key, "count": value})
    report_listdict.sort(reverse=True, key=sort_on)
    return report_listdict

main()