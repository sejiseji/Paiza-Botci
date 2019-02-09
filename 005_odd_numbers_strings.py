'''ある暗号化された文字列 S が与えられます。
文字列 S のうち奇数文字目を取り出せば解読できることがわかりました。

文字列 S が与えられるので奇数文字目の文字を取り出して解読した文字列を出力してください。
'''

input_lines = input()
ans = ''
n = len(input_lines)
for i in range(n):
    if i % 2 == 0:
        ans = ans + input_lines[i]
print(ans)
