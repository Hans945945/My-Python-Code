code={
    ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E",
    "..-.":"F","--.":"G","....":"H","..":"I",".---":"J",
    "-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",
    ".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T",
    "..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y",
    "--..":"Z"
}
n = int(input())
for _ in range(n):
    got = input().split()
    print(''.join([code[got[i]] for i in range(len(got))]))
