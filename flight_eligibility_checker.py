age = int(input("Please tell us the child's age: "))
height = int(input("Please tell us how tall the child is (in cm): "))

if age < 5:
    print("Unfortunately, children under 5 cannot travel as unaccompanied minors.")
elif height < 100:
    print("The child must be at least 100cm tall to use a standard seatbelt instead of a booster seat.")
else:
    print("Eligible for unaccompanied minor travel with standard seating. Enjoy your flight!")