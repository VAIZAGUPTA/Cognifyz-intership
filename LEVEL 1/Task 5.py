
def check_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    reversed_text = cleaned_text[::-1]

    print("Original (processed):", cleaned_text)
    print("Reversed version    :", reversed_text)

    if cleaned_text == reversed_text:
        print("Result: It IS a palindrome")
        print("Reason: It reads the same forward and backward")
    else:
        print("Result: It is NOT a palindrome")
        print("Reason: Forward and backward readings are different")


word = input("Enter a word or phrase: ")
check_palindrome(word)

