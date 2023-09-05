h = int(input("피라미드의 높이를 입력하세요: "))
for i in range(h):
    print(" " * (2*(h - i)-1), end=" ")
    for j in range(i+1):
        print(2 * j + 1, end=" ")
    for j in range(i, 0, -1):
        print(2*j - 1, end=' ')
    print("\n")
print("계속하려면 아무 키나 누르십시오 . . . ")
