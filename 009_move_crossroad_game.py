'''あなたは作りかけのゲームプログラムを発見しましたが、キャラクターの動きの制限する方法が未実装でした。 
制作中のゲームは、縦方向に H マスと横方向に W マスだけ広がる格子上のマップを用います。
左下のマスが原点であり、その座標を (0, 0) とします。
原点から横方向に x マス、縦方向に y マス進んだ座標を (x, y) と表記します。
現在の開発段階では障害物などはなく、キャラクターの初期座標が必ず (0, 0) です。
この状態から合計で N 回の上下左右への移動操作が行われます。
各移動操作はキャラクターの座標 (x, y) を以下のように変更します。
・上への移動 : キャラクターの座標を (x, y) から (x, y + 1) へ変更する。
・下への移動 : キャラクターの座標を (x, y) から (x, y - 1) へ変更する。
・左への移動 : キャラクターの座標を (x, y) から (x - 1, y) へ変更する。
・右への移動 : キャラクターの座標を (x, y) から (x + 1, y) へ変更する。
開発依頼書には、N 回の操作中にキャラクターが不正な座標にいることがないか判定するプログラムの作成が指示されています。
ここで不正な座標とは、マップ外の座標、すなわち格子上に存在しない座標すべてのことを指します。
例えば、入力例 1 および入力例 2 は以下のように考えることができます。'''

input_lines = input()
numbers = input_lines.split()
max_height = int(numbers[0]) - 1
max_width  = int(numbers[1]) - 1
move_times = int(numbers[2])
height  = 0
width   = 0
out_flg = 0
for i in range(move_times):
    k = input()
    if   k == 'U':
        height += 1
        if height > max_height:
            out_flg = 1
            break
    elif k == 'D':
        height -= 1
        if height < 0:
            out_flg = 1
            break
    elif k == 'R':
        width  += 1
        if width > max_width:
            out_flg = 1
            break
    elif k == 'L':
        width  -= 1
        if width < 0:
            out_flg = 1
            break
if out_flg == 1:
    print('invalid')
else:
    print('valid')
