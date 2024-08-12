from __future__ import annotations
import re
from typing import Callable, Literal
from typing_extensions import TypeAlias
from rst_fast_parse.core import gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_, gAAAAABmuVIfanHDr_DkOsfdtlLwNVSLjxE_lmhdlo_dWcJ6jNpVRkjsuu9j2TJrRXBxJ_CvimAiNYWtIjjwYJ3Cc0rn35_H1w__, gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_, gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__
from rst_fast_parse.elements import ListElement, ListItemElement
from rst_fast_parse._hijklmn.block import gAAAAABmuVIfUowKUg8MzT6fs_NKm5YrdEdLvlAZ6gkXtVOZ5MWoaCiE9QBwyXARRUJvhl3PsKRZK1DNJJDZuICYZxMrIcxx4A__
from rst_fast_parse.source import gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__
from rst_fast_parse.utils.diagnostics import gAAAAABmuVIf5_jpL3d0xe3TQK6anR2EKlj5nhNserDOdUxbttLdKqbaeAybrlGvZ9LEiPUHOLs9youHdAAMatj8dfRTLkPFO_snaAjYhoPpj_C_FplgNJI_
from rst_fast_parse.utils.roman_numerals import gAAAAABmuVIfrf8X3RqldYKKNELksKBdKWJMt4VPcn2Z6sUiPcoDks0h_y5MsP1NkwH8VdxbNioi4sjMs6whj1aajtdg_13wzw__

