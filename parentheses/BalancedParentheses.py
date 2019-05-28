class balanced_parentheses():
    def __init__(self):
        self.parentheses_pair = {'(': ')', '[': ']', '{': '}'}

    # バランスチェック
    def balanced_check(self, bp, str_parentheses, list_count, result):
        # 継続可能かチェック
        paren_list = bp.continue_judge(str_parentheses, result)
        # 最後の場合終了
        if len(paren_list) == (list_count + 1):
            bp.balanced_check(bp, "".join(paren_list), 0, False)
        target_e_kakko = ''
        # ペア閉じ括弧取得
        if paren_list[list_count] in bp.parentheses_pair:
            target_e_kakko = bp.parentheses_pair[paren_list[list_count]]
        # 隣に閉じ括弧がいたら削除
        if paren_list[list_count + 1] == target_e_kakko:
            paren_list[list_count] = ''
            paren_list[list_count + 1] = ''
            list_count = 0
            bp.balanced_check(bp, "".join(paren_list), list_count, True)
        else:
            # ペア閉じかっこじゃなかたら、次へ
            bp.balanced_check(bp, "".join(paren_list), list_count + 1, True)

    # 継続チェック
    def continue_judge(self, str_parentheses, result):
        if result == False:
            print('バランス悪いよ！→' + str_parentheses)
            exit()
        elif result == True and str_parentheses == '':
            print('イイカンジ！！！！')
            exit()
        else:
            print('処理中→' + str_parentheses)
            return list(str_parentheses)


if __name__ == "__main__":
    str_parentheses = input("括弧→{}[]()の組み合わせを入力してね！:")
    bp = balanced_parentheses()
    bp.balanced_check(bp, str_parentheses, 0, True)
