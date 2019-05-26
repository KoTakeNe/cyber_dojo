# ((()))[[({})]]
# ([([])])
# ({[[]]})
# ([([()])])


class balanced_parentheses():
    def __init__(self):
        self.parentheses_pair = {'(': ')', '[': ']', '{': '}'}
        self.f_parentheses_list = ['(', '[', '{']
        self.e_parentheses_list = [')', ']', '}']

    # メイン
    def parentheses_main(self, bp, result, str_parentheses, list_count):
        # 継続可能かチェック
        paren_list = bp.continue_judge(str_parentheses, result, list_count)
        # 対象の開き括弧取得
        f_paren = bp.f_parentheses_list[list_count]
        print('対象開き括弧→' + f_paren)
        # 閉じ括弧を取得
        e_paren = bp.parentheses_pair[f_paren]
        # バランスチェック
        bp.balanced_check(bp, paren_list, f_paren, e_paren, list_count)

    # 継続するか判定する
    def continue_judge(self, str_parentheses, result, list_count):
        if result == False:
            print('1:バランス悪いよ！→' + str_parentheses)
            exit()
        elif list_count > 2 and str_parentheses != '':
            print('2:バランス悪いよ！→' + str_parentheses)
            exit()
        elif result == True and str_parentheses == '':
            print('イイカンジ！！！！')
            exit()
        else:
            print('処理中→' + str_parentheses)
            return list(str_parentheses)

    # バランスチェック
    def balanced_check(self, bp, paren_list, f_paren, e_paren, list_count):
        # 奇数だったら終了
        if len(paren_list) % 2 != 0:
            bp.parentheses_main(bp, False, "".join(paren_list), list_count)

        # 末尾から開き括弧を取得する
        f_paren_length = "".join(paren_list).rfind(f_paren)
        if f_paren_length == -1:  # 開き括弧が見つからない場合、次へ
            bp.parentheses_main(bp, True, "".join(paren_list), list_count+1)
        # リストの要素数と開き括弧の位置の場所が一緒だったら処理終了
        if (f_paren_length+1) == len(paren_list):
            bp.parentheses_main(bp, False, "".join(paren_list), list_count)
        # 対象ではない閉じ括弧が隣にいたら終わり
        if paren_list[f_paren_length+1] in bp.e_parentheses_list:
            if paren_list[f_paren_length+1] != e_paren:
                bp.parentheses_main(bp, False, "".join(paren_list), list_count)

        # 開き括弧からペアの閉じ括弧の位置を調べ、
        # 奇数だったらtrue、偶数だったらfalseとする
        i = len(paren_list)-1
        for paren in reversed(paren_list):
            if paren == f_paren_length:
                break
            if paren == e_paren:
                search_length = i
            i -= 1
        # ペアが存在かつ奇数かを確認する
        print('奇数確認' + str((search_length+1) - (f_paren_length + 1)))
        if search_length != -1 and ((search_length+1) - (f_paren_length + 1)) % 2 != 0:
            paren_list[f_paren_length] = ""
            print(search_length)
            paren_list[search_length] = ""
            bp.parentheses_main(bp, True, "".join(paren_list), list_count)
        else:
            bp.parentheses_main(bp, False, "".join(paren_list), list_count)


if __name__ == "__main__":
    str_parentheses = input("括弧→{}[]()の組み合わせを入力してね！:")
    bp = balanced_parentheses()
    bp.parentheses_main(bp, True, str_parentheses, 0)
