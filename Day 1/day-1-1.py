from pathlib import Path

list_one = []
list_two = []
input_file = Path(__file__).parent / "input.txt"
with input_file.open() as f:
    for line in f:
        elems = line.split()
        list_one.append(int(elems[0]))
        list_two.append(int(elems[1]))

list_one.sort()
list_two.sort()

total_distance = 0

for left, right in zip(list_one, list_two):
    distance = abs(right - left)
    total_distance += distance

print(total_distance)
