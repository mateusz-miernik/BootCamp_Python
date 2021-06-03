"""
    DAY 2: Tip calculator
"""

if __name__ == "__main__":
    print("Welcome to the tip calculator")
    total_bill = float(input("What was the total bill? $"))
    num_of_people = int(input("How many people to split the bill? "))
    tip_in_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
    result = round((total_bill + (tip_in_percent / 100)*total_bill) / num_of_people, 2)
    print(f"Each person should pay: ${result}")
