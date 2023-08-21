"""
食堂供餐
题目描述
某公司员工食堂以盒饭方式供餐。

为将员工取餐排队时间降低为0，食堂的供餐速度必须要足够快。

现在需要根据以往员工取餐的统计信息，计算出一个刚好能达成排队时间为
0的最低供餐速度。即，食堂在每个单位时间内必须至少做出多少价盒饭才能满足要求。

输入描述
第1行为一个正整数N，表示食堂开餐时长。
1≤N≤1000
第2行为一个正整数M，表示开餐前食堂已经准备好的盒饭份数。
P1≤M≤1000
第3行为N个正整数，用空格分隔，依次表示开餐时间内按时间顺序每个单位时间进入食堂取餐的人数Pi。
1≤i≤N
0≤Pi≤100
输出描述
一个整数，能满足题目要求的最低供餐速度(每个单位时间需要做出多少份盒饭)

备注
每人只取一份盒饭。
需要满足排队时间为0，必须保证取餐员工到达食堂时，食堂库存盒饭数量不少于本次来取餐的人数。
第一个单位时间来取餐的员工只能取开餐前食堂准备好的盒饭。
每个单位时间里制作的盒饭只能供应给后续单位时间来的取餐的员工。
食堂在每个单位时间里制作的盒饭数量是相同的。
样例
输入

3
14
10 4 5
输出

3
说明

本样例中，总共有3批员工就餐，每批人数分别为
10、4、5。 开餐前食堂库存
14份 食堂每个单位时间至少要做出
3份餐饭才能达成排队时间为
0的目标。具体情况如下:

第一个单位时间来的10位员工直接从库存取餐。取餐后库存剩余
4份盒饭，加上第一个单位时间做出的
3份，库存有7份
第二个单位时间来的4位员工从库存的7份中取4份。取餐后库存剩余
3份盒饭，加上第二个单位时间做出的3份，库存有6份。
第三个单位时间来的员工从库存的6份中取5份，库存足够。
如果食堂在单位时间只能做出2份餐饭，则情况如下：

第一个单位时间来的10位员工直接从库存取餐。取餐后库存剩余4份盒饭，加上第一个单位时间做出的
2份，库存有6份。
第二个单位时间来的4位员工从库存的6份中取4份。取餐后库存剩余
2份盒饭，加上第二个单位时间做出的2份，库存有4份。
第三个单位时间来的员工需要取5份，但库存只有
4份，库存不够。


100
57
39 78 43 66 72 0 54 2 75 93 87 54 2 10 15 34 28 98 28 87 90 33 5 27 73 48 36 40 93 73 71 67 26 24 65 50 90 96 83 64 29 94 44 19 98 54 4 72 39 47 47 15 37 54 53 84 55 8 64 26 23 6 20 64 54 26 94 49 97 5 82 13 17 70 48 17 74 10 74 13 88 72 11 93 15 18 24 99 2 43 78 96 99 35 64 61 23 53 78 99
"""

"""
思路: 暴力枚举法
使用二分法缩短时间
1. 枚举上餐速度，找到符合要求的最低上餐速度
2. 复习的时候看看这是如何进行二分的，以及while条件判断退出，很重要！
"""


def main():
    total_time = int(input())
    total_rice = int(input())
    consume_list = list(map(int, input().split()))

    left_speed, right_speed = 1, 100
    min_speed = 100   # 满足需求最低速度
    while left_speed <= right_speed:
        speed = (left_speed + right_speed) // 2
        need_quicker = 0
        this_rice = total_rice
        # 模拟进餐
        for consumer in consume_list:
            if consumer > this_rice:   # 供餐不足，需要加速
                need_quicker = 1
                break
            this_rice -= consumer   ## 每回合都要加
            this_rice += speed     ## 每回合都要加
        if need_quicker:    # 供餐不足，需要加速
            left_speed = speed + 1
        else:       # 供餐足够，记录结果，再看有没有更低速的, 降速
            right_speed = speed - 1
            min_speed = min(min_speed, speed)
    return min_speed


print(main())
