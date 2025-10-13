print("Welcome to the BMI Calculator!")
print("Here you can enter your weight and height and we will tell you your Body Mass Index!")

weight = float(input("Enter your weight in KG: "))
height = float(input("Enter your height in meters: "))

bmi = weight / height**2

if bmi < 18.5:
    print("You are underweight.")
    print(f"Your BMI is: {bmi:.2f}")
elif 18.5 <= bmi < 25.9:
    print("You have a normal weight.")
    print(f"Your BMI is: {bmi:.2f}")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
    print(f"Your BMI is: {bmi:.2f}")
elif 30 <= bmi < 39.9:
    print("You are obese.")
    print(f"Your BMI is: {bmi:.2f}")
else:
    print("You are severely obese.")
    print(f"Your BMI is: {bmi:.2f}")
