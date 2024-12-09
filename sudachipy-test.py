from sudachipy import dictionary, tokenizer

def katakana_to_hiragana(text):
    """カタカナをひらがなに変換する関数"""
    hiragana = ''
    for char in text:
        code = ord(char)
        # カタカナの範囲内の文字をひらがなに変換
        if 0x30A1 <= code <= 0x30FA:
            hiragana += chr(code - 0x60)
        else:
            hiragana += char
    return hiragana

# Sudachiの辞書をロード
tokenizer_obj = dictionary.Dictionary().create()
mode = tokenizer.Tokenizer.SplitMode.C  # 分割モードを指定

# 結果を保存するファイルを開く
with open('sudachi-result.txt', 'w', encoding='utf-8') as f_output:
    # sample.txtを読み込んで処理
    with open('sample.txt', 'r', encoding='utf-8') as f_input:
        for line in f_input:
            line = line.strip()
            if not line:
                continue
            if ':' in line:
                identifier, script = line.split(':', 1)
                readings = []
                for token in tokenizer_obj.tokenize(script, mode):
                    yomi = token.reading_form()
                    readings.append(yomi)
                katakana_text = ''.join(readings)
                hiragana_text = katakana_to_hiragana(katakana_text)
                output_line = f"{identifier}:{hiragana_text}\n"
                f_output.write(output_line)
            else:
                f_output.write(line + '\n')