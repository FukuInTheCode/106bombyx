from src.calc_gens import calc_gens
from src.print_gens import print_gens


def do_case1(n: int, k: int) -> int:
    print_gens([i for i in range(1, 101)], calc_gens(n, k, 1, 100))
    return 0
