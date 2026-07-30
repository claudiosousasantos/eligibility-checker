age = int(input("Please tell us your age: "))
height = int(input("Please tell us how tall are you: "))

if age < 12:
    print("Unfortunately you can't do this, you're unable to meet the age requirement.")
elif height < 140:
    print("And also you need to be at least 140cm tall.")
else:
    print("Access allowed. Enjoy the park!")