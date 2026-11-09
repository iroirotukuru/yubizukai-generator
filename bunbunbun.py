# 別ファイルからの呼び出し例
from recorder_chart import generate_fingering_chart

# ぶんぶんぶんのメロディ（2行構成）
bun_bun_bun = [
    ['ソ', 'ファ', 'ミ', 'レ', 'ド', 'ー', 'ー', 'ー', 'レ', 'レ', 'レ', 'レ', 'ミ', 'ー', 'レ', 'ー'],
    ['レ', 'レ', 'レ', 'レ', 'ミ', 'ー', 'レ', 'ー', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ー', 'ー', 'ー']
]

# 関数を実行して「ぶんぶんぶん」の運指表画像を生成
generate_fingering_chart(bun_bun_bun, 'bun_bun_bun_unshi.png')
