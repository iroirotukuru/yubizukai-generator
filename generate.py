import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 【バロック式】各音の穴のふさぎ方（True=ふさぐ、False=あける）
# 配列の意味: [裏穴, 表1, 表2, 表3, 表4, 表5, 表6, 表7]
# 配列の意味：[裏穴, 表1, 表2, 表3, 表4, 表5, 表6, 表7]
FINGERINGS_BAROQUE = {
    'ド': [True, True, True, True, False, False, False, False],     # ソプラノの「ソ」と同じ指
    'レ': [True, True, True, False, False, False, False, False],    # ソプラノの「ラ」と同じ指
    'ミ': [True, True, False, False, False, False, False, False],   # ソプラノの「シ」と同じ指
    'ファ': [True, False, True, False, False, False, False, False],  # ソプラノの高い「ド」と同じ指
    'ソ': [False, False, True, False, False, False, False, False],  # ソプラノの高い「レ」と同じ指
    'ー': None # 伸ばす音（空白）
}


# 教科書の第九（歓喜の歌）1段目〜4段目のメロディデータ
MELODY = [
    ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'ミ', 'レ', 'レ', 'ー'],
    ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'レ', 'ド', 'ド', 'ー'],
    ['レ', 'レ', 'ミ', 'ド', 'レ', 'ミ', 'ファ', 'ミ', 'ド', 'レ', 'ミ', 'ファ', 'ミ', 'レ', 'ド', 'レ', 'ソ', 'ー'],
    ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'レ', 'ド', 'ド', 'ー']
]

def draw_recorder(ax, note):
    """1つの音の運指図を描画する関数"""
    ax.set_xlim(-1, 2)
    ax.set_ylim(-1, 9)
    ax.axis('off')

    # 伸ばす音「ー」の場合は文字だけ表示
    if note == 'ー' or note not in FINGERINGS_BAROQUE:
        ax.text(0.5, 4, 'ー', fontsize=24, ha='center', va='center')
        return

    # 音名のテキスト（ド、レ、ミなど）
    ax.text(0.5, 8.5, note, fontsize=14, ha='center', va='center', weight='bold')

    # リコーダーの本体（輪郭）
    ax.add_patch(patches.Rectangle((0.1, 0), 0.8, 8, edgecolor='black', facecolor='none', lw=2))

    # 各穴のY座標の配置データ [裏穴(左側), 表1, 表2, 表3, 表4, 表5, 表6, 表7]
    hole_positions = [
        (-0.2, 7.2), # 裏穴（左にずらす）
        (0.5, 7.2),  # 表1
        (0.5, 6.2),  # 表2
        (0.5, 5.2),  # 表3
        (0.5, 4.2),  # 表4
        (0.5, 3.2),  # 表5
        (0.5, 2.2),  # 表6
        (0.5, 1.2),  # 表7
    ]

    fingering = FINGERINGS_BAROQUE[note]
    for i, (x, y) in enumerate(hole_positions):
        is_filled = fingering[i]
        color = 'black' if is_filled else 'white' # Trueなら黒丸、Falseなら白丸
        radius = 0.15 if i == 0 else 0.2

        ax.add_patch(patches.Circle((x, y), radius, edgecolor='black', facecolor=color, lw=1.5))

        # 親指の穴が分かりやすいように「裏」とラベルを添える
        if i == 0:
            ax.text(x - 0.2, y, '裏', fontsize=8, ha='right', va='center')

# 全体を4段×横18マスのグリッドで綺麗に並べる
fig, axes = plt.subplots(4, 18, figsize=(24, 12))

for row_idx, row_notes in enumerate(MELODY):
    for col_idx in range(18):
        ax = axes[row_idx, col_idx]
        if col_idx < len(row_notes):
            draw_recorder(ax, row_notes[col_idx])
        else:
            ax.axis('off') # 余った右端のマスは白紙にする

plt.tight_layout()
# 高画質で画像ファイルとして保存
plt.savefig('dai9_baroque_unshi.png', dpi=300)
print("【大成功】4段のバロック式運指画像（dai9_baroque_unshi.png）を保存しました！")
