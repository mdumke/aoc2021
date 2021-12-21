"""Day 21: Dirac Dice, Part 1"""

class Player:
    def __init__(self, pos):
        self.pos = pos - 1
        self.score = 0

    def move(self, die):
        steps = sum(die.roll() for _ in range(3))
        self.pos = (self.pos + steps) % 10
        self.score += self.pos + 1


class Die:
    def __init__(self):
        self.count = 0
        self.i = -1

    def roll(self):
        self.count += 1
        self.i = (self.i + 1) % 100
        return self.i + 1


def play(p1, p2, die):
    p1.move(die)
    if p1.score >= 1000:
        return p1, p2, die
    else:
        return play(p2, p1, die)


if __name__ == '__main__':
    winner, loser, die = play(Player(4), Player(3), Die())
    print('part 1:', loser.score * die.count)

