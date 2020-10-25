"""
Filename: FinalAssignment_V4.py
Purpose: Calculator for calculating the electricity costs of an office building.
Input: User fills in the amount of rooms in a building, the lamps per room
and puts in what percentage stays on for 10 hours.
Output: Overview of the electricity costs for a day, week and month (based on the input of the user)
Description: The calculation of the lamp costs of an office.
Based on 10 and 20 hour lamps with the amount of rooms and lamps per individual room.

Author: Naib Haq
Student number: 500852640
Version: 4.0
Date: 24/10/2020
"""
# The intro (displayed clearly and conveniently)
print("Welcome to the HAQ office electricity calculator.\n"
      "\nThis calculates the electricity costs of lamps in an office.\n"
      "The costs are based on:\n"
      "- How many rooms the office building has.\n- How many lamps there are per room.\n"
      "- What % of the lamps are turned on for 10 hours (this program will calculate the remaining % for 20 hours).\n"
      "- Two separate totals will be calculated of the electricity costs per day, per week and per month.\n")

lamp_cost = 0.0015          # lamp costs per hour (based on tl bulbs)
per_week = 5                # 5 days a week
per_month = 4               # 4 weeks make 20 days

# (1st loop) creating a loop for the inputs of building_rooms and room_lights.
# making sure to put an integer as the input of the user will be numbers.
while True:
    building_rooms = int(input("How many rooms does the office have?:"))
    room_lights = int(input("How many lamps does one room contain?:"))

    # (2nd loop) creating a 2nd loop to check whether the user input is between 0 and 100
    # When the user input is between 0 and 100, the loop will break and move on with the 1st loop.
    # If the input is not between 0 and 100, then only the 2nd loop will start again.
    while True:
        percentage10h = int(input("Of the total amount of lamps, what % of the lamps stay on for 10 hours?:"))
        if percentage10h >= 0 and percentage10h <= 100:
            break
        else:
            print("Your input is incorrect, your % should be in a range between 0 and 100.\n")

    percentage20h = 100 - percentage10h
    confirmation = input("Please confirm the entered data below:\nThere are {} rooms in the office with "
                         "{} lamps per room.\n{}% of the lamps are on for 10 hours and {}% for 20 hours.\n"
                         "Is this correct? Please fill in [Yes] or [No]: "
                         .format(building_rooms, room_lights, percentage10h, percentage20h))

    # results10h/20h = Creating an empty lists for 10h and 20h, further down below values will be added to the list.
    # total_percentage10h/20h   = The user input will be divided by 100
    # total_lights10h/20        = Is the total of 10h and 20h lamps
    # cost_per_day10h/20        = Is the total of 10h and 20h lamps a day, rounded by 2
    # cost_per_week10h/20       = Is the total of 10h and 20h lamps a week, rounded by 2
    # cost_per_month10h/20      = Is the total of 10h and 20h lamps a month, rounded by 2
    results10h = []
    results20h = []
    total_percentage10h = percentage10h/100
    total_percentage20h = percentage20h/100
    total_lights10h = building_rooms * room_lights * total_percentage10h
    total_lights20h = building_rooms * room_lights * total_percentage20h
    cost_per_day10h = round(total_percentage10h * lamp_cost * total_lights10h, 2)
    cost_per_day20h = round(total_percentage20h * lamp_cost * total_lights20h, 2)
    cost_per_week10h = round(cost_per_day10h * per_week, 2)
    cost_per_week20h = round(cost_per_day20h * per_week, 2)
    cost_per_month10h = round(cost_per_week10h * per_month, 2)
    cost_per_month20h = round(cost_per_week20h * per_month, 2)

    results10h.append(cost_per_day10h)          # Here we add the values to the results10h lists
    results10h.append(cost_per_week10h)
    results10h.append(cost_per_month10h)

    results20h.append(cost_per_day20h)          # Here we add the values to the results20h lists
    results20h.append(cost_per_week20h)
    results20h.append(cost_per_month20h)
    # The results lists have the following order: [day costs,week costs,month costs]

# if the input on the "confirmation" is yes, then the total prices will be calculated based on the entered data.
# if the input on the "confirmation" is no, then the whole program will start again.
    if confirmation.lower() == 'yes':
        print("\nThere are a total of {} rooms and {} lamps.\n{}% of the lamps are turned on for 10 hours\n"
              "and {}% are turned on for 20 hours.\n"
          "Total costs of 10 hour lamps a day: €{}\n"
          "Total costs of 10 hour lamps a week:: €{}\n"
          "Total costs of 10 hour lamps a month: €{}\n\n"
          "Total costs of 20 hour lamps a day: €{}\n"
          "Total costs of 20 hour lamps a week: €{}\n"
          "Total costs of 20 hour lamps a month: €{}"
              .format(building_rooms, room_lights, percentage10h, percentage20h, results10h[0], results10h[1],
                      results10h[2], results20h[0], results20h[1], results20h[2]))
        break
    else:
        print("Please try again")