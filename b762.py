N =int(input())
streak = 0
death = 0
kill = 0
assist = 0
for _ in range(N):
    s = input().strip()
    if s != "Get_Kill":
        if s == "Die":
            if streak >= 3:
                print("SHUTDOWN.")
            else:
                print("You have been slained.")
            streak = 0
            death += 1
        else:
            assist += 1
    else:
        streak += 1
        if streak < 3:
            print("You have slain an enemie.")
        elif streak == 3:
            print("KILLING SPREE!")
        elif streak == 4:
            print("RAMPAGE~")
        elif streak == 5:
            print("UNSTOPPABLE!")
        elif streak == 6:
            print("DOMINATING!")
        elif streak == 7:
            print("GUALIKE!")
        else:
            print("LEGENDARY!")

        kill += 1
print(str(kill)+"/"+str(death)+"/"+str(assist))
