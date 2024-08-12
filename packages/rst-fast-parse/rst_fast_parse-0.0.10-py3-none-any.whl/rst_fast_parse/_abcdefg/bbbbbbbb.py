from __future__ import annotations
import re
from rst_fast_parse.core import gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_, gAAAAABmuVIfanHDr_DkOsfdtlLwNVSLjxE_lmhdlo_dWcJ6jNpVRkjsuu9j2TJrRXBxJ_CvimAiNYWtIjjwYJ3Cc0rn35_H1w__, gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_, gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__
from rst_fast_parse.elements import ListElement, ListItemElement
from rst_fast_parse._hijklmn.block import gAAAAABmuVIfPztc7YbmJhiG_pyETbnc5kylUbE6BGS51ntlOaBXyjQAvvz4bQxBLZ7J3op60kdVqgkWWONcWvAbYaAwBjreUD0g9A0V5SFKroV_cuE90Jo_
from rst_fast_parse.source import gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__
from rst_fast_parse.utils.diagnostics import gAAAAABmuVIf5_jpL3d0xe3TQK6anR2EKlj5nhNserDOdUxbttLdKqbaeAybrlGvZ9LEiPUHOLs9youHdAAMatj8dfRTLkPFO_snaAjYhoPpj_C_FplgNJI_

