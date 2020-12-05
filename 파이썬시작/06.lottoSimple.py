import random

count = int(input("몇개를 뽑으실겁니까"))
tmp = 0

for i in range(0, count):

    lotto = []
    ran_num = random.randint(1, 46)

    for i in range(0, 6):
        while ran_num in lotto:
            ran_num = random.randint(1, 46)
        lotto.append(ran_num)

    lotto.sort()
    print(lotto)
    tmp += 1
