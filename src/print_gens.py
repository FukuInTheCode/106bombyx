def print_gen(x: int, y: int) -> None:
    print(x, y)


def print_gens(xs: list[int], ys: list[int]) -> None:
    for x, y in zip(xs, ys):
        print_gen(x, y)
