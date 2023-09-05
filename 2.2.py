import random


answer = random.randint(0, 99)
guess = int(input("숫자를 입력하세요(범위 : 0~99) : "))


for i in range(10):

    if answer<guess:
        print("아닙니다. 더 작은 숫자입니다!")
        print(f"숫자를 입력하세요 (범위 : {min(answer, guess)} ~ {max(answer, guess)})")
        guess = int(input(f" "))
    if answer > guess:
        print("아닙니다. 더 큰 숫자입니다!")
        print(f"숫자를 입력하세요 (범위 : {min(answer, guess)} ~ {max(answer, guess)})")
        guess = int(input(f""))
    else:
        break
print("정답입니다. {}번 만에 숫자 {}를 맞추셨습니다." .format(i+1, answer))

