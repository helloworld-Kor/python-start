import random

words_dick = {
    "사자": "lion",
    "호랑이": "tiger",
    "사과": "apple",
    "비행기": "airplane"
}

words = []

for word in words_dick:
    words.append(word)
random.shuffle(words)

chance = 3

for i in range(0, len(words)):
    for j in range(0, chance):
        user_input = str(input("{}영어를 말하시오".format(words[i])))
        english = words_dick[words[i]]
        if user_input.strip().lower() == english.lower():
            print("맞쳤습니다")
            break
        else:
            print("틀렸습니디")
    if(user_input.strip().lower() != english.lower()):
        print("정답은 {} 입니다.".format(english.lower()))
print("문제가 더이상 없습니다.")
