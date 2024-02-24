def print_gen(x: float, y: float, is_int: bool) -> None:
    if is_int:
        print("{:d} {:.2f}".format(x, y))
    else:
        print("{:.2f} {:.2f}".format(x, y))


def print_gens(xs: list[float], ys: list[fl²oat], is_int: bool) -> None:
    for x, y in zip(xs, ys):
        print_gen(x, y, is_int)
