#0.5s
'''
while True:
    try:
        print("".join([chr(ord(w)-7) for w in input()]))
    except EOFError:
        break
'''
#0.4s
'''
while True:
    try:
        output = bytearray(input(), 'utf-8')
        
        for i in range(len(output)):
            output[i] -= 7

        print((output.decode('utf-8')))
    except EOFError:
        break
'''
#23ms
import sys

translation_table = {chr(i): chr(i - 7) for i in range(32,256)}

input_data = sys.stdin.read()

output = input_data.translate(str.maketrans(translation_table))

sys.stdout.write(output)

