#function for get_wordcount
def get_word_count(book_text):
        words = book_text.split()
        num_words = len(words)
        return num_words

#function for character count
def get_char_count(book_text):
	indv_char_dict = {}
	words = book_text.split()
	for word in words:
		lower_cased = word.lower()
		for letter in lower_cased:
			if letter not in indv_char_dict:
				indv_char_dict[letter] = 1
			else:
				indv_char_dict[letter] += 1
	return indv_char_dict
