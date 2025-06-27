#establish a path to the books location
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

#gather the number of words total in the book and store as a variable
def get_word_count(book_text):
	words = book_text.split()
	num_words = len(words)
	return num_words

#print book's text
#def main():
#	print(get_book_text("books/frankenstein.txt"))

#print the number of words from the book in a string response
def main():
	book_text = get_book_text("books/frankenstein.txt")
	total_words = get_word_count(book_text)
	print(f"{total_words} words found in the document")

main()


