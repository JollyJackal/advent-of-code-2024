from pathlib import Path

reports: list[list[int]] = []

input_file = Path(__file__).parent / "input.txt"
with input_file.open() as f:
    for line in f:
        report = line.split()
        reports.append([int(elem) for elem in report])

safe_reports = 0

for report in reports:
    last_diff = None
    last_elem_idx = len(report) - 1
    first_error = True
    for i in range(len(report)):
        if i == last_elem_idx:
            safe_reports += 1
        else:
            diff = report[i] - report[i + 1]

            if (
                last_diff is not None and
                (diff * last_diff) < 0
            ):
                if first_error:
                    first_error = False
                    i = 0
                else:
                    break  # unsafe, one ascending, one descending

            if (
                diff == 0 or
                diff > 3 or
                diff < -3
            ):
                break  # unsafe

            last_diff = diff

print(safe_reports)


# for i in range(len(somelist) - 1, -1, -1):
#     element = somelist[i]
#     do_action(element)
#     if check(element):
#         del somelist[i]

# i = 0
# n = len(somelist)
# while i < n:
#     element = somelist[i]
#     do_action(element)
#     if check(element):
#         del somelist[i]
#         n = n - 1
#     else:
#         i = i + 1

# reversed(range(len(somelist)))
