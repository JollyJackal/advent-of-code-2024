from pathlib import Path

reports: list[list[int]] = []

input_file = Path(__file__).parent / "input.txt"
# input_file = Path(__file__).parent / "test_input.txt"
with input_file.open() as f:
    for line in f:
        report = line.split()
        reports.append([int(elem) for elem in report])

safe_reports = 0


def unsafe_index(report: list[int]) -> int | None:
    last_diff = None
    last_elem_idx = len(report) - 1
    for i, level in enumerate(report):
        if i == last_elem_idx:
            return None
        else:
            diff = level - report[i + 1]

            if (
                last_diff is not None and
                (diff * last_diff) < 0
            ):
                return i  # unsafe, one ascending, one descending

            if (
                diff == 0 or
                diff > 3 or
                diff < -3
            ):
                return i  # unsafe

            last_diff = diff


for report in reports:
    unsafe_idx = unsafe_index(report)
    if unsafe_idx is None:
        safe_reports += 1
        continue

    report_copy = report[:]
    del report_copy[unsafe_idx]
    if unsafe_index(report_copy) is None:
        safe_reports += 1
        continue

    report_copy = report[:]
    if unsafe_idx > 0:
        del report_copy[unsafe_idx - 1]
        if unsafe_index(report_copy) is None:
            safe_reports += 1
            continue

    report_copy = report[:]
    if unsafe_idx < len(report) - 1:
        del report_copy[unsafe_idx + 1]
        if unsafe_index(report_copy) is None:
            safe_reports += 1
            continue

print(safe_reports)
