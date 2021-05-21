def score(speed: int, accuracy: float, difficulty: int):
    norm_cpm = speed / 360
    norm_acc = accuracy / 100
    norm_dif = difficulty / 10
    k = (norm_cpm * (norm_acc + 1) + 1) ** (norm_dif ** 0.05 + (0.1 / norm_cpm)) - 1 - norm_cpm
    return round(k * 100)
