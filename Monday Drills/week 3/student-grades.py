def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

students = [
    {"name": "Sam", "scores": [80, 90]}, 
    {"name": "David", "scores": [55, 60]},
#    {"name": "Alice", "scores": [75, 85]},
#    {"name": "Michael", "scores": [92, 88]},
#    {"name": "Grace", "scores": [68, 72]},
#    {"name": "Daniel", "scores": [95, 91]},
#    {"name": "Sophia", "scores": [60, 70]}
]

averages = []

for student in students:
    total = 0
    for score in student["scores"]:
        total += score
    average = total / len(student["scores"])
    averages.append(average)
    print(f"{student['name']} → Average: {average:.2f} → Grade: {calculate_grade(average)}")

# Find highest and lowest
highest = averages[0]
lowest = averages[0]
highest_index = 0
lowest_index = 0

for i in range(len(averages)):
    if averages[i] > highest:
        highest = averages[i]
        highest_index = i

    if averages[i] < lowest:
        lowest = averages[i]
        lowest_index = i

print("Highest:", students[highest_index]["name"], "with an average of", highest)
print("Lowest:", students[lowest_index]["name"], "with an average of", lowest)
