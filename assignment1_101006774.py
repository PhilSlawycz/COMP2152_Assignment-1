"""
Author: # Philip Slawycz
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #integer
membership_active = True #boolean

# Step c: Create a dictionary named workout_stats
#stores the names as keys and the tuples as values
workout_stats = {
    "Alex": (30, 30, 30), #yoga, running, weightlifting
    "Jamie": (20, 30, 20),
    "Taylor": (45, 45, 30),
    }
# Step d: Calculate total workout minutes using a loop and add to dictionary
newDict = {}
for x in workout_stats:
    newDict[f"{x}_total"] = sum(workout_stats[x])
workout_stats.update(newDict)

# Step e: Create a 2D nested list called workout_list
excludedKeys =["Alex_total", "Jamie_total", "Taylor_total"]
# my nested list that stores workout minutes for each friend
workout_list = [x for y, x in workout_stats.items() if y not in excludedKeys]

# Step f: Slice the workout_list
print(f"Totals for yoga and running for all friends: {[friend[:2] for friend in workout_list]} in minutes" )
print(f"Jamies and Taylors Time weightlifting: {[friend[2]for friend in workout_list[-2:]]} in minutes")
# Step g: Check if any friend's total >= 120
for y, x in workout_stats.items():
        if y.endswith("_total") and x >= 120:
            print(f"Great job staying active {y.replace('_total', '' )}!")
# Step h: User input to look up a friend
t = True
while t == True:
    name = input("Enter your friends name: ")
    if name.title() == "Alex":
        print(f"Yoga: {workout_list[0][0]} Minutes", "\n"
                  f"Running: {workout_list[0][1]} Minutes", "\n"
                   f"Weight Lifting: {workout_list[0][2]} Minutes", "\n"
                    f"Total workout time: {workout_stats["Alex_total"]} Minutes")
        t = False
    elif name.title() == "Jamie":
        print(f"Yoga: {workout_list[1][0]} Minutes", "\n"
                  f"Running: {workout_list[1][1]} Minutes", "\n"
                   f"Weight Lifting: {workout_list[1][2]} Minutes", "\n"
                    f"Total workout time: {workout_stats["Jamie_total"]} Minutes")
        t = False
    elif name.title() == "Taylor":
        print(f"Yoga: {workout_list[2][0]} Minutes", "\n"
                  f"Running: {workout_list[2][1]} Minutes", "\n"
                   f"Weight Lifting: {workout_list[2][2]} Minutes", "\n"
                    f"Total workout time: {workout_stats["Taylor_total"]} Minutes")
        t = False
    else:
        print("Friend", name, "not found in the records.")
        break

# Step i: Friend with highest and lowest total workout minutes
max_minute = max(newDict, key=newDict.get)
min_minute = min(newDict, key=newDict.get)
print(f"{max_minute.replace('_total','')} Worked out the most at {newDict[max_minute]} minutes" )
print(f"{min_minute.replace('_total','')} Worked out the least at {newDict[min_minute]} minutes")
