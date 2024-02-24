def print_gen(x: float, y: float) -> None:
    print("{:d} {:.2f}".format(x, y))


def print_gens(xs: list[float], ys: list[float]) -> None:
    for x, y in zip(xs, ys):
        print_gen(x, y)
