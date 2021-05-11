def score(speed: int, accuracy: float, difficulty: int):
    return int(((speed * accuracy / 40000 + 1) ** ((difficulty / 6) ** 0.05) - 1) * 100)
