while True:
    n = int(input())
    if n ==0:
        break
    elif n == 1:
        print("Discarded cards:")
        print(f'Remaining card: 1')
    else:
        cards = [i for i in range(1,n+1)]
        print("Discarded cards:", end = "")
        for i in range(n-2):
            print(f' {cards.pop(0)},', end = "")
            cards.append(cards.pop(0))
        print(f" {cards.pop(0)}")
        print(f'Remaining card: {cards[0]}')
        
