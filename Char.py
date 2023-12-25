a=input("Enter a number or a character: ")
if a.isdigit():
 print("Input is a number.")
elif a.isalpha():
    if a.isupper():
        print("Input is an uppercase character.")
    elif a.islower():
        print("Input is a lowercase character.")
else:
    print("Input is neither a number nor a character.")