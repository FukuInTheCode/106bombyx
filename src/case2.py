from src.calc_gens import calc_gens
from src.print_gens import print_gens


def do_case2(n: float, i0: int, i1: int) -> int:
    ks = [(100 + i) / 100 for i in range(301)]

    for k in ks:
        print_gens([k for _ in range(i1 - i0 + 1)], calc_gens(n, k, i0, i1), False)
    return 0
