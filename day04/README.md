# Day 4: Giant Squid

Check bingo conditions across multiple boards. Read the [full problem description](https://adventofcode.com/2021/day/4).

## Strategy

Store metainformation about which numbers have been seen in an extra column/row of the board matrix. Similarly, store the current score (the sum of remaining numbers) in the remaining free position:

```
Bingo Board

23  5  7 13  4 |  0  <- right margin stores
 2 12 16 11 39 |  1     numbers seen
14 32 45  6 15 |  0
 9  8 11 35 53 |  0
44 19 65 63  1 |  1
---------------+----
 0  0  0  0  2 | 147 <- score
```
