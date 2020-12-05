import os

operlator = ["+", "-", "/", "*", "="]

s = input("계산식을 입력해주세여 ")
s += "="
tmpindex = []
string_list = []
string_list = s

# print(string_list)
tmp_cal = 0


for i, s in enumerate(s):
    if s in operlator:
        tmpindex.append(i)
        # print(s)
    if len(tmpindex) == 2:
        print(string_list[:tmpindex[1]])
        print(eval(string_list[:tmpindex[1]]))
        del string_list[0:tmpindex[1]]

        del tmpindex[0]

# for i in range(0, len(tmpindex)):
#     print(string_list[tmpindex[i]])
# print(string_list[tmpindex])
