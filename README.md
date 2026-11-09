# yubizukai-generator
リコーダーの指遣いを生成するスクリプト
# 使い方
```python
# 別ファイルからの呼び出し例
from generate_chart import generate_fingering_chart

# 弾きたい新しいメロディを外から指定
my_melody = [
    ['ド', 'レ', 'ミ', 'ファ', 'ソ', 'ー', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ー']
]

# 関数を実行して画像を生成
generate_fingering_chart(my_melody, 'my_song_unshi.png')
 ```
