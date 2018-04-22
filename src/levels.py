import public
# A: White Block
# B: Black Block
# C: Grey Block
# D: White pit up
# E: White pit down
# F: Black pit up
# G: Black pit down
# H: Grey pit up
# I: Grey pit down
# J: Entrance
# K: Exit Black
# L: Exit White
# M: Exit Grey
# N: BreakableBlock Black
# O: BreakableBlock White
# P: BreakableBlock Grey
# Q: JumpPad Black
# R: JumpPad White
# S: JumpPad Grey
# .: RGBSphere


LEVELS = {
    0: ['For the curious user', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXAAAAAXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXAXXXXXAXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXAXXXXXXXAXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXAAAAXXXXXXXXXAXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXAXXXXXXXXXXXXAXXAAXXXXXXXXXXXXXXX",
            "XXXXXXXAXXXXXXXXXXXXAAAXAXXXXXXXXXXXXXXX",
            "XXXXXXXXAXXXXXAXXXXXXXXXAAAXXXXXXXXXXXXX",
            "XXXXXXXXXAXXXXAXXXXXXXXXXXAXXXXXXXXXXXXX",
            "XXXXXXXXXXAAXXXXXXXXXXXXXXAXXXXXXXXXXXXX",
            "XXXXXXXXXXXXAAXXXXXXXXXXXXAXXXXXXXXXXXXX",
            "XXXXXXXXXXXAXXXXXXXXXXXXXAXXXXXXXXXXXXXX",
            "XXXXXXXXXXXAAXXXXXXXXXXAAXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXAXXXXXXXXXAXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXAXXXXXXXXAXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXAXXXXXXXAXXXXXXXXXXXXXXXXXXX",
            "XXXJXXXXXXXXXAXAAXAAXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXAAXAAXXXXXXXXXXXXXXXXXXXXXX",
        ]],
    1: ['To Begin...', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXAXXXXXXXXXXXXXXBXXXXXXXXXXXX",
            "XXXXXXXXXXXXAXXXXXXXXXXXXXXBXXXXXXXXLXXX",
            "XXXJXXXXXXXXAXXXXXXXXXXXXXXBXXXXXXXXXXXX",
        ]],
    2: ['Elevate', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXBBXXXXXXBBBBB",
            "XXXXXXXXXXXXXXXXXXXXBBXXXXXXXXXXXXXXXBXX",
            "XXXXXXXXXXXXXAAXXXXXXXXXXXXXXXXXXXXXXBXX",
            "XJXXXXAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHBXX",
        ]],


    3: ['Risky Manuver', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXLXX",
            "AAAAAXXXXXXBBBBXXXXXXXXBBBBXXXXXXXXAAAAA",
            "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

    4: ['Reverse!', public.BLACK, True, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXCCCCXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXCCCCXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXCCXXXXXXXXXXXXXXXXXXX",
            "XXXAXXXXXXXXXXXXXXXCCXLXXXXXXXXXXXXXBXXX",
            "HHHHHHHHCXXXXXXXXJXCCXXXXXXXXXXCHHHHHHHH",
        ]],

    5: ['Altitude', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXDXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXAXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXAXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXQXXXAXXXXXXXX",
            "XXXXXXXXXXXXXXXXBBBBBXXXXXXBXXXAXXXXLXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXAXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXFAFXXXXXXX",
            "XXXJXXXXXRXBFFFFFFFFFFFFFFFFFFBABFFFFFFB",
        ]],

    6: ['Panic!', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBXXXBX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBXXXBX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBXOXBX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXNNNNNXXXXBXXXBX",
            "XXXXXXXXXXXXXXXXOOOOOXXXXXXXXXXXXXBXXXBX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBXLXBX",
            "XXXJXXXXRXXXCHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

    7: ['Booby Traps', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXBBBBXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXGGGGXXXXXXXXXXXXXXBBBXXXXX",
            "CCCCCCXXXXXXXXXXXXXXXXXXXDDXXXXXGGGXXXXX",
            "IIIIICXXXXXXXXXXXXXXXAAAAAAXXXXXXXQXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBBBCCXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XJXSXXXXXXXXXQXXXXXXXXXXXXXXXXXXXXXXXXLX",
            "CCCCCCXXXXXBBBXXXXXXXXXXXXXXXXXXXXXXXAAA",
            "CCCCCCHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

    8: ['Compartments', public.BLACK, True, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "CCCCCCCXXXXXXBBBBBBBBBBBXXXXXXXXXXXXXXXX",
            "CXXXXXCXXXXXXXXXXXGGGGGBXXXXXXXXXXXXXXXX",
            "CXXXXXXXXXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXX",
            "CXXJXXXXXXXXXXXXXXXXXXXBXXXXXXXXXXXXXXXX",
            "CCCCCCCXXXXXXXXXXQXXXXXBXXXXXXXXXXXXXXXX",
            "AXXXXXAXXXXXXBBBBBXXXXXBXXXXBXXXXXXXXXXX",
            "AXXXXXAXXXXXXXXXXBXXXXXBXXXXXXXXXXXXXXXX",
            "AXXKXXAXXXXXXXXXXBXXXXXBXXXXXXXXXXXXXXXX",
            "AXXXXXAXXXXXXXXXXAXXXXXAXXXXXXXXXXXXXXXX",
            "AXXXXXAXXXXXXXXXXAXXXXXADDDDDDDDDDDDDDDD",
            "AXXXXXAXXXXXXXXXXAXXXXXAAAAAAAAAAAAAAAAA",
            "XXXXXXAXXXXXXXXXXAOOOOOABBBBBBBBBBBBBBBB",
            "XXXXXXAXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXX",
            "XXXRXXAXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXX",
            "AAAAAAAXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXAXXXXXXBBBBBBBBBBBBBBBB",
            "XXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXXXXXXX",
            "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

    9: ['Tunnel Travel', public.BLACK, True, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXFFFFFFFFFFFF",
            "XXXXXXXXXXXXXXXXXAAAAAAAFXXXBBBBBBBBBBBB",
            "XXXXXXXXXXXXXXXXXEEEEEEEBXXXXXXXXXXAAAAA",
            "XXXXXXXXXXXXXXXXXXXXXXXXBXXXXXXXXXXXXXXX",
            "XXXCXXXXXXXXXXXXXSXXXXXXXXXXXXXXXXXXXLXX",
            "XXXCXXXXXAXXXCCCCCXXXXXXNNNNNNNNNNNAAAAA",
            "XXXCXXXXXAXXXXXXXCXXXXXXXXXXXXXXXXXXXXXX",
            "XXXCXXXXXAXXXXXXXCXXXXXXXXXXXXXXXXXXXXXX",
            "XXXCXXXXXXXXXFFFFCXXXXXXXXXXXXXXXXXXXXXX",
            "XXXCXXXRXXXXXBBBBCXXXXXXXXXXXXDDDDFFFFFF",
            "CCCCAAAAAAXXXXXXXCXXXXXXXXXXXBAAAABBBBBB",
            "BBBBXXXXXXXXXXXXXCXJXSXXXXXXXBXXXXGGGGGG",
            "XXXXXXXXXXXXXBBBBCCCCCXXXXXXXBXXXXXXXXXX",
            "XXXXXXXAAAXXXXXXXXXXXXXXXXXXXBXXXXXXXXXX",
            "BBBXXXXXXXXXXXXXXXXXXXXXXXXXXBBBBBBBBBBB",
            "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

    10: ['U-Turn', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXKXXXXXXXBXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXCCCXXXXXXBXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXBXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXBBBBXXXXBBBBBXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXAAAAXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXCXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXCXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXFFFFFCXRXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXCPPPPCCCCXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXBBXXXXCXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXBBXXXXCXXXXXXXXXXXRXXXXXX",
            "XXXXXXXXXXAAAXXBBXXXXCXXXXXXXXXXXCXXXXXX",
            "XXXXJXXXXXAAAXXBBXXXXCDDDDDDDDDDDDDDDDDD",
      ]],


      11: ['Time And Space', public.WHITE, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXMXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXAAAAAXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXBXXXBXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXBXXXBXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXBXXXBXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXBXRXBXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXCCCCCXXXXXXXXXXXXXXXXXX",
            "XXXBBBBBXXXBXXXXXXXAXXXXXXXXXXXXXXXXCXXX",
            "XXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXCXXX",
            "XXXXXXXXXXXXXXXXXXXAXXXXXXXXXXXXXXXXCXXX",
            "XXXXRXXXXXXXXXXXXXXCXXXXXXXXXXXXXJXXCXXX",
            "XXXCCCXXXXXXXXXXXXXCXXOOXXXXOOXXCCCCCXXX",
            "XXXXCXXXAAXXXXXXXXXCXXXXXXXXXXXXCXXXXXXX",
            "XXXXCXXXXXXXXBBBBXXCXXXXXXXXXXXXCXXXXXXX",
            "XXXXCXXXXXXXXXXXXXXCXXXXXXXXXXXXCXXXXXXX",
            "XXXXCHHHHHHHHHHHHHHCHHHHHHHHHHHHCXXXXXXX",
        ]],

      12: ['CliffStrider', public.BLACK, True, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXBBBBBXXXXXXXXXXXXXXXXXXAAAXXXXXXX",
            "XXXXXXXGGGGGXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "AAAAAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXAAAAA",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "BBBBXXXXCCCXXXXXXXXXXXXXXXXXXXXXXXXXCCCC",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXAAXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXEEXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXBBXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXAAXXXXXX",
            "XXJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "CCCCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXBBBB",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

      13: ['Absolution', public.BLACK, True, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "CCCCCCCCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXCXXJXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXCCCCCCCXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXCXXXAAXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXCXXXXXXXXXXXXNNXXXXXXXXXXXX",
            "XXXXXXXXXXXXXCXXXXXXXBBXXXXXXXXXOOXXXXXX",
            "XXXXXXXXXXXXXCXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "DDDDDDXXXXXXXCHHHHHHHHHHHHHHHHHHHHHHDDDD",
            "CCCCCCBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCC",
            "XXXXXXXXXXXXXXXXCXXXXXXXXXXXXXIIIIIIIIII",
            "XXXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXCXXXXXXXXXXXXXXXXXXXXXXX",
            "XXFFXXDDDDDDDXXXCXXXXXXXXXXXXXXXXXSXRXQX",
            "CCCCCCCCCCCCCCCCCCCCCCCCCNNNNNNNNCCCCCCC",
            "XXXXXXXXXXXXXXXXAXXXXXXXCXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXAXXXXXXXCXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXAXXXXXXXCCCCBBBBBXXAAAAA",
            "XXXXXXXXXAAAXXXXAXXXXMXXXXXCXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXABBBBBBBXXXCDFDFDFDFDFDF",
            "XXBBBXXXXXXXXXXXAXXXXXXXXXXCCCCCCCCCCCCC",
            "HHHHHHHHHHHHHHHHAHHHHHHHHHHHHHHHHHHHHHHH",
        ]],

      14: ['The End', public.BLACK, False, [
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXXCCCXXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXXXCCCCCXXXXXXXXXXXXXXXXXX",
            "XXXXXXXXXXXXXXXCCCCCCCCCXXXXXXXXXXXXXXXX",
            "XXXJXXXXXXXXCCCCCCCCCCCCCCCXXXXXXXXXXXX",
      ]]


}