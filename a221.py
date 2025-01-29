T = int(input())
for k in range(1,T+1):
    user = input()
    correct = input()
    if user == correct or user.rstrip() == correct:
        print(f'Case {k}: Yes')
    elif ''.join(user.split()) == correct:
        print(f"Case {k}: Output Format Error")
    else:
         print(f'Case {k}: Wrong Answer')
