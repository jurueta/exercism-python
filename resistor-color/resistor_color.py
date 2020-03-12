colors_codex = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
                "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def color_code(color):
    return colors_codex[color]


def colors():
    return list(colors_codex.keys())
