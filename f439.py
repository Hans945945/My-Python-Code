day = 1
while True:
    try:
        time_table = [600]
        for _ in range(int(input())):
            temp = input().split()
            start = temp[0]
            end = temp[1]
            SH, SM = map(int, start.split(":"))
            start = SH*60+SM
            time_table.append(start)
            EH, EM = map(int, end.split(":"))
            end = EH*60+EM
            time_table.append(end)
        time_table.append(18*60)
        temp = [b-a for a,b in zip(time_table[:-1], time_table[1:])]
        diff = [temp[i] for i in range(len(temp)) if i % 2 == 0]
        nap = max(diff)
        nap_start = time_table[diff.index(nap)*2]
        NSH = str(nap_start//60)
        NSM = str(nap_start%60)
        if len(NSH) < 2:
            NSH = "0"+NSH
        if len(NSM) < 2:
            NSM = "0"+NSM
        if nap >= 60:
            NH = nap // 60
            NM = nap % 60
            print(f"Day #{day}: the longest nap starts at {NSH}:{NSM} and will last for {NH} hours and {NM} minutes.")
        else:
            print(f"Day #{day}: the longest nap starts at {NSH}:{NSM} and will last for {nap} minutes.")
        day += 1
    except EOFError:
        break
