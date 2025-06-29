#establish a path to the books location
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

#pull from stats.py
from stats import get_word_count

from stats import get_char_count

#print the number of words from the book in a string response
def main():
	book_text = get_book_text("books/frankenstein.txt")
	total_words = get_word_count(book_text)
	print(f"{total_words} words found in the document")
	print(get_char_count(book_text))
main()


