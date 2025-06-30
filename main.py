#needed imports
import sys

#establish a path to the books location
def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

#pull from stats.py
from stats import (
	get_word_count, 
	get_char_count,
	char_sort
)

#print the number of words from the book in a string response
def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	input = sys.argv[1]
	book_text = get_book_text(f"{input}")
	total_words = get_word_count(book_text)
	char_counts = get_char_count(book_text)
	chars_sorted_list = char_sort(char_counts)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {input}...")
	print("----------- Word Count ----------")
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	for item in chars_sorted_list:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

main()


