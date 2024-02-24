def calc_gens(n: float, k: float, start: int, end: int) -> list[float]:
    sequence = [n]
    for i in range(start + 1, end + 1):
        sequence.append(calc_gen(k, sequence[-1]))
    return sequence


def calc_gen(k: float, last: float) -> float:
    return float(k * last * (1000 - last) / 1000)
