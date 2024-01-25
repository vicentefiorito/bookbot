def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    report = generate_report(book_path,text)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    lowercase = text.lower()
    letter_count = {}
    count = 0
    for word in lowercase:
        if word in lowercase:
            count += 1
        letter_count[word] =  count
    return letter_count
    
def generate_report(path,text):
    words = get_num_words(text)
    letter_count = get_num_letters(text)
    list_letter_count = list(letter_count.items())
    list_letter_count.sort()

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print("")
    for letter in list_letter_count:
        if letter[0].isalpha():
            print(f"{letter[0]} was found {letter[1]} times")
    print("--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()