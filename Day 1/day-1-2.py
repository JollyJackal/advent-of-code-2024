from pathlib import Path

list_one = []
list_two = []
input_file = Path(__file__).parent / "input.txt"
with input_file.open() as f:
    for line in f:
        elems = line.split()
        list_one.append(int(elems[0]))
        list_two.append(int(elems[1]))

similarity_score = 0

for left in list_one:
    num_matches = len([right for right in list_two if right == left])
    similarity = left * num_matches
    similarity_score += similarity

print(similarity_score)
