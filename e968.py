n = int(input())
absent = list(map(int, input().split()))
print("\n".join([f"No. {i}" for i in range(1, n+1) if i not in absent][::-1]))
                         
        
