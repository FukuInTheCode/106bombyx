from src.calc_gens import calc_gens
from src.print_gens import print_gens


def do_case1(n: float, k: float) -> int:
    print_gens([i for i in range(1, 101)], calc_gens(n, k, 1, 100), True)
    return 0
