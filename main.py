
def main():    
    with open("books/frankenstein.txt", "r") as file:
        data = file.read()
        print(count_words(data))
        print(count_characters(data))

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

main()