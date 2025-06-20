word = input("Enter a word: ").strip().lower().split()
word = "".join(word)  # Get the word from the user, strip whitespace, convert to lowercase, and split into a list of characters
copy_backwards = "" # Join the list into a single strin
for each in word:
    copy_backwards = each + copy_backwards
print(f"The word backwards is: {copy_backwards}")
if word == copy_backwards:
        print(f"{word} is a palindrome")
else:
        print(f"{word} is not a palindrome")
    