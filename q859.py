while 1:
    try:
        n = int(input())
        a = n%12
        if a == 0:
            print("Aspect of Combat")
        elif a == 1:
            print("Ringmaster Scarr")
        elif a == 2:
            print("Night Rose")
        elif a == 3:
            print("Aspect of Speed")
        elif a == 4:
            print("Shrouded Striker")
        elif a == 5:
            print("Unstoppable")
        elif a == 6:
            print("Aspect of Siphon")
        elif a == 7:
            print("Infernal Defenses")
        elif a == 8:
            print("The Machinist")
        elif a == 9:
            print("Shogun X")
        elif a == 10:
            print("Megalo Don")
        else:
            print("Aspect of Agility")
    except EOFError:
        break
