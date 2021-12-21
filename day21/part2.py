"""Day 21: Dirac Dice, Part 2"""

from functools import lru_cache

@lru_cache(None)
def count_wins(p1, p1_score, p2, p2_score, player=1):
    if p1_score > 20: return (1, 0)
    if p2_score > 20: return (0, 1)

    wins1 = 0
    wins2 = 0

    for steps, n in ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)):
        if player == 1:
            pos = (p1 + steps) % 10
            score = pos + 1
            w1, w2 = count_wins(pos, p1_score + score, p2, p2_score, 2)
        if player == 2:
            pos = (p2 + steps) % 10
            score = pos + 1
            w1, w2 = count_wins(p1, p1_score, pos, p2_score + score, 1)
        wins1 += w1 * n
        wins2 += w2 * n

    return wins1, wins2


if __name__ == '__main__':
    player1 = 4
    player2 = 3

    print('part 2:', max(count_wins(player1-1, 0, player2-1, 0)))