def gAAAAABmuVIfa3vfUUSnPxu14e_fA6NKN2N0wSHOVNS7YnDYNCWutsKzUBU8ZR5M0PNxKuQyhoUukvAYH9i8LdqaL6LqoHBp2puLqS_MZ8POwJbhHL9Srak_(source: gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__, parent: gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__, diagnostics: gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_, context: gAAAAABmuVIfanHDr_DkOsfdtlLwNVSLjxE_lmhdlo_dWcJ6jNpVRkjsuu9j2TJrRXBxJ_CvimAiNYWtIjjwYJ3Cc0rn35_H1w__, /) -> gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_:
    if (init_line := source.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__) is None:
        return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIflyJJjUongu_6DQvTNEStLlrdGg7Tgaxg62ePuVW6ZFuC36P4oEJ34kIf_TkN0JBkJwqf7cAwOGE_B0LZqJzVLw__
    if (result := gAAAAABmuVIfXqq6NKM7f9CMkfw_Zef0L7Cu3WM5yG4_3wSvrX2wsdkeMpOHGJSG40aYrCpJoNv78tZqF_psTvtE96fi3wCSzWUqhiCrL_0CtiPyaJd1T0E_(init_line.content)) is None:
        return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf_a25Qj_GkfWtn_mkZHayuE0P0_yNO6t3e3ERR4eciDjL1LW_ET7DN6NQ_8BOLRK4dFzMzHRpaC1w2GCo8YCkFA__
    init_format, init_type, init_ordinal, _ = result
    last_auto = init_type == 'auto'
    last_ordinal: int | None = None
    if init_type == 'auto':
        init_type = 'arabic'
    if (next_line := source.gAAAAABmuVIfBt_62JEN_NkrWsLJ_IAGZt_oKfk3IglHE0_FrJPMWtVik4Xf75q410Jngefj7Xir6RFZ3KdWwUk8dqarJaevVQ__()) and (not next_line.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__) and next_line.content[:1].strip() and (not gAAAAABmuVIfXqq6NKM7f9CMkfw_Zef0L7Cu3WM5yG4_3wSvrX2wsdkeMpOHGJSG40aYrCpJoNv78tZqF_psTvtE96fi3wCSzWUqhiCrL_0CtiPyaJd1T0E_(next_line.content)):
        return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf_a25Qj_GkfWtn_mkZHayuE0P0_yNO6t3e3ERR4eciDjL1LW_ET7DN6NQ_8BOLRK4dFzMzHRpaC1w2GCo8YCkFA__
    items: list[ListItemElement] = []
    while (gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__ := source.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__):
        if gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__:
            source.gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__()
            continue
        if (result := gAAAAABmuVIfXqq6NKM7f9CMkfw_Zef0L7Cu3WM5yG4_3wSvrX2wsdkeMpOHGJSG40aYrCpJoNv78tZqF_psTvtE96fi3wCSzWUqhiCrL_0CtiPyaJd1T0E_(gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.content, init_type)) is not None:
            eformat, etype, next_ordinal, char_offset = result
            if eformat != init_format or (etype != 'auto' and (etype != init_type or last_auto or (last_ordinal is not None and next_ordinal != last_ordinal + 1))):
                source.gAAAAABmuVIfPW0BtsCJcRQmCEwEzU5ZKQShiA33Q8gnGVUFdlWiwg32f5e_xbArUA7m_CRx9xgk_OdUS_V5j_3lhtopw7Mssw__()
                break
            if len(gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.content) > char_offset:
                content = source.gAAAAABmuVIfKowbzJQWcIoqCreTiESQI_JAeTZtsck8bu0_D5kKnU5lEXcjJ1h6mrKbTwuhtYqmxOt62o3YIUQxSJOTpEK5zd7NoeBHDGhpRtx_qrZ9vXg_(char_offset, always_first=True, advance=True)
            else:
                content = source.gAAAAABmuVIfMmNjQaTNA5H0Iq0fJvcEHk2FfmwFAb7cVjARLRwAZR_FIxZLBWf7iA9YdQcaCpxdp5ZFhTEsGWMaIFtV8SFH1Hs1FFhGzdjGP_L8qW1kuhA_(first_indent=char_offset, advance=True)
            list_item = ListItemElement((gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.line, gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.line if content.gAAAAABmuVIfMn8K7QZmUIjVcVlv1WC_Ci3h7ngYNG_I3wanrkeYE_isiAGlmCVyiI_5nA73AqYnYhP1Xh1njfjCR1_g5ZFrGg__ is None else content.gAAAAABmuVIfMn8K7QZmUIjVcVlv1WC_Ci3h7ngYNG_I3wanrkeYE_isiAGlmCVyiI_5nA73AqYnYhP1Xh1njfjCR1_g5ZFrGg__.line))
            items.append(list_item)
            context.gAAAAABmuVIf_PwOm7Pp40eA1eV0Q5AYKRkV_MKySOtmIWEonuuP8hiLYo3SqjupoxuURTLDtLIiZv7YkUWLiTJaN3Anc_D8Jw__(content, list_item, diagnostics)
            last_auto = etype == 'auto'
            last_ordinal = next_ordinal
            source.gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__()
        else:
            source.gAAAAABmuVIfPW0BtsCJcRQmCEwEzU5ZKQShiA33Q8gnGVUFdlWiwg32f5e_xbArUA7m_CRx9xgk_OdUS_V5j_3lhtopw7Mssw__()
            break
    if items:
        parent.append(ListElement('enum_list', items))
        gAAAAABmuVIf5_jpL3d0xe3TQK6anR2EKlj5nhNserDOdUxbttLdKqbaeAybrlGvZ9LEiPUHOLs9youHdAAMatj8dfRTLkPFO_snaAjYhoPpj_C_FplgNJI_(diagnostics, source, 'Enumerated list')
    return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf26PxlIKRwpnbh3_5RJ8X8v5UqKh26G7FkgbijHc1wjZRx1ymoelyoYHqWOO9yzuu8KYjP045HyQ0RG6USv5xJg__
