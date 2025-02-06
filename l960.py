table = ("Sunday", "Monday", "Tuesday", "Wednesday","Thursday","Friday",'Saturday')
day = input()
print(table.index(day) if day in table else "error")
