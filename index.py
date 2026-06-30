angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))

angle3 = 180 - (angle1 + angle2)

if angle3 <= 0:
    print("Invalid triangle")
elif angle1 == 90 or angle2 == 90 or angle3 == 90:
    print("The triangle is a Right-Angled Triangle")
else:
    print("The triangle is NOT a Right-Angled Triangle")
