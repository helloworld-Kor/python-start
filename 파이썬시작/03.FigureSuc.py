import random
import os
number1 = random.randint(1, 10)


def ck_Count(msg, casting=int):
    while True:
        try:
            hitCount = casting(input("숫자를 맞춰보시오:"))
            return hitCount
        except:
            continue


print(number1)
chance = 4
count = 0
# print(number1 == hitCount)
os.system("cls")
while chance > count:
    count += 1
    hitCount = ck_Count("몇일까요?")
    if number1 == hitCount:
        break
    elif number1 < hitCount:
        print("{}보다 작습니다".format(hitCount))
    elif number1 > hitCount:
        print("{}보다 큽니다".format(hitCount))

if number1 == hitCount:
    print("성공! 정답은 {}".format(number1))
else:
    print("실패! 정답은 {}".format(number1))