def gAAAAABmuVIfPlr__na8C_wq3KoS8rhM1Pkp3Wz5iBOVili0l6C33SIEJbmFbX1SNenvkGmeBwqf87NXHExi04FJEh3L_M4JNq0CkbHOTzPXU_Oej1aZVGw_(source: gAAAAABmuVIfn8_QoZZda_B1ee7ZSZOU9HYQ3WCA_RfcyKsUPfTrulwxfbLz_wAf1h3l5WJTwf8xOwzWW1SaFPNclPosK0zq7A__, parent: gAAAAABmuVIfN0l2TcdJP_L82Pdsk1CA_7f5myp0bAlzwyCicFleRAxfCC8S9b9oEjbjpJ1PlWSv56d6mzx6yK_VbsMFTV9lLg__, diagnostics: gAAAAABmuVIfZaVSbKyFlYJr0ekNr2t_Jrz7ijtSG_SjOCgPZnZzzo7KFR0Yh26ZqEgWw_08pVV2qINoQ5wCkn6BNf81oGst9zrcv_vlMHLSrh5i3DNOwNc_, context: gAAAAABmuVIfanHDr_DkOsfdtlLwNVSLjxE_lmhdlo_dWcJ6jNpVRkjsuu9j2TJrRXBxJ_CvimAiNYWtIjjwYJ3Cc0rn35_H1w__, /) -> gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_:
    if not (first_line := source.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__):
        return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIflyJJjUongu_6DQvTNEStLlrdGg7Tgaxg62ePuVW6ZFuC36P4oEJ34kIf_TkN0JBkJwqf7cAwOGE_B0LZqJzVLw__
    if not (match := re.match(gAAAAABmuVIfPztc7YbmJhiG_pyETbnc5kylUbE6BGS51ntlOaBXyjQAvvz4bQxBLZ7J3op60kdVqgkWWONcWvAbYaAwBjreUD0g9A0V5SFKroV_cuE90Jo_, first_line.content)):
        return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf_a25Qj_GkfWtn_mkZHayuE0P0_yNO6t3e3ERR4eciDjL1LW_ET7DN6NQ_8BOLRK4dFzMzHRpaC1w2GCo8YCkFA__
    symbol: str = match.group(1)
    items: list[ListItemElement] = []
    while (gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__ := source.gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__):
        if gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.gAAAAABmuVIfkFxbCqNYbRuFdouu_r6feqTsiw61cRZGCux2fLb9Cm7ZR6_3eOCL5erbwhbttfjBgD0K9AmIgM8asyDwVwvmXQ__:
            source.gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__()
            continue
        if (match := re.match(gAAAAABmuVIfPztc7YbmJhiG_pyETbnc5kylUbE6BGS51ntlOaBXyjQAvvz4bQxBLZ7J3op60kdVqgkWWONcWvAbYaAwBjreUD0g9A0V5SFKroV_cuE90Jo_, gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.content)):
            next_symbol: str = match.group(1)
            if next_symbol != symbol:
                source.gAAAAABmuVIfPW0BtsCJcRQmCEwEzU5ZKQShiA33Q8gnGVUFdlWiwg32f5e_xbArUA7m_CRx9xgk_OdUS_V5j_3lhtopw7Mssw__()
                break
            first_indent = match.end(0)
            if len(gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.content) > first_indent:
                content = source.gAAAAABmuVIfKowbzJQWcIoqCreTiESQI_JAeTZtsck8bu0_D5kKnU5lEXcjJ1h6mrKbTwuhtYqmxOt62o3YIUQxSJOTpEK5zd7NoeBHDGhpRtx_qrZ9vXg_(first_indent, always_first=True, advance=True)
            else:
                content = source.gAAAAABmuVIfMmNjQaTNA5H0Iq0fJvcEHk2FfmwFAb7cVjARLRwAZR_FIxZLBWf7iA9YdQcaCpxdp5ZFhTEsGWMaIFtV8SFH1Hs1FFhGzdjGP_L8qW1kuhA_(first_indent=first_indent, advance=True)
            list_item = ListItemElement((gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.line, gAAAAABmuVIfncMy6dT6FMHEGGwByexwJCKMmI3Fpu3qtKS5x69BWXw_3Cfe9SiBrWc_1S0ALqLCzbg8iMGdcj9gpfgGXAz_GA__.line if content.gAAAAABmuVIfMn8K7QZmUIjVcVlv1WC_Ci3h7ngYNG_I3wanrkeYE_isiAGlmCVyiI_5nA73AqYnYhP1Xh1njfjCR1_g5ZFrGg__ is None else content.gAAAAABmuVIfMn8K7QZmUIjVcVlv1WC_Ci3h7ngYNG_I3wanrkeYE_isiAGlmCVyiI_5nA73AqYnYhP1Xh1njfjCR1_g5ZFrGg__.line))
            items.append(list_item)
            context.gAAAAABmuVIf_PwOm7Pp40eA1eV0Q5AYKRkV_MKySOtmIWEonuuP8hiLYo3SqjupoxuURTLDtLIiZv7YkUWLiTJaN3Anc_D8Jw__(content, list_item, diagnostics)
            source.gAAAAABmuVIfTCJjbwXcXMJV5Dw8XlNnlPqU2RodK8L6jdsswNmMD_pQvWclTZ_rphENmPlQuU_iT7Hkoz_XP8H8iCrAzHrrng__()
        else:
            source.gAAAAABmuVIfPW0BtsCJcRQmCEwEzU5ZKQShiA33Q8gnGVUFdlWiwg32f5e_xbArUA7m_CRx9xgk_OdUS_V5j_3lhtopw7Mssw__()
            break
    if items:
        parent.append(ListElement('bullet_list', items))
        gAAAAABmuVIf5_jpL3d0xe3TQK6anR2EKlj5nhNserDOdUxbttLdKqbaeAybrlGvZ9LEiPUHOLs9youHdAAMatj8dfRTLkPFO_snaAjYhoPpj_C_FplgNJI_(diagnostics, source, 'Bullet list')
    return gAAAAABmuVIfPw1MR29_WhZNGCi3Q8FEwRFlbI3nEb7WlGptd1PJMphv9DnNDT5S5_bxEA4hslOwR4nYUYkVeZ5eGsJmzvASR4_HNP9Omkl_Jx_yXd9iRLs_.gAAAAABmuVIf26PxlIKRwpnbh3_5RJ8X8v5UqKh26G7FkgbijHc1wjZRx1ymoelyoYHqWOO9yzuu8KYjP045HyQ0RG6USv5xJg__