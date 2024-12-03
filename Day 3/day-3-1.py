from pathlib import Path


def get_mul(mul_candidate: str) -> tuple[int | None, str]:
    mul_res = None

    before, _, after = mul_candidate.partition(")")

    if after != '':
        # print(f'{after=}\n')
        # print(f'{before=}')
        _, _, bef_aft = before.rpartition("mul(")

        if bef_aft != '':
            res = bef_aft.split(",", maxsplit=1)
            if (
                len(res) == 2 and
                res[0].isdigit() and
                res[1].isdigit() and
                len(res[0]) < 4 and
                len(res[1]) < 4
            ):
                # print(f'{bef_aft=}\n')
                mul_res = int(res[0]) * int(res[1])

    return mul_res, after


total_muls = 0

input_file = Path(__file__).parent / "input.txt"
# input_file = Path(__file__).parent / "test_input.txt"
with input_file.open() as f:
    for line in f:
        line_copy = line[:]
        while line_copy != '':
            mul_res, line_copy = get_mul(line_copy)
            if mul_res is not None:
                total_muls += mul_res

print(total_muls)
