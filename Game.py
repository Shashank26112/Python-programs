import random
number=random.randint(1,10)
class Error(Exception):
    pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
    pass
while True:
    try:
        guess=int(input("Enter a number:"))
        if guess< number:
            raise ValueSmallError
        elif guess> number:
            raise ValueLargeError
        break
    except ValueSmallError:
        print("This value is small,try again!!")
    except ValueLargeError:
        print("This value is large,try again!!")
print("Congratulations!! You guessed it correctly.")
            