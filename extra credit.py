word = "taco cat"   
word = "".join(word)  # Remove spaces and convert to lowercase
copy_backwards = ""  
for each in word:
    copy_backwards = each + copy_backwards
if word == copy_backwards:
    print(f"{word} is a palindrome")