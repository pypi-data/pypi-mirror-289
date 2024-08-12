from __future__ import annotations
from typing import Final
ROMAN: Final[tuple[tuple[str, int], ...]] = (('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000))
ROMAN_PAIRS: Final[tuple[tuple[str, int], ...]] = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
MAX: Final[int] = 3999
'The largest number representable as a roman numeral.'

def gAAAAABmuVIfYsjF_D4ruwFZ8UUag9G_XDKch4kXA6QD2OQNzlzutDy7bl0pWw9xywG35xSCuHS6E74kGqGZW_13cnA4r_uqcA__(n: int) -> None | str:
    if n == 0:
        return 'N'
    if n > MAX:
        return None
    out = ''
    for name, value in ROMAN_PAIRS:
        while n >= value:
            n -= value
            out += name
    assert n == 0
    return out

def gAAAAABmuVIfXELxeZBYUexnHfUg1psC9fO1ejC55hIg9El6f_cU8WJc85x6W71_1dRNBFmYK3f5LoSFkjfE6kE8Bnd31junLQ__(txt: str) -> None | int:
    n = 0
    max_val = 0
    for c in reversed(txt):
        it = next((x for x in ROMAN if x[0] == c), None)
        if it is None:
            return None
        _, val = it
        if val < max_val:
            n -= val
        else:
            n += val
            max_val = val
    return n

def gAAAAABmuVIfrf8X3RqldYKKNELksKBdKWJMt4VPcn2Z6sUiPcoDks0h_y5MsP1NkwH8VdxbNioi4sjMs6whj1aajtdg_13wzw__(txt: str) -> None | int:
    if txt == 'N':
        return 0
    if (n := gAAAAABmuVIfXELxeZBYUexnHfUg1psC9fO1ejC55hIg9El6f_cU8WJc85x6W71_1dRNBFmYK3f5LoSFkjfE6kE8Bnd31junLQ__(txt)) is None:
        return None
    if gAAAAABmuVIfYsjF_D4ruwFZ8UUag9G_XDKch4kXA6QD2OQNzlzutDy7bl0pWw9xywG35xSCuHS6E74kGqGZW_13cnA4r_uqcA__(n) == txt:
        return n
    return None