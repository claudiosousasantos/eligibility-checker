age = int(input("Please tell us your age: "))
height = int(input("Please tell us how tall you are (in cm): "))

if age < 16:
    print("Unfortunately you can't apply, you don't meet the minimum age requirement.")
elif height < 150:
    print("You also need to be at least 150cm tall to safely reach the pedals.")
else:
    print("Eligible to apply for a learner's permit. Good luck!")