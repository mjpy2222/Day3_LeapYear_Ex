# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0 and year % 100 >= 1:
    print("Leap year")
elif year % 100 >= 1 or year % 400 != 0:
    print("Not leap year")
