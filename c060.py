import sys
r = []
for s in sys.stdin:
    nums = list(map(int, s.split()))
    words = ""
    first = 1
    for i in range(9):
        n = nums[i]
        if n != 0:
            if n > 0:
                if first:
                    first = 0
                    if i < 7:
                        if n == 1:
                            words += f"x^{8-i}"
                        else:
                            words += f"{n}x^{8-i}"
                    elif i == 7:
                        if n == 1:
                            words += f"x"
                        else:
                            words += f"{n}x"
                    else:
                        words += f"{n}"
                else:
                    if i < 7:
                        if n == 1:
                            words += f" + x^{8-i}"
                        else:
                            words += f" + {n}x^{8-i}"
                    elif i == 7:
                        if n == 1:
                            words += f" + x"
                        else:
                            words += f" + {n}x"
                    else:
                        words += f" + {n}"
            else:
                if first:
                    first = 0
                    if i < 7:
                        if n == -1:
                            words += f"-x^{8-i}"
                        else:
                            words += f"-{-n}x^{8-i}"
                    elif i == 7:
                        if n == -1:
                            words += f"-x"
                        else:
                            words += f"-{-n}x"
                    else:
                        words += f"-{-n}"
                else:
                    if i < 7:
                        if n == -1:
                            words += f" - x^{8-i}"
                        else:
                            words += f" - {-n}x^{8-i}"
                    elif i == 7:
                        if n == -1:
                            words += f" - x"
                        else:
                            words += f" - {-n}x"
                    else:
                        words += f" - {-n}"
    r.append(words if words else "0")
sys.stdout.write("\n".join(r)+"\n")
