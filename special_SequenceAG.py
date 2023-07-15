s = input()
def special_Sequence_AG(s):
 A_Count = 0
 res = 0
 for c in s:
    if c == "A":
        A_Count  += 1
    elif c == "G":
        res += A_Count
 return res
print(special_Sequence_AG("ABCGAG"))
print(special_Sequence_AG("GAB"))
print(special_Sequence_AG(s))
print(special_Sequence_AG("AGGGGGAG"))