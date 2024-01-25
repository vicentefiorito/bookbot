def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(num_letters)


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
    
        


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()