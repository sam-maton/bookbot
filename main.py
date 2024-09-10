
def main():    
	with open("books/frankenstein.txt", "r") as file:
		data = file.read()
		word_count = count_words(data)
		character_count = count_characters(data)
		print('--- Begin report of books/frankenstein.txt ---')
		print(f"{word_count} words found in the document")
		print_letter_report(character_count)
		print('--- End report ---')

def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	loweer_text = text.lower()
	count = {}
	for char in loweer_text:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	return count

def print_letter_report(word_dict):
	letter_list = convert_dict_to_list(word_dict)
	letter_list.sort(key=sort_on, reverse=True)

	for letter in letter_list:
		if letter['char'].isalpha():
			print(f"The '{letter['char']}' character was found {letter['count']} times")

def convert_dict_to_list(word_dict):
	word_list = []
	for key, value in word_dict.items():
		word_list.append({"char": key, "count": value})
	return word_list

def sort_on(dict):
    return dict["count"]
	

main()