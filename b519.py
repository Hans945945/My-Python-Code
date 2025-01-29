n = int(input())
for _ in range(n):
    cards = list(map(int, input().split()))
    cards.sort()
    number = [i%13 for i in cards]
    number.sort()
    color = [(i-1)//13 for i in cards]
    if cards[4]-cards[0] == 4 or (number[0] == 1 and cards[4]-cards[0] == 3 and color[0] == color[1]):
        print(7)
    elif number.count(number[0]) == 4 or number.count(number[1]) == 4:
        print(6)
    elif number[0] == number[1] and number[3] == number[4] and (number[2] == number[0] or number[2] == number[4]):
        print(5)
    elif number[4]-number[0] == 4 or (number[0] == 1 and number[4]-number[0] == 3):
        print(4)
    elif number.count(number[0]) == 3 or number.count(number[1]) == 3 or number.count(number[2]) == 3:
        print(3)
    elif number.count(number[1]) == 2 and number.count(number[3]) == 2:
        print(2)
    elif number.count(number[0]) == 2 or number.count(number[1]) == 2 or number.count(number[2]) == 2 or number.count(number[3]) == 2:
        print(1)
    else:
        print(0)
