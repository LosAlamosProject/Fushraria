import noise, random

# TODO: napravi funkciju generate koja generise 2d platformer svet
# na noise algoritmu.

def generate(width : int = 69) -> list:
    heights = []

    points = 256
    span = 5.0
    startpos = random.randint(1,1000)

    for i in range(width):
        x = float(i) * span / points - 0.5 * span
        heights.append(noise.pnoise1(x + startpos + i) * 10)

    return heights