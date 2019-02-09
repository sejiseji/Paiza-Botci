'''
あなたは書類の整理をしています。
書類には 1 から 3 までの重要度 e が設定されています。数字が大きいほど重要な書類とされています。
書類のタイトル文字列 S_i と重要度 e_i が n 件与えられます。
重要度が 3 の書類のタイトルのみを入力された順に出力してください。

入力される値
n
S_1 e_1
...
S_n e_n
・1 行目は与えられる書類の件数 n が与えられます。
・2 行目から 2 + n 行目に書類のタイトル文字列 S_i と重要度 e_i が与えられます。
・入力は 2 + n 行となり、末尾に改行が 1 つ入ります。
'''
n = int(input())
books_value3 = []
i = 0
for k in range(n-1):
    a = input()
    book = a.split()[0]
    value = a.split()[1]
    if value == "3":
        books_value3.append(book)
        i += 1
for k in range(i):
    print(books_value3[k])
