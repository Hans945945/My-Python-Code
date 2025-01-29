while True:
    try:
        n = float(input())
        abs_n = abs(n)
        n = f'{n:.4f}'
        abs_n = f'{abs_n:.4f}'
        print(f"|{n}|={abs_n}")
    except:
        break
