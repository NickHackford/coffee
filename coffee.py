import os
import random

file_path = "./names.txt"
assert os.path.exists(file_path), "./names.txt needs to exist."

lines = []
max_name_length = 0

with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())
        if len(line) > max_name_length:
            max_name_length = len(line)

length = len(lines)
if length % 2 == 1:
    lines.append("BYE")
    length += 1
    if 3 > max_name_length:
        max_name_length = 3

random.shuffle(lines)

weeks = []
for i in range(length - 1):
    week = [(lines[i], lines[length - 1 - i]) for i in range(length // 2)]
    weeks.append(week)
    lines = lines[:1] + lines[2:] + lines[1:2]

random.shuffle(weeks)

for i, week in enumerate(weeks):
    week_label = "Week " + str(i + 1) + " "
    print("\033[1;31m" + week_label.ljust(max_name_length * 2 + 3, "=") + "\033[0m")
    for meeting in week:
        print(meeting[0].rjust(max_name_length), ":", meeting[1].ljust(max_name_length))
