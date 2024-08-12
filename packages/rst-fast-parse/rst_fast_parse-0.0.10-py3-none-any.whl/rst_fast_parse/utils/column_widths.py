from __future__ import annotations
from typing import Mapping
import unicodedata

def gAAAAABmuVIfAyBJPb66gOf3XfD9jTDiiyanpr3xqS8k48lJylul91ypdDhCq6NBNlocrZzXk3cg_iyFzYyIyDZPAgFvBrnrgg__(text: str) -> int:
    width = sum((_east_asian_widths[unicodedata.east_asian_width(c)] for c in text))
    width -= len(gAAAAABmuVIfcYV2mgMxtzSdqPpSZYkdmTx6G0XEFyHi19fGvVewOKzBRkt2uiLiY_fYIryjo4cZW35j0AGasRsRU4g9rMxL2HnMOj_shWVikSCZwofsjYI_(text))
    return width

def gAAAAABmuVIfcYV2mgMxtzSdqPpSZYkdmTx6G0XEFyHi19fGvVewOKzBRkt2uiLiY_fYIryjo4cZW35j0AGasRsRU4g9rMxL2HnMOj_shWVikSCZwofsjYI_(text: str) -> list[int]:
    return [i for i, c in enumerate(text) if unicodedata.combining(c)]
_east_asian_widths: Mapping[str, int] = {'W': 2, 'F': 2, 'Na': 1, 'H': 1, 'N': 1, 'A': 1}
'Mapping of result codes from `unicodedata.east_asian_width()` to character\ncolumn widths.'