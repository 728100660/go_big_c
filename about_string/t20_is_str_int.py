"""
剑指 Offer 20. 表示数值的字符串
中等
526
相关企业
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]


示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = "    .1  "
输出：true


提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
"""
# 学一手确定有限状态自动机 吧，if else有点太难了
if __name__ == '__main__':
    def is_number(string):
        # 0 啥都没有 1: 第一个正负号   2: 符号+num   3: 符号+num+.    4: 符号 + num + . + num
        # 5: 符号 + num + . + num + E/e   6: 符号 + num + . + num + E/e + 符号
        # 7: 符号 + num + . + num + E/e + 符号 + num    8: 符号 + num + . + num + E/e + 符号 + num +    后加空格，此阶段不能再有数字了
        if not string:
            return False
        s_end = string[-1]
        if "a" <= s_end <= "z" or "A" <= s_end <= "Z" or s_end in ("+", "-"):
            return False
        stage = 0
        max_idx = len(string) - 1
        for idx, s1 in enumerate(string):
            if stage == 8 and s1 != " ":
                return False
            if ord("a") <= ord(s1) <= ord("z") or ord("A") <= ord(s1) <= ord("Z"):
                if s1 not in ("e", "E"):     # 非法字符
                    return False
                if stage not in (2, 3, 4):     # 非法字符
                    return False
                stage = 5
            elif ord("0") <= ord(s1) <= ord("9"):
                if stage in (0, 1, 2):
                    stage = 2
                elif stage in (3, 4):
                    stage = 4
                elif stage in (5, 6, 7):
                    stage = 7
            elif s1 in("-", "+"):
                if stage == 0:
                    stage = 1
                elif stage == 5:
                    stage = 6
                else:
                    return False
            elif s1 == " ":
                if stage in (1, 5, 6):     # 非法字符
                    return False
                elif stage != 0:
                    stage = 8
            elif s1 == ".":
                if stage not in (0, 1, 2):     # 非法字符
                    return False
                # 前后都为空或者不存在就是非法的数据
                pre_val = string[idx - 1] if idx - 1 >= 0 else " "
                next_val = string[idx + 1] if idx + 1 <= max_idx else " "
                if pre_val in (" ", "-", "+") and next_val in (" ", "e", "E"):
                    return False
                stage = 3
        return True if stage in (2, 3, 4, 7, 8) else False

    assert is_number("0") == True
    assert is_number("e") == False
    assert is_number(".") == False
    assert is_number("    .1  ") == True
    assert is_number("    -.1  ") == True
    assert is_number("    -.1+   ") == False
    assert is_number("     ") == False
    assert is_number("  3.  ") == True
    assert is_number("  .3  ") == True
    assert is_number("  .  ") == False
    assert is_number("+-.") == False
    assert is_number("-.") == False
    assert is_number("46.e3") == True
    assert is_number(".e3") == False
    assert is_number("6ee69") == False
    assert is_number(" 005047e+6") == True
