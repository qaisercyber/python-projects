#Word Count
#Characters count
#Most common words
#Palindrome checker
#User will be asked to provide the text
import string
#Word Count
def count_words(text):
    words = text.split()
    return len(words)

#Charcters Count

def count_chars(text):
    with_spaces = len(text)
    without_spaces = len(text.replace(" ", ""))
    return with_spaces , without_spaces

def most_frequent(text):
    words = text.split()

    frequency = {}
    for word in words:
        cleaned_word = word.lower().strip(string.punctuation)
        if cleaned_word:
            frequency[cleaned_word]=frequency.get(cleaned_word,0)+1
    if not frequency:
        return None , 0
    most_common = max(frequency, key = frequency.get)
    return most_common , frequency[most_common]

def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    cleaned_text = cleaned_text.translate(str.maketrans("","",string.punctuation))
    return cleaned_text == cleaned_text[::-1]

def display_results(text):
    word_count = count_words(text)
    with_spaces, without_spaces = count_chars(text)
    common_word , count_frequency = most_frequent(text)
    palindrome_status = is_palindrome(text)

    print("\n📊 TEXT ANALYSIS RESULTS")
    print("-" * 35)
    print(f"Total words: {word_count}")
    print(f"Characters with spaces: {with_spaces}")
    print(f"Characters without spaces : {without_spaces}")

    if common_word:
        print(f"Most common words : {common_word} is {count_frequency}")
    else:
        print("Most common word is " , None)
    if palindrome_status:
        print("Yes")
    else:
        print("No")

def main():
    print("📝 TEXT ANALYZER TOOL")
    print("=" * 35)

    text = input("Enter your text:\n")
    display_results(text)


# ------------------ Program Entry Point ------------------
if __name__ == "__main__":
    main()






