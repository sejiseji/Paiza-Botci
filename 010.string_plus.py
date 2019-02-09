'''
単語を組み合わせて新単語を作ります。
新単語は N 個の文字列を、前から順に結合して作ります。
この時、冗長さをなくすため、 前から結合した単語の末尾 と 後ろの単語の先端 が一番長く一致するように結合します。
例えば、 入力例 1 の "paiza", "apple", "letter" の場合、
先頭から "paiza", "apple" を条件どおり重ねると "paizapple" となります。
この単語を更に次の単語と重ねると "paizappletter" となります。
なお、必ず前から順番に重ねるため、 入力例 2 の "poh", "p", "oh" を結合する場合は、
"poh" と "p" を重ねた後の単語 "pohp" と "oh" を重ね "pohpoh" となります。
N 個の単語が与えられるので、前から順番に単語を結合した場合の新単語を出力してください。
'''
n = int(input())
#n = 2
word_plus   = ''
for i in range(n):
    if i == 0:
        word_before = input()
#       word_before = 'paiza'
        length_b = len(word_before)
        word_plus += word_before
    elif i > 0:
        word_after  = input()
#       word_after = 'jaiho'
        length_a = len(word_after)
        if length_a <= length_b:
            l = length_a
        else:
            l = length_b
        for j in range(l):
            chklit_a = word_after[:l - j]
            chklit_b = word_before[-(l - j):]
            if chklit_a == chklit_b:
                word_plus += word_after[l - j :]
                break
            elif len(chklit_a) == 1 and chklit_a != chklit_b:
                word_plus += word_after
#           print(str(j) + " " + word_before[-(l - j):] + " " + word_after[:l - j] + " " + word_plus)
#       print(str(j) + " " + word_before[-(l - j):] + " " + word_after[:l - j] + " " + word_plus)
        word_before = word_plus
        length_b = len(word_before)
print(word_plus)
