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
    for i, level in enumerate(report):
        if i == last_elem_idx:
            safe_reports += 1
        else:
            diff = level - report[i + 1]

            if (
                last_diff is not None and
                (diff * last_diff) < 0
            ):
                break  # unsafe, one ascending, one descending

            if (
                diff == 0 or
                diff > 3 or
                diff < -3
            ):
                break  # unsafe

            last_diff = diff

print(safe_reports)
