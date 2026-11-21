
# Task 01: Text and Number Tools
def count_words(sentence):    # count the words in a sentence
    words = sentence.split()
    return len(words)
def longest_word(sentence):      # Function used to find the longest word
    words = sentence.split()
    if not words:
        return "No words found"
    return max(words, key=len)
def reverse_sentence(sentence):     # Reverse a sentence
    return sentence[::-1]
def is_prime(number):     # Check whether a number is prime
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# Main program
print("===== TEXT AND NUMBER TOOLS =====")
sentence = input("\nEnter a sentence: ")
print("\n----- TEXT RESULTS -----")
print("Word Count:", count_words(sentence))
print("Longest Word:", longest_word(sentence))
print("Reversed Sentence:", reverse_sentence(sentence))
number = int(input("\nEnter a number: "))
print("\n----- NUMBER RESULTS -----")
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
print("\n===== PROGRAM COMPLETED =====")