_ParenType: TypeAlias = Literal['parens', 'rparen', 'period']
_EnumType: TypeAlias = Literal['auto', 'arabic', 'loweralpha', 'upperalpha', 'lowerroman', 'upperroman']
gAAAAABmuVIf9tkZ4Z_d8NIUoWxO_xsYhrrVDwtALW4Cp7wI0V_XTNRakbPnBfm9F9_fiyWXWxWockLebus65__Q8MR_999OfCCJncRCITkN5sdmvBPIH50_: dict[_EnumType, tuple[str, _EnumType]] = {'auto': ('^[0-9]+$', 'arabic'), 'arabic': ('^[0-9]+$', 'arabic'), 'loweralpha': ('^[a-z]$', 'loweralpha'), 'upperalpha': ('^[A-Z]$', 'upperalpha'), 'lowerroman': ('^[ivxlcdm]+$', 'lowerroman'), 'upperroman': ('^[IVXLCDM]+$', 'upperroman')}
gAAAAABmuVIfs4cT_6aZD8UufPI9F8hITBnDE3MskAL5aR6Oq_Dd0izHgdAg1mgWrpVdCFKqmbx_N9IasEjKVG8zvPVmwjkS5w__: tuple[tuple[str, _EnumType], ...] = (('^[0-9]+$', 'arabic'), ('^[a-z]$', 'loweralpha'), ('^[A-Z]$', 'upperalpha'), ('^[ivxlcdm]+$', 'lowerroman'), ('^[IVXLCDM]+$', 'upperroman'))
gAAAAABmuVIfLPhZFWl4kIjQWGHkyFeoArs6eI7GWyN2GLSrU_d_nkysqn_M96GycYowoBQa9ilkprHch6rbmZ7G5aTp16_NPm6l0tyahGavfnLsXNkzTpw_: dict[_EnumType, Callable[[str], int | None]] = {'auto': lambda t: 1, 'arabic': int, 'loweralpha': lambda t: ord(t) - ord('a') + 1, 'upperalpha': lambda t: ord(t) - ord('A') + 1, 'lowerroman': lambda t: gAAAAABmuVIfrf8X3RqldYKKNELksKBdKWJMt4VPcn2Z6sUiPcoDks0h_y5MsP1NkwH8VdxbNioi4sjMs6whj1aajtdg_13wzw__(t.upper()), 'upperroman': lambda t: gAAAAABmuVIfrf8X3RqldYKKNELksKBdKWJMt4VPcn2Z6sUiPcoDks0h_y5MsP1NkwH8VdxbNioi4sjMs6whj1aajtdg_13wzw__(t)}

def gAAAAABmuVIfXqq6NKM7f9CMkfw_Zef0L7Cu3WM5yG4_3wSvrX2wsdkeMpOHGJSG40aYrCpJoNv78tZqF_psTvtE96fi3wCSzWUqhiCrL_0CtiPyaJd1T0E_(line: str, expected: None | _EnumType=None) -> None | tuple[_ParenType, _EnumType, int, int]:
    if not (match := re.match(gAAAAABmuVIfUowKUg8MzT6fs_NKm5YrdEdLvlAZ6gkXtVOZ5MWoaCiE9QBwyXARRUJvhl3PsKRZK1DNJJDZuICYZxMrIcxx4A__, line)):
        return None
    fmt: _ParenType
    for fmt in ('parens', 'rparen', 'period'):
        if (submatch := match.group(fmt)):
            text: str = submatch[:-1]
            if fmt == 'parens':
                text = text[1:]
            break
    else:
        raise RuntimeError(f'enumerator format not matched: {line!r}')
    sequence: None | _EnumType = None
    if text == '#':
        sequence = 'auto'
    elif expected is not None:
        regex, result = gAAAAABmuVIf9tkZ4Z_d8NIUoWxO_xsYhrrVDwtALW4Cp7wI0V_XTNRakbPnBfm9F9_fiyWXWxWockLebus65__Q8MR_999OfCCJncRCITkN5sdmvBPIH50_[expected]
        if re.match(regex, text):
            sequence = result
    elif text == 'i':
        sequence = 'lowerroman'
    elif text == 'I':
        sequence = 'upperroman'
    if sequence is None:
        for regex, result in gAAAAABmuVIfs4cT_6aZD8UufPI9F8hITBnDE3MskAL5aR6Oq_Dd0izHgdAg1mgWrpVdCFKqmbx_N9IasEjKVG8zvPVmwjkS5w__:
            if re.match(regex, text):
                sequence = result
                break
        else:
            raise RuntimeError(f'enumerator sequence not matched: {text!r}')
    if (ordinal := gAAAAABmuVIfLPhZFWl4kIjQWGHkyFeoArs6eI7GWyN2GLSrU_d_nkysqn_M96GycYowoBQa9ilkprHch6rbmZ7G5aTp16_NPm6l0tyahGavfnLsXNkzTpw_[sequence](text)) is None:
        return None
    return (fmt, sequence, ordinal, match.end(0))