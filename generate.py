import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 【バロック式】各音の穴のふさぎ方（True=ふさぐ、False=あける）
# 配列の意味：[裏穴, 表1, 表2, 表3, 表4, 表5, 表6, 表7]
FINGERINGS_BAROQUE = {
    '低ソ': [True, True, True, True, True, True, True, True],       # 【追加】一番低いソ（全閉）
    'ド': [True, True, True, True, False, False, False, False],     # ソプラノの「ソ」と同じ
    'レ': [True, True, True, False, False, False, False, False],    # ソプラノの「ラ」と同じ
    'ミ': [True, True, False, False, False, False, False, False],   # ソプラノの「シ」と同じ
    'ファ': [True, False, True, False, False, False, False, False],  # ソプラノの高い「ド」と同じ
    'ソ': [False, False, True, False, False, False, False, False],  # ソプラノの高い「レ」と同じ
    '高ド': [False, False, True, True, True, False, True, True],    # 【追加】高いド（ソプラノの高いファと同じ）
    '高レ': [False, False, True, True, True, True, True, False],    # 【追加】高いレ（ソプラノの高いソと同じ）
    'ー': None # 伸ばす音（空白）
}

def draw_recorder(ax, note):
    """1つの音の運指図を描画する内部関数"""
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

def generate_fingering_chart(melody, output_filename='recorder_unshi.png'):
    """
    外部からメロディ（2次元配列）を受け取り、運指表の画像を生成・保存する関数
    """
    num_rows = len(melody)
    # 最も長い行の音数、または最低18マスを確保
    max_cols = max(max(len(row) for row in melody), 18) 
    
    # 動的にグリッドサイズを設定
    fig, axes = plt.subplots(num_rows, max_cols, figsize=(max_cols * 1.33, num_rows * 3))

    # 1行だけの場合は axes が1次元配列になるため2次元に統一
    if num_rows == 1:
        axes = axes.reshape(1, -1)

    for row_idx, row_notes in enumerate(melody):
        for col_idx in range(max_cols):
            ax = axes[row_idx, col_idx]
            if col_idx < len(row_notes):
                draw_recorder(ax, row_notes[col_idx])
            else:
                ax.axis('off') # 余った右端のマスは白紙にする

    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.close() # メモリ解放
    print(f"【大成功】運指画像（{output_filename}）を保存しました！")

# テスト用のメイン処理：第九の完全版（4段構成）
if __name__ == '__main__':
    # 第九（歓喜の歌）完全版メロディ
    TEST_MELODY = [
        ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'ミ', 'レ', 'レ', 'ー'], # 1段目
        ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'レ', 'ド', 'ド', 'ー'], # 2段目
        ['レ', 'レ', 'ミ', 'ド', 'レ', 'ミ', 'ファ', 'ミ', 'ド', 'レ', 'ミ', 'ファ', 'ミ', 'レ', 'ド', 'レ', '低ソ', 'ー'], # 3段目（低いソが登場）
        ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'レ', 'ド', 'ド', 'ー']  # 4段目
    ]
    
    # ※もし「高ド」「高レ」を使ったサビの山場（別パートなど）を試したい場合は、以下を有効にしてください
    # TEST_MELODY = [
    #     ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'ミ', 'レ', 'レ', 'ー'],
    #     ['ミ', 'ミ', 'ファ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'レ', 'ド', 'ド', 'ー'],
    #     ['レ', 'レ', 'ミ', 'ド', 'レ', 'ミ', 'ファ', 'ミ', 'ド', 'レ', 'ミ', 'ファ', 'ミ', 'レ', 'ド', 'レ', '低ソ', 'ー'],
    #     ['高ド', '高ド', '高レ', 'ソ', 'ソ', 'ファ', 'ミ', 'レ', 'ド', 'ド', 'レ', 'ミ', 'レ', 'ド', 'ド', 'ー'] # 4段目を山場アレンジにする場合
    # ]

    generate_fingering_chart(TEST_MELODY, 'dai9_full_unshi.png')
