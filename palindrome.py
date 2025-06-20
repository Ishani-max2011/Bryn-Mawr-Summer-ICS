word = input("Enter a word: ").strip().lower().split()
word = "".join(word)  
copy_backwards = "" 
copy_backwards = each + copy_backwards
print(f"The word backwards is: {copy_backwards}")
if word == copy_backwards:
        print(f"{word} is a palindrome")
else:
        print(f"{word} is not a palindrome")

#Extra Credit
word = "taco cat"   
word = "".join(word)  # Remove spaces and convert to lowercase
copy_backwards = ""  
for each in word:
    copy_backwards = each + copy_backwards
if word == copy_backwards:
    print(f"{word} is a palindrome")
      