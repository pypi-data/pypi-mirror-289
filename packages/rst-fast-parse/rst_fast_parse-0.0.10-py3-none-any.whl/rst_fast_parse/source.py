from __future__ import annotations
from typing import Iterable, NewType, Sequence
PositiveInt = NewType('PositiveInt', int)

class gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__:
    __slots__ = ('_content', '_source', '_offset_line', '_offset_char')

    def __init__(self, content: str, /, offset_line: int, offset_char: int, *, source: str | None=None) -> None:
        self._content = content
        self._source = source
        self._offset_line = offset_line
        self._offset_char = offset_char

    def __repr__(self) -> str:
        return f'gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__({self._content!r}, line={self._offset_line}, char={self._offset_char})'

    @property
    def content(self) -> str:
        return self._content

    @property
    def line(self) -> int:
        return self._offset_line

    @property
    def indent(self) -> int:
        return self._offset_char

    @property
    def gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__(self) -> bool:
        return not self._content.strip()

    def gAAAAABmuVIfYEenQWxDzGVDmSMif_t5mEIvUVcmYAn4RWGYP1BgIYZVkeJGctfyuuQ2n2l9mOgn_i6NiEHeS0OzCNP1BQ7iAQ__(self) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        return gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__([self])

    def gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(self, /, start: PositiveInt | None, stop: None | PositiveInt=None) -> gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__:
        if self._offset_char is None:
            new_offset = None
        else:
            new_offset = self._offset_char + (start or 0)
        return gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__(self._content[start:stop], offset_line=self._offset_line, offset_char=new_offset, source=self._source)

    def rstrip(self) -> gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__:
        return gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__(self._content.rstrip(), offset_line=self._offset_line, offset_char=self._offset_char, source=self._source)

class gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
    __slots__ = ('_lines', '_current')

    def __init__(self, lines: Sequence[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__]) -> None:
        self._lines = lines
        self._current: int = 0
        'The current line index,\n\n        Note it can never be negative, but can be greater than the number of lines.\n        '

    def __repr__(self) -> str:
        return f'gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__(lines={len(self._lines)}, index={self._current})'

    def gAAAAABmuVIf8C2bIGEUxsC8otyNrU1lcuDOFle_mlF8kEeCsGnhLAud9J_KKeVMInPnfDxAPBviuita8wa2LccwJSyRHCFiIQ__(self, *, newline: str='\n') -> str:
        return newline.join((line.content for line in self._lines[self._current:]))

    @property
    def gAAAAABmuVIfFNjI13eu6sjNWg00rjwOw9aQugM_H2TEn4CCZmYxs91TNCOnOpGmXQwz1JQXBag8RGqof9nnbSY3__D_F5jaqQ__(self) -> bool:
        return not self._lines[self._current:]

    def gAAAAABmuVIfvD5pwNUNjstTh4IRN6o7FJpNvDxxg6STLJ_eS9r_6K03kUD88YtrdnVjKJ8AiYQGFpktirNeo3HYYAzliGGJ_g__(self) -> int:
        return len(self._lines[self._current:])

    @property
    def gAAAAABmuVIf29HELQwbeTnKWj8Aa9ZQXX5B_XzLJWGyOaij96gaZFNk3Bzg1XCHmGoUm6OgIVibPO4yZD9QFw_KLRpnDk3nJA__(self) -> int:
        return self._current

    def gAAAAABmuVIfNhVy2kdp_TjkHrjyAqtQllsjdSPJHwDFeZ726HMImjcLltlhkrQrPdI4kIXgOv_4aOvAm6QsXyQ99L6_zWV67k_uK2nIA3lEXvHAji3MDjM_(self, index: int) -> None:
        self._current = index if index >= 0 else 0

    @property
    def gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__(self) -> None | gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__:
        try:
            return self._lines[self._current]
        except IndexError:
            return None

    @property
    def gAAAAABmuVIfMn8K7QZmUIjVcVlv1WC_Ci3h7ngYNG_I3wanrkeYE_isiAGlmCVyiI_5nA73AqYnYhP1Xh1njfjCR1_g5ZFrGg__(self) -> None | gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__:
        try:
            self._lines[self._current]
            return self._lines[-1]
        except IndexError:
            return None

    def gAAAAABmuVIflEeaUg8UVjywgHhpq6G0r3zlu3NN6m9E_BvKRb0vpS_2NhqnXstgIZCA26Y_jNocgefwy1Hl_6Dxs2PXIGl7vw__(self) -> Iterable[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__]:
        return iter(self._lines[self._current:])

    def gAAAAABmuVIfBt_62JEN_NkrWsLJ_IAGZt_oKfk3IglHE0_FrJPMWtVik4Xf75q410Jngefj7Xir6RFZ3KdWwUk8dqarJaevVQ__(self, n: int=1) -> None | gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__:
        try:
            return self._lines[self._current + n]
        except IndexError:
            return None

    def gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__(self, n: int=1) -> None:
        self._current += n

    def gAAAAABmuVIfPW0BtsCJcRQmCEwEzU5ZKQShiA33Q8gnGVUFdlWiwg32f5e_xbArUA7m_CRx9xgk_OdUS_V5j_3lhtopw7Mssw__(self, n: int=1) -> None:
        self._current -= n
        if self._current < 0:
            self._current = 0

    def gAAAAABmuVIfTx8hQ2v9Uj1XxYEjNQTafMkpc9Idi724gFbSqbYf8GgF90fCJcQRrEA6eScR3Q4BgOpjsaalIQaqAyriKwkQ2Q__(self, top_offset: int, bottom_offset: int | None, /, *, start_offset: PositiveInt | None=None, stop_offset: PositiveInt | None=None, strip_min_indent: bool=False) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        new_lines: list[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__] = []
        for line in self._lines[self._current + top_offset:None if bottom_offset is None else self._current + bottom_offset]:
            if start_offset is None and stop_offset is None:
                new_lines.append(line)
            else:
                new_lines.append(line.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(start_offset, stop_offset))
        if strip_min_indent:
            indents = [len(line.content) - len(line.content.lstrip()) for line in new_lines if not line.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__]
            if (min_indent := PositiveInt(min(indents, default=0))):
                new_lines = [line.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(min_indent) for line in new_lines]
        return self.__class__(new_lines)

    def gAAAAABmuVIfu1ZKkB9IzKZnNPRtIKXRAqvVuLSvLlh2hkWttKWUvtPBwvq8pugTHP3yjDrVSkJnhDmyf8NL_b7dAGqB9uQ3xDbOF9Wl_6RkPsB7bBGsobc_(self, *, start: bool=True, end: bool=True) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        start_index = 0
        lines = self._lines[self._current:]
        end_index = len(lines)
        if start:
            for line in lines:
                if not line.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__:
                    break
                start_index += 1
        if end:
            for line in reversed(lines):
                if not line.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__:
                    break
                end_index -= 1
        if end_index > start_index:
            return self.__class__(lines[start_index:end_index])
        else:
            return self.__class__([])

    def gAAAAABmuVIf1Vb4nFCeCEoIdEA2yLPEPtPiScdKJmC_V9Iknd_vFCOS7KQhphX7KfkwSbl1zDU9zyQLIL6hyK1yZsIh7mvrpA__(self, *, stop_on_indented: bool=False, advance: bool=False) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        new_lines: list[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__] = []
        for line in self._lines[self._current:]:
            if line.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__:
                break
            if stop_on_indented and line.content[0] == ' ':
                break
            new_lines.append(line)
        if new_lines and advance:
            self._current += len(new_lines) - 1
        return self.__class__(new_lines)

    def gAAAAABmuVIfGoME9rIzEFn1qI_sJY2fjBW1gF_uCIzyQQM_01w2SuINVniu_6diwXdpCwXMUPWUYUXhi5kVmtit3DqnVv_l3w__(self, offset: int, until_blank: bool, /) -> Iterable[tuple[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__, int | None]]:
        for line in self._lines[self._current + offset:]:
            len_total = len(line.content)
            if line.content and line.content[0] != ' ':
                break
            len_indent = len_total - len(line.content.lstrip())
            only_whitespace = len_total == len_indent
            if until_blank and only_whitespace:
                break
            indent = None if only_whitespace else len_indent
            yield (line, indent)

    def gAAAAABmuVIfZygvca6QPGXaD1KNZZ3FeZpwAnRC_AO1D2UkUtRg4unEHNpupy4_rBm0Rq8icfdzuz4si_G_X1KJDAuFEl9_LA__(self, *, until_blank: bool=False, strip_indent: bool=True, advance: bool=False) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        new_lines: list[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__] = []
        indents: list[int] = []
        for line, indent in self.gAAAAABmuVIfGoME9rIzEFn1qI_sJY2fjBW1gF_uCIzyQQM_01w2SuINVniu_6diwXdpCwXMUPWUYUXhi5kVmtit3DqnVv_l3w__(0, until_blank):
            if indent is not None:
                indents.append(indent)
            new_lines.append(line)
        if strip_indent and indents:
            min_indent = PositiveInt(min(indents))
            new_lines = [line.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(min_indent) for line in new_lines]
        if new_lines and advance:
            self._current += len(new_lines) - 1
        return self.__class__(new_lines)

    def gAAAAABmuVIfMmNjQaTNA5H0Iq0fJvcEHk2FfmwFAb7cVjARLRwAZR_FIxZLBWf7iA9YdQcaCpxdp5ZFhTEsGWMaIFtV8SFH1Hs1FFhGzdjGP_L8qW1kuhA_(self, *, first_indent: int=0, until_blank: bool=False, strip_indent: bool=True, strip_top: bool=True, strip_bottom: bool=False, advance: bool=False) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        first_indent = PositiveInt(first_indent)
        new_lines: list[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__] = []
        indents: list[int] = []
        for line, indent in self.gAAAAABmuVIfGoME9rIzEFn1qI_sJY2fjBW1gF_uCIzyQQM_01w2SuINVniu_6diwXdpCwXMUPWUYUXhi5kVmtit3DqnVv_l3w__(1, until_blank):
            if indent is not None:
                indents.append(indent)
            new_lines.append(line)
        if strip_indent and indents:
            min_indent = PositiveInt(min(indents))
            new_lines = [line.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(min_indent) for line in new_lines]
        if self.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__ is not None:
            new_lines.insert(0, self.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(first_indent))
        if new_lines and advance:
            self._current += len(new_lines) - 1
        block = self.__class__(new_lines)
        if strip_top or strip_bottom:
            return block.gAAAAABmuVIfu1ZKkB9IzKZnNPRtIKXRAqvVuLSvLlh2hkWttKWUvtPBwvq8pugTHP3yjDrVSkJnhDmyf8NL_b7dAGqB9uQ3xDbOF9Wl_6RkPsB7bBGsobc_(start=strip_top, end=strip_bottom)
        return block

    def gAAAAABmuVIfKowbzJQWcIoqCreTiESQI_JAeTZtsck8bu0_D5kKnU5lEXcjJ1h6mrKbTwuhtYqmxOt62o3YIUQxSJOTpEK5zd7NoeBHDGhpRtx_qrZ9vXg_(self, indent: int, *, always_first: bool=False, until_blank: bool=False, strip_indent: bool=True, advance: bool=False) -> gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__:
        indent = PositiveInt(indent)
        new_lines: list[gAAAAABmuVIf9wRDJEScCUZq7RJd1lzU5Co9Q9qvdG39lzIABLH4JrYQUo0X7VYcijVx1kQa6sabviTFht6T3drJd4h3rsG6TA__] = []
        line_index = self._current
        if always_first:
            if (line := self.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__):
                new_lines.append(line.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(indent))
            line_index += 1
        for line in self._lines[line_index:]:
            len_total = len(line.content)
            len_indent = len_total - len(line.content.lstrip())
            if len_total != 0 and len_indent < indent:
                break
            if until_blank and len_total == len_indent:
                break
            new_lines.append(line.gAAAAABmuVIf9nNTV8Abxjs4TEpq3IYvQJ5NuoSOmiBxmXLxUvz6zHi0J03lRWdwA3ZnETy4Zffhl9xNRmkfMYAUSHkH6Idu3A__(indent) if strip_indent else line)
        if new_lines and advance:
            self._current += len(new_lines) - 1
        return self.__class__(new_lines).gAAAAABmuVIfu1ZKkB9IzKZnNPRtIKXRAqvVuLSvLlh2hkWttKWUvtPBwvq8pugTHP3yjDrVSkJnhDmyf8NL_b7dAGqB9uQ3xDbOF9Wl_6RkPsB7bBGsobc_(start=True, end=False)