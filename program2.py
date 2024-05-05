def calculate_average(oxygen_levels):
    total = sum(oxygen_levels)
    average = total / len(oxygen_levels)
    return round(average)

def check_oxygen_value(oxygen):
    return 1 <= oxygen <= 100

trainees = []
for i in range(3):
    oxygen_levels = []
    for j in range(3):
        oxygen = int(input(f"Enter oxygen level for trainee {i + 1}, round {j + 1}: "))
        if not check_oxygen_value(oxygen):
            print("INVALID INPUT")
            exit(1)
        oxygen_levels.append(oxygen)
    average_oxygen = calculate_average(oxygen_levels)
    trainees.append((i + 1, average_oxygen))

trainees.sort(key=lambda x: x[1], reverse=True)
max_average = trainees[0][1]
fittest_trainees = [t[0] for t in trainees if t[1] == max_average]

if max_average < 70:
    print("All trainees are unfit.")
else:
    print("Most fit trainee(s):", fittest_trainees)
    print("Highest average oxygen level:", max_average)
