# Write a match-case program that takes user input for a day of the week and prints whether it’s a weekday or weekend.

day = input("Enter a day: ").lower()

match day:
    case "saturday" | "sunday":
        print("Weekend")
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case _:
        print("Invalid day")