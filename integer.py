def check_input(input_str):
 if input_str.isdigit():
     print("Input is a number.")
 elif input_str.isalpha():
    if input_str.isupper():
         print("Input is an uppercase character.")
    elif input_str.islower():
         print("Input is a lowercase character.")
 else:
     print("Input is neither a number nor a character.")
user_input = input("Enter a number or a character: ")
check_input(user_input)