'''
PAIZA病院のシステムを解析します。
不正アクセスを試みるクラッカーからユーザーを守るために、ユーザーが設定するパスワードが十分に複雑であるようにしなくてはなりません。
PAIZA病院は、パスワードの複雑さの条件として以下の 3 つを定めました。

・長さが 6 以上
・英字と数字の両方を含む必要がある
・同じ文字を 3 つ以上連続で使用することはできない

なお、英字の大文字と小文字は区別する必要はありません。
パスワードの候補が入力として与えられるので、複雑さの条件をすべて満たす場合は "Valid"、そうでない場合は "Invalid" と出力してください。

例えば、入力例 1 で与えられる 7Caaad9 は 1 つ目の条件と 2 つ目の条件を満たしますが、aaa と 3 つ以上同じ文字が連続で使用されているため、複雑さの条件をすべて満たしません。
'''

input_lines = input()
n = len(input_lines)
out_flg = 0
if n < 6:
    out_flg = 1

str_num_flg = 0
str_alpha_flg = 0
str_equal2_chk = 0

for i in range(n):
    if input_lines[i].isnumeric():
        str_num_flg = 1
    if input_lines[i].isalpha():
        str_alpha_flg = 1
    if i > 0 and input_lines[i-1] == input_lines[i]:
        str_equal2_chk = 1
    if i > 1 and str_equal2_chk == 1 and input_lines[i-1] == input_lines[i]:
        out_flg = 1
if str_num_flg == 0 or str_alpha_flg == 0:
    out_flg = 1
if out_flg == 1:
    print('Invalid')
else:
    print('Valid')
