word={"HELLO":"ENGLISH","HOLA":"SPANISH","HALLO":"GERMAN","BONJOUR":"FRENCH","CIAO":"ITALIAN","ZDRAVSTVUJTE":"RUSSIAN"}
x = 1
while True:
    S = input()
    if S == "#":
        break
    print(f"Case {x}: {word.get(S, 'UNKNOWN')}")
    x+=1
