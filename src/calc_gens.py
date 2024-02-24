def calc_gens(n: float, k: float, start: int, end: int) -> list[float]:
    all_sequence = calc_all_gens(k, n, end)
    sequence = all_sequence[start - 1:end]
    return sequence


def calc_all_gens(k: float, n: float, end: int) -> list[float]:
    all_sequence = [n]
    for i in range(1, end):
        all_sequence.append(calc_gen(k, all_sequence[-1]))
    return all_sequence


def calc_gen(k: float, last: float) -> float:
    return float(k * last * (1000 - last) / 1000)
