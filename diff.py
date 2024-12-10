import difflib

def compare_results(core_file, full_file, diff_output_file):
    # ファイルを読み込みます
    with open(core_file, 'r', encoding='utf-8') as f_core:
        core_lines = f_core.readlines()
    with open(full_file, 'r', encoding='utf-8') as f_full:
        full_lines = f_full.readlines()
    
    # 結果を保存するファイルを開く
    with open(diff_output_file, 'w', encoding='utf-8') as f_output:
        # 行数のチェック
        max_lines = max(len(core_lines), len(full_lines))
        
        for i in range(max_lines):
            core_line = core_lines[i].strip() if i < len(core_lines) else ''
            full_line = full_lines[i].strip() if i < len(full_lines) else ''
            
            # 識別子と台本部分を分離
            core_identifier, core_script = (core_line.split(':', 1) + [''])[:2]
            full_identifier, full_script = (full_line.split(':', 1) + [''])[:2]
            
            # 台本部分を比較
            if core_script != full_script:
                f_output.write(f"--- 差分が見つかりました（行 {i+1}） ---\n")
                f_output.write(f"識別子: {core_identifier}\n")
                f_output.write(f"【Core辞書の結果】\n")
                f_output.write(core_script + '\n')
                f_output.write(f"【Full辞書の結果】\n")
                f_output.write(full_script + '\n')
                f_output.write(f"【差分】\n")
                # 差分を表示（文字単位での比較）
                diff = difflib.ndiff(core_script, full_script)
                f_output.write(''.join(diff) + '\n\n')
            else:
                pass
                # f_output.write(f"行 {i+1}（{core_identifier}）: 差分はありません。\n")

# 比較するファイルのパス
core_file = 'sudachi-result.txt'
full_file = 'sudachi-full-result.txt'
diff_output_file = 'diff_results.txt'

compare_results(core_file, full_file, diff_output_file)