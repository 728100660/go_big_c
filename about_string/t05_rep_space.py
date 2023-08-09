"""
剑指 Offer 05. 替换空格
简单
525
相关企业
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。



示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."


限制：

0 <= s 的长度 <= 10000
"""
if __name__ == '__main__':
    def func(s):
        return s.replace(" ", "%20")      # 速度太慢了

    assert func("We are happy.") == "We%20are%20happy."