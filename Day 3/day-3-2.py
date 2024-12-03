from pathlib import Path


def get_mul(mul_candidate: str) -> int | None:
    res = mul_candidate.split(",", maxsplit=1)
    if (
        len(res) == 2 and
        res[0].isdigit() and
        res[1].isdigit() and
        len(res[0]) < 4 and
        len(res[1]) < 4
    ):
        return int(res[0]) * int(res[1])

    return None


def find_dont_idxs(line: str) -> list[tuple[int, bool]]:
    dont_idxs = []
    idx = line.find("don't()")
    while idx != -1:
        dont_idxs.append((idx, False))
        idx = line.find("don't()", idx + 1)

    return dont_idxs


def find_do_idxs(line: str) -> list[tuple[int, bool]]:
    do_idxs = []
    idx = line.find("do()")
    while idx != -1:
        do_idxs.append((idx, True))
        idx = line.find("do()", idx + 1)

    return do_idxs


def find_mul_idxs(line: str) -> list[tuple[int, int]]:
    mul_idxs = []
    idx = line.find("mul(")
    while idx != -1:
        close_idx = line.find(")", idx + 1)
        if close_idx != -1:
            slice = line[idx+4:close_idx]
            mul_res = get_mul(slice)
            if mul_res is not None:
                mul_idxs.append((idx, mul_res))
        idx = line.find("mul(", idx + 1)

    return mul_idxs


total_muls = 0
stack = []

input_file = Path(__file__).parent / "input.txt"
# input_file = Path(__file__).parent / "test_input_2.txt"
with input_file.open() as f:
    line = f.read()
    stack.extend(find_do_idxs(line))
    stack.extend(find_dont_idxs(line))
    stack.extend(find_mul_idxs(line))


stack.sort(key=lambda x: x[0])
print(f'{stack=}')
do_mul = True
for idx, val in stack:
    if isinstance(val, bool):
        do_mul = val
    elif do_mul:
        total_muls += val


print(total_muls)
