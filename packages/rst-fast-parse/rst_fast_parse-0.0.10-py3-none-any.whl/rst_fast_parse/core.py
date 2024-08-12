from __future__ import annotations
from enum import Enum
from typing import Protocol, Sequence
from rst_fast_parse.diagnostics import Diagnostic, DiagnosticList
from rst_fast_parse.elements import BasicElementList, ElementBase, ElementListBase
from rst_fast_parse.source import gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__

class gAAAAABmuVIfanHDr_DkOsfdtlLwNVSLjxE_lmhdlo_dWcJ6jNpVRkjsuu9j2TJrRXBxJ_CvimAiNYWtIjjwYJ3Cc0rn35_H1w__:

    def __init__(self, block_parsers: Sequence[gAAAAABmuVIfVha6G67z1s3rWuXlPoPJXCwGHxsniKYepTcKKbezeqqSvz_VXAD6OzGW_vQTK5qHtCT1j9KFZU_ujzcT2sf2MQ__], *, gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__: bool=True) -> None:
        self._gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__ = gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__
        self._block_parsers = block_parsers

    @property
    def gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__(self) -> bool:
        return self._gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__

    def gAAAAABmuVIf9xwq70eSeWWPXDe93ixzBJC7a8weQ2_i_NZ9vZkDqYI2b0eXslg25raKyC1lEeLU9eMIiaFB8UWPp8wu9stR7g__(self, source: gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__) -> tuple[ElementListBase, DiagnosticList]:
        end_of_file = False
        parent = BasicElementList()
        diagnostics: list[Diagnostic] = []
        while not end_of_file:
            for parser in self._block_parsers:
                result = parser(source, parent, diagnostics, self)
                if result == gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf26PxlIKRwpnbh3_5RJ8X8v5UqKh26G7FkgbijHc1wjZRx1ymoelyoYHqWOO9yzuu8KYjP045HyQ0RG6USv5xJg__:
                    break
                elif result == gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf_a25Qj_GkfWtn_mkZHayuE0P0_yNO6t3e3ERR4eciDjL1LW_ET7DN6NQ_8BOLRK4dFzMzHRpaC1w2GCo8YCkFA__:
                    continue
                elif result == gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIflyJJjUongu_6DQvTNEStLlrdGg7Tgaxg62ePuVW6ZFuC36P4oEJ34kIf_TkN0JBkJwqf7cAwOGE_B0LZqJzVLw__:
                    end_of_file = True
                    break
                else:
                    raise RuntimeError(f'Unknown parser result: {result!r}')
            else:
                if (line := source.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__):
                    raise RuntimeError(f'No parser matched line {line.line}: {line.content!r}')
            source.gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__()
            if source.gAAAAABmuVIfFNjI13eu6sjNWg00rjwOw9aQugM_H2TEn4CCZmYxs91TNCOnOpGmXQwz1JQXBag8RGqof9nnbSY3__D_F5jaqQ__:
                break
        return (parent, diagnostics)

    def gAAAAABmuVIf_PwOm7Pp40eA1eV0Q5AYKRkV_MKySOtmIWEonuuP8hiLYo3SqjupoxuURTLDtLIiZv7YkUWLiTJaN3Anc_D8Jw__(self, source: gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__, parent: gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__, diagnostics: gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_, /) -> None:
        old_gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__ = self._gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__
        try:
            self._gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__ = False
            end_of_file = False
            while not end_of_file:
                for parser in self._block_parsers:
                    result = parser(source, parent, diagnostics, self)
                    if result == gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf26PxlIKRwpnbh3_5RJ8X8v5UqKh26G7FkgbijHc1wjZRx1ymoelyoYHqWOO9yzuu8KYjP045HyQ0RG6USv5xJg__:
                        break
                    elif result == gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf_a25Qj_GkfWtn_mkZHayuE0P0_yNO6t3e3ERR4eciDjL1LW_ET7DN6NQ_8BOLRK4dFzMzHRpaC1w2GCo8YCkFA__:
                        continue
                    elif result == gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIflyJJjUongu_6DQvTNEStLlrdGg7Tgaxg62ePuVW6ZFuC36P4oEJ34kIf_TkN0JBkJwqf7cAwOGE_B0LZqJzVLw__:
                        end_of_file = True
                        break
                    else:
                        raise RuntimeError(f'Unknown parser result: {result!r}')
                else:
                    if (line := source.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__):
                        raise RuntimeError(f'No parser matched line {line.line}: {line.content!r}')
                source.gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__()
                if source.gAAAAABmuVIfFNjI13eu6sjNWg00rjwOw9aQugM_H2TEn4CCZmYxs91TNCOnOpGmXQwz1JQXBag8RGqof9nnbSY3__D_F5jaqQ__:
                    break
        finally:
            self._gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__ = old_gAAAAABmuVIfcXy2TjUGLvLZZFEAzfOae7n31X6IJPve_S2LXUEA4BI3_2ywyIak25h3FwN9fGRzkQP_9svVI0aPtcbqgu_iwg__

class gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_(Enum):
    gAAAAABmuVIf26PxlIKRwpnbh3_5RJ8X8v5UqKh26G7FkgbijHc1wjZRx1ymoelyoYHqWOO9yzuu8KYjP045HyQ0RG6USv5xJg__ = 0
    'The parser successfully matched the input.'
    gAAAAABmuVIf_a25Qj_GkfWtn_mkZHayuE0P0_yNO6t3e3ERR4eciDjL1LW_ET7DN6NQ_8BOLRK4dFzMzHRpaC1w2GCo8YCkFA__ = 1
    'The parser did not match the input.'
    gAAAAABmuVIflyJJjUongu_6DQvTNEStLlrdGg7Tgaxg62ePuVW6ZFuC36P4oEJ34kIf_TkN0JBkJwqf7cAwOGE_B0LZqJzVLw__ = 2
    'The parser reached the end of the file.'

class gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__(Protocol):

    def append(self, element: ElementBase) -> None:
        pass

class gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_(Protocol):

    def append(self, diagnostic: Diagnostic) -> None:
        pass

class gAAAAABmuVIfVha6G67z1s3rWuXlPoPJXCwGHxsniKYepTcKKbezeqqSvz_VXAD6OzGW_vQTK5qHtCT1j9KFZU_ujzcT2sf2MQ__(Protocol):

    def __call__(self, source: gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__, parent: gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__, diagnostics: gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_, context: gAAAAABmuVIfanHDr_DkOsfdtlLwNVSLjxE_lmhdlo_dWcJ6jNpVRkjsuu9j2TJrRXBxJ_CvimAiNYWtIjjwYJ3Cc0rn35_H1w__, /) -> gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_:
        pass